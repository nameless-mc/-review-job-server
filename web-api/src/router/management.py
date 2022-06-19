from fastapi import APIRouter, Depends
from db import get_db
from sqlalchemy.orm import Session
from model import Group, Join, User, Review, Category

router = APIRouter()


@router.get("/management/users")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    def query_to_result(query_result):
        return{
            "id": query_result.id,
            "name": query_result.name,
            "signin_id": query_result.signin_id,
            "password": query_result.password
        }

    results = list(map(query_to_result, users))
    return {
        "users": results
    }


@router.get("/management/groups")
async def get_groups(db: Session = Depends(get_db)):
    groups = db.query(Group).all()
    results = list(map(Group.toResultJSON, groups))
    return {
        "groups": results
    }


@router.get("/management/joins")
async def get_joins(db: Session = Depends(get_db)):
    joins = db.query(Join).all()

    def query_to_result(query_result):
        return{
            "user_id": query_result.user_id,
            "group_id": query_result.group_id,
        }
    results = list(map(query_to_result, joins))
    return {
        "joins": results
    }


@router.get("/management/reviews")
async def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(Review).all()

    def query_to_result(query_result):
        return{
            "id": query_result.id,
            "user_id": query_result.user_id,
            "group_id": query_result.group_id,
            "name": query_result.name,
            "note": query_result.note,
            "category_id": query_result.category_id,
            "star": query_result.star,
        }
    results = list(map(query_to_result, reviews))
    return {
        "reviews": results
    }


@router.get("/management/categories")
async def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()

    def query_to_result(query_result):
        return{
            "id": query_result.id,
            "name": query_result.name,
        }
    results = list(map(query_to_result, categories))
    return {
        "categories": results
    }
