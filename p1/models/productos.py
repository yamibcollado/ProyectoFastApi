from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import Column, Integer, String
from config.db import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)