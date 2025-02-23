from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean
from sqlalchemy.orm import relationship

from typing import List,Optional
import uuid
from datetime import datetime,date

import sqlalchemy.dialects.postgresql as pg

from src.db.dbConnect import Base


class User(Base):
    __tablename__="users"
    uid: uuid.UUID = Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password_hash:str=Column(String, nullable= False)
    role : str = Column(pg.VARCHAR, nullable=False, server_default="user")
    created_at:datetime=Column(pg.TIMESTAMP, default=datetime.utcnow, nullable=False)
    update_at:datetime=Column(pg.TIMESTAMP,default=datetime.utcnow,onupdate=datetime.utcnow, nullable=False)

    bookings = relationship("Booking", back_populates="user")


