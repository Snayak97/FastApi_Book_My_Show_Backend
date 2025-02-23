from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean
from sqlalchemy.orm import relationship

from typing import List,Optional
import uuid
from datetime import datetime,date

import sqlalchemy.dialects.postgresql as pg

from src.db.dbConnect import Base



class Movie(Base):
    __tablename__="movies"
    uid: uuid.UUID = Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    language = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    release_date = Column(Date, nullable=False)
    country = Column(String, nullable=False)
    # user_uid: Optional[uuid.UUID] = Column(pg.UUID(as_uuid=True), ForeignKey("users.uid"),nullable=True)
    created_at:datetime=Column(pg.TIMESTAMP, default=datetime.utcnow, nullable=False)
    update_at:datetime=Column(pg.TIMESTAMP,default=datetime.utcnow,onupdate=datetime.utcnow, nullable=False)

    shows    = relationship("Show", back_populates="movie")


