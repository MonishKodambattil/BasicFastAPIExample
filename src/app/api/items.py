from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.app.schemas import item as item_schemas
from src.app.db.repository.item_repository import ItemRepository
from src.app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items/", response_model=list[item_schemas.Item])
def list_items(db: Session = Depends(get_db)):
    item_repo = ItemRepository()
    return item_repo.get_users(db)


@router.post("/items/", response_model=item_schemas.Item)
def create_item(item: item_schemas.ItemCreate, db: Session = Depends(get_db)):
    item_repo = ItemRepository()
    new_item = item_repo.create_item(db, Item(title=item.title, description=item.description, owner_id=1))
    return new_item