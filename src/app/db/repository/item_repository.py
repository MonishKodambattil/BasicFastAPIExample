from sqlalchemy.orm import Session
from src.app.db.models.item import Item

class ItemRepository:

    def get_items(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Item).offset(skip).limit(limit).all()

    def create_item(self, db: Session, item: Item):
        db.add(item)
        db.commit()
        db.refresh(item)
        return item