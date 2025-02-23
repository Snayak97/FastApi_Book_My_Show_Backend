from fastapi import FastAPI
import uvicorn

from src.routes import userRouter,movieRouter,showRouter,bookingRouter,cinemaHallRouter,seatRouter

from src.db.dbConnect import engine

from src.models import Base



app = FastAPI()



# model
Base.metadata.create_all(engine)

app.include_router(userRouter.user_router)
app.include_router(movieRouter.movie_router)
app.include_router(showRouter.show_router)
app.include_router(bookingRouter.booking_router)
app.include_router(cinemaHallRouter.cinema_hall_router)
app.include_router(seatRouter.seat_router)

@app.get("/")
def read_root():
    return {"message": "Hello, Soumya!"}



