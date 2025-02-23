import uuid

from pydantic import BaseModel
from datetime import datetime,date

from typing import List,Optional
from src.models.seatModel import SeatStatus,SeatCategory


class CinemaSeatSchema(BaseModel):
    seat_id: uuid.UUID   
    row_number :str
    seat_number : int
    category : SeatCategory
    cinema_hall_id : uuid.UUID 
    created_at : datetime
    update_at : datetime
    # class Config():
    #     from_attributes =True

class ShowSeatSchema(BaseModel):
    show_seat_id :uuid.UUID 
    show_id : uuid.UUID 
    seat_id : uuid.UUID 
    Status : SeatStatus
    Price: float
    booking_id : uuid.UUID 
    # class Config():
    #     from_attributes =True
class BookSeatsRequest(BaseModel):
    seat_ids: List[uuid.UUID]
    booking_id : uuid.UUID