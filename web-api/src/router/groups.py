from typing import Union
from fastapi import APIRouter, Cookie, Depends, Response
from pydantic import BaseModel
from sqlalchemy import asc
from db import get_db, idgen
from utils.signin_manager import get_user
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from utils.error import forbiddenError, resourceNouFoundError
from model import Group, Join, User

router = APIRouter()


@router.get("/api/groups")
async def get_groups(token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None), db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError

    groups = db.query(Join, Group, Group.id, Group.name, Group.code).join(
        Group, Join.group_id == Group.id
    ).filter(Join.user_id == user.id).order_by(asc(Group.name)).all()

    print(groups)
    def query_to_result(query_result):
        return{
            "id": query_result.id,
            "name": query_result.name,
            "code": query_result.code
        }
    result = list(map(query_to_result, groups))
    return {
        "groups": result
    }


@router.get("/api/groups/{group_id}")
async def get_group(group_id: int, token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None),  db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError

    group = db.get(Group, group_id)

    if(group is None):
        return resourceNouFoundError("group")

    return group.toResultJSON()
    
class CreateGroupSchema(BaseModel):
    name: str

@router.post("/api/groups")
async def create_group(data: CreateGroupSchema, token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None),  db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError
    group =  Group(id = idgen(), name=data.name, code = idgen())
    join = Join(user_id = user.id, group_id = group.id)
    db.add(group)
    db.add(join)
    db.flush()
    return group.toResultJSON()

class JoinSchema(BaseModel):
    code: str

@router.post("/api/join")
async def join(data: JoinSchema, token: Union[str, None] = Cookie(None), id: Union[str, None] = Cookie(None),  db: Session = Depends(get_db)):
    user = get_user(token, id, db)
    if(user is None):
        return forbiddenError
    group = db.query(Group).filter(Group.code == data.code).first()

    if(group is None):
        return resourceNouFoundError("group")

    join = Join(user_id = user.id, group_id = group.id)

    db.add(join)
    db.commit()
    db.flush()
    