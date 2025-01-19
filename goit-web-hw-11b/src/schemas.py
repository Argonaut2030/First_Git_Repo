# from datetime import datetime
# from typing import List, Optional
# from pydantic import BaseModel, Field


from datetime import date
from pydantic import BaseModel, Field

class ContactBase(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    email: str
    phone_number: str
    birthday: date
    comments: str
   





class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True

class ContactUpdate(ContactBase):
    pass

 

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
