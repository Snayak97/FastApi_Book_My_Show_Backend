from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
import uuid
from src.db.dbConnect import get_db
from typing import Optional,List
# from sqlalchemy.ext.asyncio import AsyncSession
from src.models.showModel import Show

from src.services.seatManagementService import seat_management_service
from src.schemas.seatSchema import CinemaSeatSchema,ShowSeatSchema,BookSeatsRequest
from src.auth.dependency import AccessTokenBearer


seat_router=APIRouter(
    prefix="/api/v1/seat",
    tags=["seat"],
)




@seat_router.post("/cinema-halls/{hall_id}/initialize")
async def initialize_hall_seats(hall_id:str, db: Session = Depends(get_db)):
    """Initialize cinema hall with seats"""
    seat_management_service.create_cinema_hall_seats(db, hall_id)
    return {"message": "Seats initialized successfully"}


@seat_router.post("/shows/{show_id}/seats")
async def create_show_seats(show_id: str, db: Session = Depends(get_db)):
    """Create seats for a show with pricing"""
      # Fetch the associated hall_id from the Show table
    show = db.query(Show).filter(Show.show_id == show_id).first()

    if not show:
        return {"error": "Show not found"}

    hall_id = show.cinema_hall_id
    seat_management_service.create_show_seats(db, show_id, hall_id)
    return {"message": "Show seats initialized successfully"}

@seat_router.get("/shows/{show_id}/available-seats", response_model=List[ShowSeatSchema])
async def get_available_seats(show_id: str, db: Session = Depends(get_db)):
    """Get available seats for a show"""
    seats = await seat_management_service.get_available_seats(db, show_id)
    # return seat_management_service.get_available_seats(db, show_id)
    return seats


@seat_router.post("/shows/{show_id}/book-seats")
async def book_seats(show_id: str, request:BookSeatsRequest, db: Session = Depends(get_db)):
    """Book selected seats for a show"""
    return await seat_management_service.book_seats(db,show_id, request.seat_ids, request.booking_id)

@seat_router.post("/bookings/{booking_id}/cancel")
async def cancel_booking(booking_id: str, db: Session = Depends(get_db)):
    """Cancel a booking and release seats"""
    return await seat_management_service.cancel_booking(db, booking_id)