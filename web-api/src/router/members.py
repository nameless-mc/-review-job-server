from typing import Union
from fastapi import APIRouter, Cookie, Depends, Response
from pydantic import BaseModel
from sqlalchemy import asc, func, outerjoin
from db import get_db, idgen
from utils.signin_manager import get_user
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from utils.error import forbiddenError, resourceNouFoundError
from model import Group, Join, User, Review

router = APIRouter()


@router.get("/api/groups/{group_id}/members")
async def get_members(group_id: int, token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None), db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError

    group = db.get(Group, group_id)

    if(group is None):
        return resourceNouFoundError("group")

    join = db.get(Join, {"user_id": user.id, "group_id": group.id})

    if(join is None):
        return resourceNouFoundError("group")

    sub = (db.query(Review.user_id.label("user_id"), func.count(Review.id).label(
        "count")).filter(Review.group_id == group_id).group_by(Review.user_id)).subquery("sub")

    members = db.query(Join, sub, User.id.label("id"), User.name.label("name"), sub.c.count).join(User, Join.user_id == User.id).join(sub, Join.user_id == sub.c.user_id, isouter=True).filter(
        Join.group_id == group_id
    )

    def query_to_result(query_result):
        return{
            "id": query_result.id,
            "name": query_result.name,
            "review_counts": query_result.count if query_result.count is not None else 0
        }

    results = list(map(query_to_result, members))

    return{
        "members": results
    }


@router.get("/api/groups/{group_id}/members/{user_id}")
async def get_mamber(group_id: int, user_id: int, token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None), db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError

    group = db.get(Group, group_id)

    if(group is None):
        return resourceNouFoundError("group")

    join = db.get(Join, {"user_id": user.id, "group_id": group.id})

    if(join is None):
        return resourceNouFoundError("group")

    target_user = db.get(User, user_id)

    if(target_user is None):
        return resourceNouFoundError("user")

    reviews = db.query(Review).filter(Review.group_id ==
                                      group_id, Review.user_id == user_id).all()

    def reviews_query_to_result(query_result):
        return{
            "id": query_result.Review.id,
            "name": query_result.Review.name,
            "note": query_result.Review.note,
            "category_name": query_result.Review.category_name,
            "category_id": query_result.Review.category_id,
            "star": query_result.Review.star
        }

    reviews_results = list(map(reviews_query_to_result, reviews))

    return {
        "user_id": target_user.id,
        "user_name": target_user.name,
        "review_counts": len(reviews_results),
        "reviews": reviews_results
    }