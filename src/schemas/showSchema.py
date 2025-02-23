import uuid

from pydantic import BaseModel
from datetime import datetime,date

from typing import List,Optional


class Show(BaseModel):
    show_id: uuid.UUID   
    show_date :datetime
    start_time : datetime
    end_time : datetime
    created_at : datetime
    update_at : datetime
    # class Config():
    #     from_attributes =True

class showCreateModel(BaseModel):
    show_date :datetime
    start_time : datetime
    end_time : datetime
    # class Config():
    #     from_attributes =True

class showUpdateModel(BaseModel):
    show_date :datetime
    start_time : datetime
    end_time : datetime
