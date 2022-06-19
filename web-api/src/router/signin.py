from fastapi.responses import JSONResponse
from fastapi import APIRouter, Cookie, Depends, Response
from pydantic import BaseModel
from db import get_db, idgen
from model import User
from utils.signin_manager import check_password, hash
from sqlalchemy.orm import Session
from utils.error import invalidParameterError


class SigninSchema(BaseModel):
    password: str
    id: str


class SignupSchema(BaseModel):
    password: str
    id: str
    name: str


router = APIRouter()


@router.post("/api/signin")
async def signin(res: Response, data: SigninSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.signin_id == data.id).first()
    if(user is None):
        print("invalid signin_id")
        return invalidParameterError
    if(not check_password(data.password, user)):
        print("invalid password")
        return invalidParameterError
    res.set_cookie("token", user.password, samesite="none", secure=True)
    res.set_cookie("id", user.id, samesite="none", secure=True)


@router.post("/api/signout")
async def signout(res: Response):
    res.delete_cookie("token")
    res.delete_cookie("id")


@router.post('/api/signup')
async def signup(res: Response, data: SignupSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.signin_id == data.id).first()
    if(user is not None):
        return JSONResponse(status_code=400, content={"code": "DuplicateId"})
    id = idgen()
    password = hash(data.password)
    user = User(
        id=id,
        signin_id=data.id,
        name=data.name,
        password=password
    )
    db.add(user)
    db.commit()
    res.set_cookie("token", password, samesite="none", secure=True)
    res.set_cookie("id", id, samesite="none", secure=True)
