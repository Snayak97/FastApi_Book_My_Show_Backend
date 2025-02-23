import uuid

from pydantic import BaseModel
from datetime import datetime,date

from typing import List,Optional
from src.models.bookingModel import BookingStatus


class Booking(BaseModel):
    booking_id: uuid.UUID   
    number_of_seats :int
    status : BookingStatus
    created_at : datetime
    update_at : datetime
    # class Config():
    #     from_attributes =True

class bookingCreateModel(BaseModel):
    number_of_seats :int
    status : BookingStatus
    # class Config():
    #     from_attributes =True

class bookingUpdateModel(bookingCreateModel):
    pass
