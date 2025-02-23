from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter,Depends,status,Response,HTTPException
# from sqlalchemy.orm import Session
from datetime import datetime
from src.models.seatModel import CinemaSeat,ShowSeat,SeatStatus

from sqlalchemy.future import select
from sqlalchemy import desc
from typing import List,Optional
import uuid

from src.schemas.seatSchema import CinemaSeatSchema,ShowSeatSchema

class SeatManagementService:

    @staticmethod
    async def create_cinema_hall_seats(db: AsyncSession, hall_id: str):
        """Create seats for a cinema hall"""
        seat_layout = {
            "VIP": {"rows": ["A", "B"], "seats_per_row": 10},
            "PREMIUM": {"rows": ["C", "D", "E"], "seats_per_row": 10},
            "REGULAR": {"rows": ["F", "G", "H", "I", "J"], "seats_per_row": 10}
        }
        
        for category, layout in seat_layout.items():
            for row in layout["rows"]:
                for seat_num in range(1, layout["seats_per_row"] + 1):
                    seat = CinemaSeat(
                        row_number=row,
                        seat_number=str(seat_num),
                        category=category,
                        cinema_hall_id=hall_id
                    )
                    db.add(seat)
        await db.flush()
        await db.commit()
    
    @staticmethod
    async def create_show_seats(db: AsyncSession, show_id: str, hall_id: str):
        """Create seats for a show with predefined prices"""
        show_seats = []
        cinema_seats = db.query(CinemaSeat).filter(CinemaSeat.cinema_hall_id == hall_id).all()
        
        base_prices = {"VIP": 300.0, "PREMIUM": 200.0, "REGULAR": 100.0}
        
        for seat in cinema_seats:
            show_seat = ShowSeat(
                show_id=show_id,
                seat_id=seat.seat_id,
                Status=SeatStatus.AVAILABLE,
                Price=base_prices[seat.category]
            )
            db.add(show_seat)
            show_seats.append(show_seat)
        
        db.commit()
        return show_seats
    
    @staticmethod
    async def get_available_seats(db: AsyncSession, show_id: str):
        """Retrieve available seats for a show"""
        return db.query(ShowSeat).filter(
            ShowSeat.show_id == show_id,
            ShowSeat.Status == SeatStatus.AVAILABLE
        ).all()
    
    @staticmethod
    async def book_seats(db: AsyncSession, show_id: str, seat_ids:List, booking_id:str):
        """Book selected seats for a show"""
        seats = db.query(ShowSeat).filter(
            ShowSeat.show_id == show_id,
            ShowSeat.show_seat_id.in_(seat_ids),
            ShowSeat.Status == SeatStatus.AVAILABLE
        ).all()
        
        if len(seats) != len(seat_ids):
            raise HTTPException(status_code=400, detail="Some seats are not available")
        
        for seat in seats:
            seat.Status = SeatStatus.BOOKED
            seat.booking_id = booking_id
        
        db.commit()
        return {"detail": "Seats booked successfully"}
    
    @staticmethod
    async def cancel_booking(db: AsyncSession, booking_id: str):
        """Cancel a booking and release seats"""
        seats = db.query(ShowSeat).filter(ShowSeat.booking_id== booking_id).all()
        
        if not seats:
            raise HTTPException(status_code=404, detail="Booking not found")
        
        for seat in seats:
            seat.Status = SeatStatus.AVAILABLE
            seat.booking_id = None
        
        await db.commit()
        return {"message": "Booking cancelled successfully"}





seat_management_service = SeatManagementService()