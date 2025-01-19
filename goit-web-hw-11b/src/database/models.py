# Ім'я
# Прізвище
# Електронна адреса
# Номер телефону
# День народження
# Додаткові дані (необов'язково)


from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts3"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birthday = Column(DateTime, nullable=False)
    comments = Column(String(150), nullable=False)     
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=True)

