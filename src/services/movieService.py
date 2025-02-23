from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import Session
from datetime import datetime
from src.models import Movie

from sqlalchemy.future import select
from sqlalchemy import desc

import uuid

from src.schemas.movieSchema import movieCreateModel,movieUpdateModel

class MovieService:
    async def get_all_movies(self,db:AsyncSession):
        # Anotheraproch by asending
        # books=db.query(Book).all()

        #using desending
        statement = select(Movie).order_by(desc(Movie.created_at))
        # Execute the statement and await the result
        result =db.execute(statement)
        # Extract the list of books
        movies = result.scalars().all()
        return movies
    
    async def create_a_movie(self,movie_data,db:AsyncSession):
        movie_data_dict = movie_data.model_dump()
        new_movie = Movie(**movie_data_dict)
        if isinstance(movie_data_dict["release_date"], str):
            new_movie.release_date = datetime.strptime(
            movie_data_dict["release_date"], "%Y-%m-%d"
            ).date()
        else:
            new_movie.release_date = movie_data_dict["release_date"]
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie
    
    async def update_movie(self,movie_uid,update_movie_data:movieUpdateModel,db:AsyncSession):
        movie_to_update = db.query(Movie).filter(Movie.uid == movie_uid).first()
        if movie_to_update is not None:
            movie_data_dict = update_movie_data.model_dump()
            for key,val in movie_data_dict.items():
                setattr(movie_to_update,key,val)
            db.commit()
            return movie_to_update
        else:
            return None
        
    async def delete_a_movie(self,movie_uid,db:AsyncSession):
        movie_to_delete= db.query(Movie).filter(Movie.uid == movie_uid).first()
        if movie_to_delete is not None:
            db.delete(movie_to_delete)
            db.commit()
            return "movie deleted"
        else:
            return None

movie_service = MovieService()