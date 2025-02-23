from pydantic import BaseModel, constr
import uuid
from datetime import datetime,date

from typing import List,Optional

class CreateUserModel(BaseModel):
    username: constr(max_length=20)     # String with max length of 8
    email: constr(max_length=40)       # String with max length of 40
    password_hash: constr(min_length=6)



class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    password_hash: str 
    created_at: datetime
    update_at: datetime

class UserLoginModel(BaseModel):
    email: str = constr(max_length=40)
    password: str = constr(min_length=6)