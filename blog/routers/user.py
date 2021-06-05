from fastapi import APIRouter, status, HTTPException
from fastapi import Depends, status, HTTPException
from starlette.routing import request_response
from blog import schemas, models, database
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users'])
get_db = database.get_db

@router.post('/', status_code= status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def getbyid(id, db: Session = Depends(get_db)):
    return user.getbyid(id, db)