from fastapi import APIRouter, HTTPException

from app.auth.auth_schemas import AuthResponse
from app.utils.environment_variables import STATIC_AUTH_TOKEN

router = APIRouter(tags=["Auth"])

@router.get("/token", response_model=AuthResponse)
def get_token():
    token = STATIC_AUTH_TOKEN
    if not token:
        raise HTTPException(status_code=404)
    return AuthResponse(token=token)