from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean
from sqlalchemy.orm import relationship

from typing import List,Optional
import uuid
from datetime import datetime,date

import sqlalchemy.dialects.postgresql as pg

from src.db.dbConnect import Base

class CinemaHall(Base):
    __tablename__ = "cinema_halls"
    cinema_hall_id : uuid.UUID = Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4,index=True)
    cinema_hall_name= Column(String, nullable=False)
    total_seats = Column(Integer, nullable=False)
    created_at:datetime = Column(pg.TIMESTAMP, default=datetime.utcnow, nullable=False)
    update_at:datetime = Column(pg.TIMESTAMP,default=datetime.utcnow,onupdate=datetime.utcnow, nullable=False)
    
    shows = relationship("Show", back_populates="cinema_hall")
    cinema_seats = relationship("CinemaSeat", back_populates="cinema_hall")