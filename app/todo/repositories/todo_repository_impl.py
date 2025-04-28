from typing import List, Optional
from sqlalchemy.orm import Session

from app.todo.entities.todo_item_entity import TodoItemEntity
from app.todo.repositories.todo_repository import TodoRepository
from app.todo.models.create_todo_request_model import TodoCreateModel


class TodoRepositoryImpl(TodoRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, todo: TodoCreateModel) -> TodoItemEntity:
        new_todo = TodoItemEntity(**todo.model_dump())
        self.db.add(new_todo)
        self.db.commit()
        self.db.refresh(new_todo)
        return new_todo

    def get_all(self) -> List[TodoItemEntity]:
        return self.db.query(TodoItemEntity).all()

    def get_by_id(self, todo_id: int) -> Optional[TodoItemEntity]:
        return self.db.query(TodoItemEntity).filter(TodoItemEntity.id == todo_id).first()

    def update(self,
               todo_id: int,
               updated_todo: TodoCreateModel) -> Optional[TodoItemEntity]:
        todo = self.db.query(TodoItemEntity).filter(TodoItemEntity.id == todo_id).first()
        if todo:
            for key, value in updated_todo.dict().items():
                setattr(todo, key, value)
            self.db.commit()
            return todo
        return None

    def delete(self, todo_id: int) -> bool:
        todo = self.db.query(TodoItemEntity).filter(TodoItemEntity.id == todo_id).first()
        if todo:
            self.db.delete(todo)
            self.db.commit()
            return True
        return False
