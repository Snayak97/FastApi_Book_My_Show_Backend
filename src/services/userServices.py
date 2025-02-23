from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter,Depends,HTTPException,status,Response

from sqlalchemy.future import select
from sqlalchemy import desc


import uuid

from datetime import datetime

from src.models import User

from src.auth.hashingPassword import Hash


from src.schemas.userSchema import CreateUserModel,UserModel



class UserService:
    
    async def get_user_by_email(self,email,db:AsyncSession):
        user= db.query(User).filter(User.email==email).first()
        return user
    
    async def user_exists(self,email,db:AsyncSession):
        exist_user = await self.get_user_by_email(email,db)
        return True if exist_user is not None else False
    

    async def create_user(self,user_data:CreateUserModel,db:AsyncSession):
        user_data_dict= user_data.model_dump()
        new_user= User(** user_data_dict)
        new_user.password_hash = Hash.bcrypt_password(user_data_dict["password_hash"])
        new_user.role = "user"
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    async def delete_user(self,user_data,db:AsyncSession):
        pass

    async def make_admin(self,user_id, db:AsyncSession):
        user = db.query(User).filter(User.uid == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
    
        if user.role=="admin":
            return {"message": "User is already an admin"}

        user.role="admin"
        db.commit()
        db.refresh(user)
    
        return {"message": f"User {user.username} is now an Admin"}

user_service=UserService()