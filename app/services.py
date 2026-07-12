from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List, Optional
from . import crud, schemas, models
from passlib.context import CryptContext

# Use a simpler hashing scheme if bcrypt is problematic in tests
# or ensure the password is VERY short.
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

# Item Services

def get_all_items(db: Session) -> List[models.ItemDB]:
    return crud.get_all(db)

def get_item_by_id(db: Session, item_id: int) -> models.ItemDB:
    item = crud.get_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

def create_new_item(db: Session, item_create: schemas.ItemCreate) -> models.ItemDB:
    # Business rule: Price must be positive
    if item_create.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be positive")
    return crud.create(db, item_create)

def update_item_service(db: Session, item_id: int, item_update: schemas.ItemUpdate) -> models.ItemDB:
    item = crud.get_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if item_update.price is not None and item_update.price < 0:
        raise HTTPException(status_code=400, detail="Price must be positive")
        
    return crud.update(db, item, item_update)

def delete_item_service(db: Session, item_id: int) -> models.ItemDB:
    item = crud.get_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.delete(db, item)

# Auth Services
def authenticate_user(db: Session, username: str, password: str) -> Optional[models.UserDB]:
    user = crud.get_user_by_username(db, username)
    # The traceback indicates the issue is inside bcrypt, potentially related to the internal 
    # mock hashes in passlib. Let's try passing the password as bytes and ensure it's short.
    # Also, ensure we aren't passing a super long string which might be what bcrypt complains about.
    # The error message says 'secret = b'0123...'' which is VERY long. This is NOT coming from our 'password' variable.
    # It looks like passlib's bcrypt backend is trying to verify against a very long bug_hash internally.
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user

def register_user(db: Session, user_create: schemas.UserCreate) -> models.UserDB:
    if crud.get_user_by_username(db, user_create.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Hash the password
    hashed_password = pwd_context.hash(user_create.password)
    return crud.create_user(db, user_create, hashed_password)
