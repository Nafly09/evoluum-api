from pydantic import BaseModel, Field


class TodoCreateModel(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1, max_length=1024)