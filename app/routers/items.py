import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud, auth, models

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(auth.get_current_user)]
)


@router.get("/", response_model=list[schemas.ItemResponse])
def list_items(db: Session = Depends(get_db)):
    logger.info("Listing all items")
    return crud.get_items(db)


@router.get("/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    logger.info(f"Getting item with id: {item_id}")
    item = crud.get_item(db, item_id)
    if not item:
        logger.warning(f"Item not found: {item_id}")
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=schemas.ItemResponse, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating item: {item.name}")
    return crud.create_item(db, item)


@router.patch("/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    logger.info(f"Updating item with id: {item_id}")
    updated = crud.update_item(db, item_id, item)
    if not updated:
        logger.warning(f"Item not found for update: {item_id}")
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting item with id: {item_id}")
    deleted = crud.delete_item(db, item_id)
    if not deleted:
        logger.warning(f"Item not found for deletion: {item_id}")
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
