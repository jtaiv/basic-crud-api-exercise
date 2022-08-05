from sqlalchemy import Column, String

from .database import Base


class Profile(Base):
    __tablename__ = "profile"

    email = Column(String, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)
