from datetime import datetime

from pydantic import BaseModel


class TodoResponseModel(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_validate
    
    class Config:
        from_atributes = True