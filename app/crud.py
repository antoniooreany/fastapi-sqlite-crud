from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas

# Data Access Layer (Repository Pattern)

def get_all(db: Session) -> List[models.ItemDB]:
    return db.query(models.ItemDB).all()

def get_by_id(db: Session, item_id: int) -> Optional[models.ItemDB]:
    return db.query(models.ItemDB).filter(models.ItemDB.id == item_id).first()

def create(db: Session, item_create: schemas.ItemCreate) -> models.ItemDB:
    db_item = models.ItemDB(name=item_create.name, price=item_create.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update(db: Session, item: models.ItemDB, item_update: schemas.ItemUpdate) -> models.ItemDB:
    if item_update.name is not None:
        item.name = item_update.name
    if item_update.price is not None:
        item.price = item_update.price

    db.commit()
    db.refresh(item)
    return item

def delete(db: Session, item: models.ItemDB) -> models.ItemDB:
    db.delete(item)
    db.commit()
    return item

# Users
def get_user_by_username(db: Session, username: str) -> Optional[models.UserDB]:
    return db.query(models.UserDB).filter(models.UserDB.username == username).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str) -> models.UserDB:
    db_user = models.UserDB(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
