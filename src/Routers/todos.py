from fastapi import APIRouter, Path, HTTPException, status
from Data.models import Todos
from pydantic import BaseModel, Field
from Data.db import get_all, find_by_id, db_add, db_delete, db_update


class TodoModel(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=200)
    priority: int = Field(gt=0, lt=6)
    completed: bool

router = APIRouter(
    tags=["Todos controllers"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all():
    return get_all(Todos)


@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_id( todo_id: int = Path(gt=0)):
    todo = find_by_id(Todos, todo_id)
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(todo_model: TodoModel):
    new_todo = Todos(**todo_model.model_dump())
    db_add(new_todo)
    return {"message": "Todo created successfully"}


@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(todo_request: TodoModel,
                      todo_id: int = Path(gt=0)):
    todo = find_by_id(Todos, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.title = todo_request.title
    todo.description = todo_request.description
    todo.priority = todo_request.priority
    todo.completed = todo_request.completed
    db_update()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int = Path(gt=0)):
    todo = find_by_id(Todos, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db_delete(todo)
