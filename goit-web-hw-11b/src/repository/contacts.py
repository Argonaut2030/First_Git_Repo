from typing import List

from sqlalchemy.orm import Session, subqueryload

from src.database.models import Contact , User # Assuming this is your contact model
from src.schemas import ContactBase, ContactUpdate, ContactResponse

from datetime import date, timedelta
from sqlalchemy import extract



async def get_birthdays_in_next_week(db: Session):
    today = date.today()
    next_week = today + timedelta(days=7)

    today_month = extract('month', today)
    today_day = extract('day', today)

    birthdays_this_week = []

    for i in range(7): 
        check_date = today + timedelta(days=i) 
        check_month = extract('month', check_date)
        check_day = extract('day', check_date)

        contacts = db.query(Contact).filter(
            extract('month', Contact.birthday) == check_month,
            extract('day', Contact.birthday) == check_day
        ).all()
        birthdays_this_week.extend(contacts)

    return birthdays_this_week

async def get_contacts(skip: int, limit: int, db: Session, user:User) -> List[Contact]:
    """
    Retrieves all contacts with optional pagination.
    """
    return db.query(Contact).filter_by(user=user).offset(skip).limit(limit).all()


async def get_contact(id: int, db: Session, user:User) -> Contact | None:
    """
    Retrieves a single contact by its ID.
    """
    return db.query(Contact).filter(Contact.id == id, Contact.user_id == user.id).first()



# async def create_todo(body: TodoSchema, db: AsyncSession, user: User):
#     todo = Todo(**body.model_dump(exclude_unset=True), user=user)  # (title=body.title, description=body.description)
#     db.add(todo)
#     await db.commit()
#     await db.refresh(todo)
#     return todo

async def create_contact(body: ContactBase, db: Session, user: User) -> Contact:
    """
    Creates a new contact.
    """
    contact = Contact(
                    first_name=body.first_name, 
                    last_name=body.last_name,
                    birthday=body.birthday,
                    comments=body.comments,   
                    email=body.email,
                    phone_number =body.phone_number,
                    user=user
                     )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(id: int, body: ContactUpdate, db: Session, user:User) -> Contact | None:
    """
    Updates an existing contact.
    """
    contact = await get_contact(id, db, user)
    if contact:
        for key, value in body.dict().items():
            setattr(contact, key, value)
        db.commit()
    return contact


async def remove_contact(id: int, db: Session, user:User) -> Contact | None:
    """
    Deletes a contact.
    """
    contact = await get_contact(id, db, user)
    if contact:
        db.delete(contact)
        db.commit()
    return contact



async def search_contacts(query: str, db: Session, user:User):
    contacts = db.query(Contact).filter(
            Contact.user_id == user.id,
            Contact.first_name.ilike(f"%{query}%")| 
            Contact.last_name.ilike(f"%{query}%")|
            Contact.email.ilike(f"%{query}%")
        
    ).all()
    return contacts



