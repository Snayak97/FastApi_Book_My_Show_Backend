from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session

from src.db.dbConnect import get_db
from typing import Optional,List
# from sqlalchemy.ext.asyncio import AsyncSession

from src.services.movieService import movie_service
from src.schemas.movieSchema import movieCreateModel,movieUpdateModel,Movie
from src.auth.dependency import AccessTokenBearer

movie_router=APIRouter(
    prefix="/api/v1/movie",
    tags=["Movies"],
)

# create movies
@movie_router.post("/",response_model = Movie, status_code=status.HTTP_201_CREATED)
async def create_book(movie_data:movieCreateModel,db:Session=Depends(get_db)):
    return await movie_service.create_a_movie(movie_data,db)

# get all movies
@movie_router.get("/",response_model=List[Movie] ,status_code=status.HTTP_200_OK)
async def get_movies(db:Session=Depends(get_db)):
    return await movie_service.get_all_movies(db)

#update Movies
@movie_router.patch("/{movie_uid}",response_model=Movie, status_code=status.HTTP_202_ACCEPTED)
async def update_book(movie_uid:str,update_movie_data:movieUpdateModel,db:Session=Depends(get_db)):
    return await movie_service.update_movie(movie_uid,update_movie_data,db)

# delete Book
@movie_router.delete("/{movie_uid}", status_code=status.HTTP_202_ACCEPTED)
async def delete_movie(movie_uid:str,db:Session=Depends(get_db)):
    return await movie_service.delete_a_movie(movie_uid,db)