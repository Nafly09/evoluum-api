from fastapi import HTTPException, Header

from app.utils.environment_variables import STATIC_AUTH_TOKEN

async def token_validator(token: str = Header(...)):
    if token != STATIC_AUTH_TOKEN:
        raise HTTPException(status_code=403, detail="Permission denied")