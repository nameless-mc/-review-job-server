from typing import Any, Union
from fastapi import APIRouter, Cookie, Depends
from pydantic import BaseModel
from sqlalchemy import asc
from db import get_db, idgen
from utils.signin_manager import get_user
from sqlalchemy.orm import Session
from utils.error import forbiddenError, resourceNouFoundError
from model import Group, Join, User, Review, Category

router = APIRouter()


@router.get("/api/groups/{group_id}/reviews")
async def get_reviews(group_id: int, q: Union[str, None] = None, category: Union[str, None] = None, sort_target: Union[str, None] = None, order: Union[str, None] = None, token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None), db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError

    group = db.get(Group, group_id)

    if(group is None):
        return resourceNouFoundError("group")

    join = db.get(Join, {"user_id": user.id, "group_id": group.id})

    if(join is None):
        return resourceNouFoundError("group")

    query = db.query(
        Review,
        User,
        Category,
        Review.id.label("id"),
        Review.name.label("name"),
        User.id.label("user_id"),
        User.name.label("user_name"),
        Review.note.label("note"),
        Category.id.label("category_id"),
        Category.name.label("category_name"),
        Review.star.label("star")
    ).join(
        User,
        Review.user_id == User.id
    ).join(
        Category,
        Review.category_id == Category.id
    ).filter(
        Review.group_id == group_id
    )

    query = query.order_by(asc(Review.name))

    reviews = query.all()

    def query_to_result(query_result):
        return{
            "id": query_result.id,
            "name": query_result.name,
            "user_id": query_result.user_id,
            "user_name": query_result.user_name,
            "note": query_result.note,
            "category_name": query_result.category_name,
            "category_id": query_result.category_id,
            "star": query_result.star
        }

    results = list(map(query_to_result, reviews))

    return {
        "reviews": results
    }


@router.get("/api/groups/{group_id}/reviews/{review_id}")
async def get_review(group_id: int, review_id: int, token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None), db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError

    group = db.get(Group, group_id)

    if(group is None):
        return resourceNouFoundError("group")

    join = db.get(Join, {"user_id": user.id, "group_id": group.id})

    if(join is None):
        return resourceNouFoundError("group")

    query_result: Any = db.query(
        Review,
        User,
        Category,
        Review.id.label("id"),
        Review.name.label("name"),
        User.id.label("user_id"),
        User.name.label("user_name"),
        Review.note.label("note"),
        Category.id.label("category_id"),
        Category.name.label("category_name"),
        Review.star.label("star")
    ).join(
        User,
        Review.user_id == User.id
    ).join(
        Category,
        Review.category_id == Category.id
    ).filter(
        Review.id == review_id
    ).first()

    if(query_result is None):
        return resourceNouFoundError("review")

    return{
        "id": query_result.id,
        "name": query_result.name,
        "user_id": query_result.user_id,
        "user_name": query_result.user_name,
        "note": query_result.note,
        "category_name": query_result.category_name,
        "category_id": query_result.category_id,
        "star": query_result.star
    }


class PostReviewSchema(BaseModel):
    name: str
    note: str
    category_id: int
    star: int


@router.post("/api/groups/{group_id}/reviews")
async def post_review(data: PostReviewSchema, group_id: int, token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None), db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError

    group = db.get(Group, group_id)

    if(group is None):
        return resourceNouFoundError("group")

    join = db.get(Join, {"user_id": user.id, "group_id": group.id})

    if(join is None):
        return resourceNouFoundError("group")

    category = db.get(Category, data.category_id)

    if(category is None):
        return resourceNouFoundError("category")
    
    review = Review(
        id=idgen(),
        user_id=user.id,
        group_id=group_id,
        name=data.name,
        note=data.note,
        category_id=data.category_id,
        star=data.star
    )

    db.add(review)
    db.commit()

    return {
        "id": review.id,
        "name": review.name,
        "user_id": user.id,
        "user_name": user.name,
        "note": review.note,
        "category_name": category.name,
        "category_id": category.id,
        "star": review.star
    }
