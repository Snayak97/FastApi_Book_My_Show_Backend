from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import Session
from datetime import datetime
from src.models import Show

from sqlalchemy.future import select
from sqlalchemy import desc

import uuid

from src.schemas.showSchema import showCreateModel,showUpdateModel

class ShowService:
    async def get_all_show(self,db:AsyncSession):
        # Anotheraproch by asending
        # books=db.query(Book).all()

        #using desending
        statement = select(Show).order_by(desc(Show.created_at))
        # Execute the statement and await the result
        result =db.execute(statement)
        # Extract the list of books
        shows = result.scalars().all()
        return shows
    
    async def get_a_show(self,show_id,db:AsyncSession):
        try:
        # Ensure the book_uid is a UUID object
            show_id = uuid.UUID(show_id)
        except ValueError:
            return f"Invalid UUID format: {show_id}"
       
        show= db.query(Show).filter(Show.show_id==show_id).first()
        return show

    async def create_a_show(self,show_data,db:AsyncSession):
        show_data_dict = show_data.model_dump()
        new_show = Show(**show_data_dict)
        print(new_show)
        db.add(new_show)
        db.commit()
        db.refresh(new_show)
        return new_show
    
    async def update_show(self,show_id,update_show_data:showUpdateModel,db:AsyncSession):
        show_to_update = db.query(Show).filter(Show.show_id == show_id).first()
        if show_to_update is not None:
            show_data_dict = update_show_data.model_dump()
            for key,val in show_data_dict.items():
                setattr(show_to_update,key,val)
            db.commit()
            return show_to_update
        else:
            return None
        
    async def delete_a_show(self,show_id,db:AsyncSession):
        show_to_delete= db.query(Show).filter(Show.show_id == show_id).first()
        if show_to_delete is not None:
            db.delete(show_to_delete)
            db.commit()
            return "show deleted"
        else:
            return None

show_service = ShowService()

