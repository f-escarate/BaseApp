from sqlalchemy import Column, Date, Float, Integer, String

from database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    continuousVar = Column(Float, primary_key=False)
    discreteVar = Column(Integer, primary_key=False)
    date = Column(Date, primary_key=False)
    image = Column(String, primary_key=False)