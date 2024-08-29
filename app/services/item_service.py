from sqlalchemy.orm import Session
from app.db.repository.item_repository import ItemRepository


class ItemService:

    def __init__(self, db: Session):
        self.item_repository = ItemRepository(db)

    def create_item(self, name: str, description: str):
        return self.item_repository.create_item(name, description)

    def get_item(self, item_id: int):
        return self.item_repository.get_item(item_id)

    def get_items(self):
        return self.item_repository.get_items()

    def update_item(self, item_id: int, name: str, description: str):
        return self.item_repository.update_item(item_id, name, description)

    def delete_item(self, item_id: int):
        return self.item_repository.delete_item(item_id)
