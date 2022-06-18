from typing import List, Union
from fastapi import APIRouter, Cookie, Depends
from pydantic import BaseModel
from db import get_db, idgen
from utils.signin_manager import get_user
from sqlalchemy.orm import Session
from utils.error import forbiddenError
from model import  Category

router = APIRouter()


@router.get("/api/categories")
async def get_categories(token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None), db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError
    categories = db.query(Category).all()

    results = list(map(Category.toResultJSON, categories))

    return {
        "categories": results
    }


class CategorySchema(BaseModel):
    name: str


class PostCategoriesSchema(BaseModel):
    categories: List[CategorySchema]


@router.post("/api/categories")
async def post_categories(data: PostCategoriesSchema, token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None), db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError

    categories = list(map(lambda c: Category(
        id=idgen(), name=c.name), data.categories))

    db.add_all(categories)
    db.commit()

    categories = db.query(Category).all()

    results = list(map(Category.toResultJSON, categories))

    return {
        "categories": results
    }
