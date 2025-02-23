
from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import Session
from datetime import datetime
from src.models import CinemaHall

from sqlalchemy.future import select
from sqlalchemy import desc

import uuid

from src.schemas.cinemaHallModelSchema import cinemaHallCreateModel,cinemaHallUpdateModel

class CinemaHallService:
    async def get_all_cinema_hall(self,db:AsyncSession):
        # Anotheraproch by asending
        # books=db.query(Book).all()

        #using desending
        statement = select(CinemaHall).order_by(desc(CinemaHall.created_at))
        # Execute the statement and await the result
        result =db.execute(statement)
        # Extract the list of books
        cinema_halls = result.scalars().all()
        return cinema_halls
    
    async def get_a_cinema_hall(self,cinema_hall_id,db:AsyncSession):
        try:
        # Ensure the book_uid is a UUID object
            cinema_hall_id = uuid.UUID(cinema_hall_id)
        except ValueError:
            return f"Invalid UUID format: {cinema_hall_id}"
       
        cinema_hall= db.query(CinemaHall).filter(CinemaHall.cinema_hall_id==cinema_hall_id).first()
        return cinema_hall

    async def create_a_cinema_hall(self,cinema_hall_data,db:AsyncSession):
        cinema_hall_data_dict = cinema_hall_data.model_dump()
        new_cinema_hall = CinemaHall(**cinema_hall_data_dict)
        print(new_cinema_hall)
        db.add(new_cinema_hall)
        db.commit()
        db.refresh(new_cinema_hall)
        return new_cinema_hall
    
    async def update_cinema_hall(self,cinema_hall_id,update_cinema_hall_data:cinemaHallUpdateModel,db:AsyncSession):
        cinema_hall_to_update = db.query(CinemaHall).filter(CinemaHall.cinema_hall_id == cinema_hall_id).first()
        if cinema_hall_to_update is not None:
            show_data_dict = update_cinema_hall_data.model_dump()
            for key,val in show_data_dict.items():
                setattr(cinema_hall_to_update,key,val)
            db.commit()
            return cinema_hall_to_update
        else:
            return None
        
    async def delete_a_cinema_hall(self,cinema_hall_id,db:AsyncSession):
        cinema_hall_to_delete= db.query(CinemaHall).filter(CinemaHall.cinema_hall_id == cinema_hall_id).first()
        if cinema_hall_to_delete is not None:
            db.delete(cinema_hall_to_delete)
            db.commit()
            return "cinema_hall deleted"
        else:
            return None

cinema_hall_service = CinemaHallService()

