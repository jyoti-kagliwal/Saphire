from fastapi import APIRouter, status, Depends
from blog import schemas, oauth2, database
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users'])
get_db = database.get_db

@router.post('/', status_code= status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request:schemas.User, db: Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.create_user(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def getbyid(id, db: Session = Depends(get_db) , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.getbyid(id, db)