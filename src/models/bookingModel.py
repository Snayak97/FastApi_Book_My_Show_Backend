from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean,Enum
from typing import List,Optional
import uuid
from datetime import datetime,date
import enum

import sqlalchemy.dialects.postgresql as pg

from src.db.dbConnect import Base

class BookingStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


class Booking(Base):
    __tablename__ = "bookings"
    booking_id : uuid.UUID = Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4,index=True)
    number_of_seats = Column(Integer, nullable=False)
    status = Column(Enum(BookingStatus), default=BookingStatus.PENDING)
    user_id: Optional[uuid.UUID] = Column(pg.UUID(as_uuid=True), ForeignKey("users.uid"),nullable=True)
    show_id: Optional[uuid.UUID] = Column(pg.UUID(as_uuid=True), ForeignKey("shows.show_id"),nullable=True)
    created_at:datetime = Column(pg.TIMESTAMP, default=datetime.utcnow, nullable=False)
    update_at:datetime = Column(pg.TIMESTAMP,default=datetime.utcnow,onupdate=datetime.utcnow, nullable=False)
    
    user = relationship("User", back_populates="bookings")
    show = relationship("Show", back_populates="bookings")
    show_seats = relationship("ShowSeat", back_populates="booking")


