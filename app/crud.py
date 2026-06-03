from sqlalchemy.orm import Session
from . import models, schemas

def get_items(db: Session):
    return db.query(models.ItemDB).all()

def get_item(db: Session, item_id: int):
    return db.query(models.ItemDB).filter(models.ItemDB.id == item_id).first()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.ItemDB(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item_data: schemas.ItemUpdate):
    item = get_item(db, item_id)
    if not item:
        return None

    if item_data.name is not None:
        item.name = item_data.name
    if item_data.price is not None:
        item.price = item_data.price

    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item_id: int):
    item = get_item(db, item_id)
    if not item:
        return None

    db.delete(item)
    db.commit()
    return item
