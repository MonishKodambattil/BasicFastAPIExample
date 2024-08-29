from sqlalchemy.orm import Session
from app.db.dao.item_dao import ItemDAO
from app.db.models.item import Item

class ItemRepository:

    def __init__(self, db: Session):
        self.dao = ItemDAO(db)

    def create_item(self, name: str, description: str):
        item = Item(name=name, description=description)
        return self.dao.add(item)

    def get_item(self, item_id: int):
        return self.dao.get(item_id)

    def get_items(self):
        return self.dao.get_all()

    def update_item(self, item_id: int, name: str, description: str):
        if item := self.dao.get(item_id):
            item.name = name
            item.description = description
            return self.dao.update(item)
        return None

    def delete_item(self, item_id: int):
        if item := self.dao.get(item_id):
            self.dao.delete(item)
            return True
        return False
