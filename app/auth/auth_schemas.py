from pydantic import BaseModel, Field


class AuthResponse(BaseModel):
    token: str = Field(..., description="Logged user token")