from fastapi import APIRouter, status, HTTPException
from fastapi import Depends, status, HTTPException
from blog import schemas, models, database
from sqlalchemy.orm import Session
from typing import List
from blog.repository import authentication


router = APIRouter(
    prefix="/login",
    tags=['Authentication'])
get_db = database.get_db


@router.post('/',  status_code= status.HTTP_201_CREATED)
def login_session(request:schemas.Login, db: Session = Depends(get_db)):
    return authentication.login(request, db)