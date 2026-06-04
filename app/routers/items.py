import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, auth, services

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(auth.get_current_user)]
)


@router.get("/", response_model=list[schemas.ItemResponse])
def list_items(db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    logger.info(f"User {current_user.username} is listing all items")
    return services.get_all_items(db)


@router.get("/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    logger.info(f"User {current_user.username} is getting item with id: {item_id}")
    return services.get_item_by_id(db, item_id)


@router.post("/", response_model=schemas.ItemResponse, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    logger.info(f"User {current_user.username} is creating item: {item.name}")
    return services.create_new_item(db, item)


@router.patch("/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    logger.info(f"User {current_user.username} is updating item with id: {item_id}")
    return services.update_item_service(db, item_id, item)


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    logger.info(f"User {current_user.username} is deleting item with id: {item_id}")
    return services.delete_item_service(db, item_id)
