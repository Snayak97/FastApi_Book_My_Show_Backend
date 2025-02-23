import uuid

from pydantic import BaseModel
from datetime import datetime,date

from typing import List,Optional


class CinemaHall(BaseModel):
    cinema_hall_id: uuid.UUID   
    cinema_hall_name :str
    total_seats : int
    created_at : datetime
    update_at : datetime
    # class Config():
    #     from_attributes =True

class cinemaHallCreateModel(BaseModel):
    cinema_hall_name :str
    total_seats : int
    # class Config():
    #     from_attributes =True

class cinemaHallUpdateModel(cinemaHallCreateModel):
   pass
 