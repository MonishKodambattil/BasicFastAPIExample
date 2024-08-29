from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.item_service import ItemService
from app.db.session import get_db

router = APIRouter()


@router.post("/items/", tags=["Item"])
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    item_service = ItemService(db)
    return item_service.create_item(name, description)

@router.get("/items/{item_id}", tags=["Item"])
def read_item(item_id: int, db: Session = Depends(get_db)):
    item_service = ItemService(db)
    item = item_service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/items/", tags=["Item"])
def read_items(db: Session = Depends(get_db)):
    item_service = ItemService(db)
    return item_service.get_items()

@router.put("/items/{item_id}", tags=["Item"])
def update_item(item_id: int, name: str, description: str, db: Session = Depends(get_db)):
    item_service = ItemService(db)
    updated_item = item_service.update_item(item_id, name, description)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/items/{item_id}", tags=["Item"])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item_service = ItemService(db)
    if not item_service.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
