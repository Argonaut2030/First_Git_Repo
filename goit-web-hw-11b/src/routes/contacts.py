from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session

from src.services.auth import auth_service
from src.database.db import get_db
from src.database.models import Contact, User  # Assuming this is the model for contacts
from src.schemas import ContactBase, ContactUpdate, ContactResponse  # Assuming these are the schemas for contacts
from src.repository import contacts as repository_contacts  # Assuming this is the repository for contacts

router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get("/birthdays_next_week/", response_model=list[ContactResponse])
async def read_birthdays_next_week(db: Session = Depends(get_db)):
    birthdays = await repository_contacts.get_birthdays_in_next_week(db)
    return birthdays

@router.get("/search", response_model=list[ContactResponse])
async def search_contacts(query: str, db: Session = Depends(get_db),
                          user: User = Depends(auth_service.get_current_user)):
    """
    Search for contacts by name, surname, or email.
    """
    contacts = await repository_contacts.search_contacts(query, db, user) 
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No contacts found.")
    return contacts

@router.get("/", response_model=List[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    """
    Get all contacts.
    """
    contacts = await repository_contacts.get_contacts(skip, limit, db, user)
    return contacts


@router.get("/{id}", response_model=ContactResponse)
async def read_contact_id(id: int, db: Session = Depends(get_db),
                          user: User = Depends(auth_service.get_current_user)):
    """
    Get a single contact by id.
    """
    contact = await repository_contacts.get_contact(id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact



@router.post("/", response_model=ContactBase)
async def create_contact(body: ContactBase, db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    """
    Create a new contact.
    """
    contact = await repository_contacts.create_contact(body, db, user)
    return contact


@router.put("/{id}", response_model=ContactResponse)
async def update_contact(body: ContactUpdate, id: int, db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    """
    Update a contact.
    """
    contact = await repository_contacts.update_contact(id, body, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.delete("/{id}", response_model=ContactResponse)
async def remove_contact(id: int, db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    """
    Delete a contact.
    """
    contact = await repository_contacts.remove_contact(id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

# @router.get("/{first_name}", response_model=ContactResponse)
# async def read_contact_fname(first_name: str, db: Session = Depends(get_db),
#                              user: User = Depends(auth_service.get_current_user)):
#     """
#     Get a single contact by first name.
#     """
#     contact = await repository_contacts.get_contact_fname(first_name, db, user)
#     if contact is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
#     return contact
