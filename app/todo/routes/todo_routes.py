from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.todo.models.create_todo_request_model import TodoCreateModel
from app.todo.models.create_todo_response_model import TodoResponseModel
from app.todo.usecases.todo_usecases import TodoUsecases
from app.utils.auth_validators import token_validator
from app.core.config import get_db

router = APIRouter(tags=["Todo"])


@router.post("/", response_model=TodoResponseModel, status_code=201)
def create_todo(
    todo: TodoCreateModel,
    db: Session = Depends(get_db),
    token: str = Depends(token_validator),
):
    usecase = TodoUsecases(db)
    return usecase.create_todo(todo)


@router.get("/list", response_model=List[TodoResponseModel])
def read_todos(db: Session = Depends(get_db),
               token: str = Depends(token_validator)):
    controller = TodoUsecases(db)
    todo_list = controller.get_all_todos()
    if not todo_list:
        raise HTTPException(status_code=404,
                            detail="Nenhuma tarefa encontrada.")
    return todo_list


@router.get("/{todo_id}", response_model=TodoResponseModel)
def read_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(token_validator)
):
    controller = TodoUsecases(db)
    todo = controller.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return todo


@router.put("/{todo_id}", response_model=TodoResponseModel)
def update_todo(
    todo_id: int,
    updated_todo: TodoCreateModel,
    db: Session = Depends(get_db),
    token: str = Depends(token_validator),
):
    controller = TodoUsecases(db)
    todo = controller.update_todo(todo_id, updated_todo)
    if not todo:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return todo


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(token_validator)
):
    controller = TodoUsecases(db)
    success = controller.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return {"message": "Tarefa deletada com sucesso!"}