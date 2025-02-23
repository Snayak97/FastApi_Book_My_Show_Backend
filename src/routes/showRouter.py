from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session

from src.db.dbConnect import get_db
from typing import Optional,List
# from sqlalchemy.ext.asyncio import AsyncSession

from src.services.showService import show_service
from src.schemas.showSchema import showCreateModel,showUpdateModel,Show
from src.auth.dependency import AccessTokenBearer

show_router=APIRouter(
    prefix="/api/v1/show",
    tags=["Shows"],
)

# create show
@show_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_show(show_data:showCreateModel,db:Session=Depends(get_db)):
    return await show_service.create_a_show(show_data,db)


# get all shows
@show_router.get("/",response_model=List[Show] ,status_code=status.HTTP_200_OK)
async def get_shows(db:Session=Depends(get_db)):
    return await show_service.get_all_show(db)

# get a show
@show_router.get("/{show_id}",response_model=Show, status_code=status.HTTP_200_OK)
async def get_show(show_id:str,db:Session=Depends(get_db)):
    return await show_service.get_a_show(show_id,db)

#update show
@show_router.patch("/{show_id}",response_model=Show, status_code=status.HTTP_202_ACCEPTED)
async def update_show(show_id:str,update_show_data:showUpdateModel,db:Session=Depends(get_db)):
    return await show_service.update_show(show_id,update_show_data,db)

# delete show
@show_router.delete("/{show_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_show(show_id:str,db:Session=Depends(get_db)):
    return await show_service.delete_a_show(show_id,db)
