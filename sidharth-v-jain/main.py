from typing import List, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Todo CRUD API")
ALLOWED_PRIORITIES = ["low", "medium", "high"]


class Todo(BaseModel):
    id: int
    title: str
    checked: bool = False
    priority: str = "medium"


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, description="At least 3 characters")
    checked: bool = False
    priority: str = "medium"


class TodoUpdate(BaseModel):
    title: str = Field(..., min_length=3, description="At least 3 characters")
    checked: bool = False
    priority: str = "medium"


todos: List[Todo] = []


def find_todo(todo_id: int) -> Optional[Todo]:
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None


def validate_priority(priority: str):
    if priority not in ALLOWED_PRIORITIES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid priority '{priority}'. Allowed values: {ALLOWED_PRIORITIES}",
        )


@app.exception_handler(RequestValidationError)
async def custom_validation_handler(request: Request, exc: RequestValidationError):
    messages = []
    for error in exc.errors():
        field = error["loc"][-1]
        messages.append(f"'{field}': {error['msg']}")
    return JSONResponse(
        status_code=422,
        content={"detail": "Validation failed", "errors": messages},
    )


@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    return todo


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo_in: TodoCreate):
    validate_priority(todo_in.priority)
    new_id = max((todo.id for todo in todos), default=0) + 1
    new_todo = Todo(id=new_id, **todo_in.dict())
    todos.append(new_todo)
    return new_todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_in: TodoUpdate):
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")

    validate_priority(todo_in.priority)
    todo.title = todo_in.title
    todo.checked = todo_in.checked
    todo.priority = todo_in.priority
    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    todos.remove(todo)
    return None


@app.patch("/todos/{todo_id}/complete", response_model=Todo)
def complete_todo(todo_id: int):
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    todo.checked = True
    return todo
