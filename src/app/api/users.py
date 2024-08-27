from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.app.schemas import user as user_schemas
from src.app.db.repository.user_repository import UserRepository
from src.app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/", response_model=list[user_schemas.User])
def list_items(db: Session = Depends(get_db)):
    repo = UserRepository()
    return repo.get_users(db)


@router.post("/users/", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    user_repo = UserRepository()
    db_user = user_repo.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = user.password + "notreallyhashed"
    new_user = user_repo.create_user(db, User(email=user.email, hashed_password=hashed_password))
    return new_user