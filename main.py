import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from src.database.database import engine, SessionLocal
from src.database import models
from src.api import ToDoBase

app = FastAPI()
models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/todo/{todo_id}')
async def read_todo(todo_id: int, db: db_dependency):
    result = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if not result:
        raise HTTPException(status_code = 404, detail = 'ToDo not found!')
    return result

@app.post('/todo/')
async def create_todo(todo: ToDoBase, db: db_dependency):
    db_todo = models.ToDo(todo_text = todo.todo_text)
    db_is_done = models.ToDo(is_done = todo.is_done)
    db.add(db_todo)
    db.add(db_is_done)
    db.commit()

if __name__ == "__main__":
    uvicorn.run(app, host = '127.0.0.1', port = 8000)