import uuid

from pydantic import BaseModel
from datetime import datetime,date

from typing import List,Optional


class Movie(BaseModel):
    uid: uuid.UUID   
    title : str
    description :str
    genre : str
    language : str
    duration_minutes : int
    release_date  : date
    country : str
    created_at : datetime
    update_at : datetime
    # class Config():
    #     from_attributes =True

class movieCreateModel(BaseModel):
    title : str
    description :str
    genre : str
    language : str
    duration_minutes : int
    release_date  : date
    country : str
    # class Config():
    #     from_attributes =True

class movieUpdateModel(BaseModel):
    title : str
    description :str
    genre : str
    language : str
    duration_minutes : int
    release_date  : date
    country : str

