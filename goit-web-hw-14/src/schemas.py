# from datetime import datetime
# from typing import List, Optional
# from pydantic import BaseModel, Field


from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr

class ContactBase(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    email: str
    phone_number: str
    birthday: date
    comments: str
    """AI is creating summary for ContactBase
    """



class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True

class ContactUpdate(ContactBase):
    pass
...


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)
    """Create a model for a user model .
    """

class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str
    """Create a database class for the database .
    """
    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"
    """Create a response string for the user .
    """

class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    """Generate a token for use in a token .
    """
class RequestEmail(BaseModel):
    email: EmailStr

    """This method is used to create a new one .
    """
# class TagResponse(TagModel):
#     id: int

#     class Config:
#         orm_mode = True


# class NoteBase(BaseModel):
#     title: str = Field(max_length=50)
#     description: str = Field(max_length=150)


# class NoteModel(NoteBase):
#     tags: List[int]


# class NoteUpdate(NoteModel):
#     done: bool


# class NoteStatusUpdate(BaseModel):
#     done: bool


# class NoteResponse(NoteBase):
#     id: int
#     created_at: datetime
#     tags: List[TagResponse]

#     class Config:
#         orm_mode = True
