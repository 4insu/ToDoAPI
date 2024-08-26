from pydantic import BaseModel

class ToDoBase(BaseModel):
    todo_text: str
    is_done: bool