from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session

from src.db.dbConnect import get_db
from typing import Optional,List
# from sqlalchemy.ext.asyncio import AsyncSession

from src.services.cinemaHallService import cinema_hall_service
from src.schemas.cinemaHallModelSchema import cinemaHallCreateModel,cinemaHallUpdateModel,CinemaHall
from src.auth.dependency import AccessTokenBearer

cinema_hall_router=APIRouter(
    prefix="/api/v1/cinema_hall",
    tags=["CinemaHall"],
)

# create show
@cinema_hall_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_cinema_hall(cinema_hall_data:cinemaHallCreateModel,db:Session=Depends(get_db)):
    return await cinema_hall_service.create_a_cinema_hall(cinema_hall_data,db)


# get all shows
@cinema_hall_router.get("/",response_model=List[CinemaHall] ,status_code=status.HTTP_200_OK)
async def get_cinema_halls(db:Session=Depends(get_db)):
    return await cinema_hall_service.get_all_cinema_hall(db)

# get a show
@cinema_hall_router.get("/{cinema_hall_id}",response_model=CinemaHall, status_code=status.HTTP_200_OK)
async def get_cinema_hall(cinema_hall_id:str,db:Session=Depends(get_db)):
    return await cinema_hall_service.get_a_cinema_hall(cinema_hall_id,db)

#update show
@cinema_hall_router.patch("/{cinema_hall_id}",response_model=CinemaHall, status_code=status.HTTP_202_ACCEPTED)
async def update_cinema_hall(cinema_hall_id:str,update_show_data:cinemaHallUpdateModel,db:Session=Depends(get_db)):
    return await cinema_hall_service.update_cinema_hall(cinema_hall_id,update_show_data,db)

# delete show
@cinema_hall_router.delete("/{cinema_hall_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_cinema_hall(cinema_hall_id:str,db:Session=Depends(get_db)):
    return await cinema_hall_service.delete_a_cinema_hall(cinema_hall_id,db)
