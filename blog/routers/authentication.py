from fastapi import APIRouter, status, Depends
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from blog.repository import authentication
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/login",
    tags=['Authentication'])
get_db = database.get_db


@router.post('/',  status_code= status.HTTP_201_CREATED)
def login_session(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return authentication.login(request, db)