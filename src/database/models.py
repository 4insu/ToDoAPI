from sqlalchemy import Boolean, Column, Integer, String
from src.database import Base

class ToDo(Base):
    __tablename__ = 'todolist'
    id = Column(Integer, primary_key = True, index = True)
    todo_text = Column(String, index = True)
    is_done = Column(Boolean, default = False)