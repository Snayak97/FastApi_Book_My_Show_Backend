from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean
from sqlalchemy.orm import relationship

from typing import List,Optional
import uuid
from datetime import datetime,date

import sqlalchemy.dialects.postgresql as pg

from src.db.dbConnect import Base

class Show(Base):
    __tablename__="shows"
    show_id: uuid.UUID = Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4,index=True)
    show_date = Column(DateTime, nullable=False, default = datetime.utcnow)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    movie_id: Optional[uuid.UUID] = Column(pg.UUID(as_uuid=True), ForeignKey("movies.uid"),nullable=True)
    cinema_hall_id : Optional[uuid.UUID] = Column(pg.UUID(as_uuid=True), ForeignKey("cinema_halls.cinema_hall_id"),nullable=True)
    created_at:datetime=Column(pg.TIMESTAMP, default=datetime.utcnow, nullable=False)
    update_at:datetime=Column(pg.TIMESTAMP,default=datetime.utcnow,onupdate=datetime.utcnow, nullable=False)


    movie = relationship("Movie", back_populates="shows")
    cinema_hall = relationship("CinemaHall", back_populates="shows")
    bookings = relationship("Booking", back_populates="show")
    show_seats = relationship("ShowSeat", back_populates="show")