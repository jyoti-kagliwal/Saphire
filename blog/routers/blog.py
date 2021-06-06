from fastapi import APIRouter, status, HTTPException
from fastapi import Depends, status, HTTPException
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from blog.repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs'])
get_db = database.get_db



@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.get('/', response_model=List[schemas.ShowBlog])
def get(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get(db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db: Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def getbyid(id, db: Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.getbyid(id, db)