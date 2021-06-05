from fastapi import Depends, status, HTTPException
from blog import schemas, models, database
from sqlalchemy.orm import Session


get_db = database.get_db

def get(db: Session = Depends(get_db)):
    all_blogs = db.query(models.Blog).all()
    return all_blogs


def create(request:schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body = request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return f'The blog with id {id} is deleted'

def update(id, request:schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    blog.update(vars(request))
    db.commit()
    return f'The blog with id {id} is updated'


def getbyid(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with id {id} is not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    return blog