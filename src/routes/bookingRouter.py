from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session

from src.db.dbConnect import get_db
from typing import Optional,List
# from sqlalchemy.ext.asyncio import AsyncSession

from src.services.bookingService import booking_service
from src.schemas.bookingSchema import bookingCreateModel,bookingUpdateModel,Booking
from src.auth.dependency import AccessTokenBearer


booking_router=APIRouter(
    prefix="/api/v1/booking",
    tags=["Booking"],
)

# create booking
@booking_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_booking(booking_data:bookingCreateModel,db:Session=Depends(get_db)):
    return await booking_service.create_a_bookings(booking_data,db)


# get all bookings
@booking_router.get("/",status_code=status.HTTP_200_OK)
async def get_bookings(db:Session=Depends(get_db)):
    return await booking_service.get_all_bookings(db)

# get a booking
@booking_router.get("/{booking_id}",response_model=Booking, status_code=status.HTTP_200_OK)
async def get_booking(booking_id:str,db:Session=Depends(get_db)):
    return await booking_service.get_a_booking(booking_id,db)

@booking_router.patch("/{booking_id}",response_model=Booking, status_code=status.HTTP_202_ACCEPTED)
async def update_booking(booking_id:str,update_booking_data:bookingUpdateModel,db:Session=Depends(get_db)):
    return await booking_service.update_booking(booking_id,update_booking_data,db)

# delete show
@booking_router.delete("/{booking_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_booking(booking_id:str,db:Session=Depends(get_db)):
    return await booking_service.delete_a_booking(booking_id,db)
