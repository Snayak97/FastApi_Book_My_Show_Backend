
from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import Session
from datetime import datetime
from src.models.bookingModel import Booking

from sqlalchemy.future import select
from sqlalchemy import desc


import uuid

from src.schemas.bookingSchema import bookingCreateModel,bookingUpdateModel

class BookingService:
    async def get_all_bookings(self,db:AsyncSession):
        # Anotheraproch by asending
        # books=db.query(Book).all()

        #using desending
        statement = select(Booking).order_by(desc(Booking.created_at))
        # Execute the statement and await the result
        result =db.execute(statement)
        # Extract the list of books
        bookings = result.scalars().all()
        return bookings
    
    async def get_a_booking(self,booking_id,db:AsyncSession):
        try:
        # Ensure the book_uid is a UUID object
            booking_id = uuid.UUID(booking_id)
        except ValueError:
            return f"Invalid UUID format: {booking_id}"
       
        booking= db.query(Booking).filter(Booking.booking_id==booking_id).first()
        return booking

    async def create_a_bookings(self,bookings_data,db:AsyncSession):
        bookings_data_dict = bookings_data.model_dump()
        new_bookings = Booking(**bookings_data_dict)
        print(new_bookings)
        db.add(new_bookings)
        db.commit()
        db.refresh(new_bookings)
        return new_bookings
    
    
    async def update_booking(self,booking_id,update_booking_data:bookingUpdateModel,db:AsyncSession):
        booking_to_update = db.query(Booking).filter(Booking.booking_id == booking_id).first()
        if booking_to_update is not None:
            booking_data_dict = update_booking_data.model_dump()
            for key,val in booking_data_dict.items():
                setattr(booking_to_update,key,val)
            db.commit()
            return booking_to_update
        else:
            return None
        
    async def delete_a_booking(self,booking_id,db:AsyncSession):
        booking_to_delete= db.query(Booking).filter(Booking.booking_id == booking_id).first()
        if booking_to_delete is not None:
            db.delete(booking_to_delete)
            db.commit()
            return "Booking deleted"
        else:
            return None

booking_service = BookingService()
    