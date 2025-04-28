from abc import ABC, abstractmethod
from typing import List, Optional

from app.todo.entities.todo_item_entity import TodoItemEntity
from app.todo.models.create_todo_request_model import TodoCreateModel
from app.todo.models.create_todo_response_model import TodoResponseModel

class TodoRepository(ABC):
    @abstractmethod
    def create(self, todo: TodoCreateModel) -> TodoItemEntity:
        pass
    
    @abstractmethod
    def get_by_id(self, todo_id: str) -> Optional[TodoItemEntity]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[TodoItemEntity]:
        pass
    
    @abstractmethod
    def update(self, todo_id: str, todo: TodoResponseModel) -> Optional[TodoItemEntity]:
        pass
    
    @abstractmethod
    def delete(self, todo_id: str) -> bool:
        pass