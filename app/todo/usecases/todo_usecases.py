from typing import List, Optional
from sqlalchemy.orm import Session

from app.todo.models.create_todo_request_model import TodoCreateModel
from app.todo.models.create_todo_response_model import TodoResponseModel
from app.todo.repositories.todo_repository_impl import TodoRepositoryImpl

class TodoUsecases:
    def __init__(self, db: Session):
        self.repository = TodoRepositoryImpl(db)

    def create_todo(self, todo: TodoCreateModel) -> TodoResponseModel:
        created_todo = self.repository.create(todo)
        return TodoResponseModel(
            id=created_todo.id,
            title=created_todo.title,
            description=created_todo.description,
            created_at=created_todo.created_at.isoformat(),
            updated_at=created_todo.updated_at.isoformat(),
        )

    def get_all_todos(self) -> List[TodoResponseModel]:
        todo_list = self.repository.get_all()
        return [
            TodoResponseModel(
                id=todo.id,
                title=todo.title,
                description=todo.description,
                created_at=todo.created_at.isoformat(),
                updated_at=todo.updated_at.isoformat(),
        )
            for todo in todo_list
        ]

    def get_todo_by_id(self, todo_id: int) -> Optional[TodoResponseModel]:
        entity = self.repository.get_by_id(todo_id)
        if entity:
            return TodoResponseModel(
                id=entity.id,
                title=entity.title,
                description=entity.description,
                created_at=entity.created_at.isoformat(),
                updated_at=entity.updated_at.isoformat(),
        )
        return None

    def update_todo(self,
                    todo_id: int,
                    updated_todo: TodoCreateModel) -> Optional[TodoResponseModel]:
        entity = self.repository.update(todo_id, updated_todo)
        if entity:
            return TodoResponseModel(
                id=entity.id,
                title=entity.title,
                description=entity.description,
                created_at=entity.created_at.isoformat(),
                updated_at=entity.updated_at.isoformat(),
        )
        return None

    def delete_todo(self, todo_id: int) -> bool:
        return self.repository.delete(todo_id)
