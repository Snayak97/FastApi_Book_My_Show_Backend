from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean,Enum,Float
from typing import List,Optional
import uuid
from datetime import datetime,date
import enum

import sqlalchemy.dialects.postgresql as pg

from src.db.dbConnect import Base

class SeatCategory(str, enum.Enum):
    VIP = "vip"
    PREMIUM = "premium"
    REGULAR = "regular"

class SeatStatus(str, enum.Enum):
    AVAILABLE = "available"
    BOOKED = "booked"
    RESERVED = "reserved"


class CinemaSeat(Base):
    __tablename__ = "cinema_seats"

    seat_id : uuid.UUID = Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4,index=True)
    row_number = Column(String, nullable=False)  
    seat_number = Column(Integer,nullable=False)   
    category = Column(Enum(SeatCategory),default=SeatCategory.REGULAR )
    cinema_hall_id:Optional[uuid.UUID] = Column(pg.UUID(as_uuid=True), ForeignKey("cinema_halls.cinema_hall_id"),nullable=True)
    created_at:datetime = Column(pg.TIMESTAMP, default=datetime.utcnow, nullable=False)
    update_at:datetime = Column(pg.TIMESTAMP,default=datetime.utcnow,onupdate=datetime.utcnow, nullable=False)

    cinema_hall = relationship("CinemaHall", back_populates="cinema_seats")
    show_seats = relationship("ShowSeat", back_populates="cinema_seat")

class ShowSeat(Base):
    __tablename__ = "show_seats"
    
    show_seat_id :uuid.UUID = Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4,index=True)
    show_id :Optional[uuid.UUID] = Column(pg.UUID(as_uuid=True), ForeignKey("shows.show_id"),nullable=True)
    seat_id : Optional[uuid.UUID] = Column(pg.UUID(as_uuid=True), ForeignKey("cinema_seats.seat_id"),nullable=True)
    Status = Column(Enum(SeatStatus), default=SeatStatus.AVAILABLE)
    Price = Column(Float)
    booking_id : Optional[uuid.UUID] = Column(pg.UUID(as_uuid=True), ForeignKey("bookings.booking_id"),nullable=True)
    created_at:datetime = Column(pg.TIMESTAMP, default=datetime.utcnow, nullable=False)
    update_at:datetime = Column(pg.TIMESTAMP,default=datetime.utcnow,onupdate=datetime.utcnow, nullable=False)

    show = relationship("Show", back_populates="show_seats")
    cinema_seat = relationship("CinemaSeat", back_populates="show_seats")
    booking = relationship("Booking", back_populates="show_seats")                                                                                     