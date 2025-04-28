import app.todo.entities.todo_item_entity as todo_item_entity

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.utils.exceptions import Exceptions
from app.auth.auth_routes import router as auth_router
from app.todo.routes.todo_routes import router as todo_router
from app.core.config import engine


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todo_item_entity.Base.metadata.create_all(bind=engine)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    return Exceptions.handler_error_400()


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request,
                                 exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


app.include_router(router=auth_router, prefix="/auth")
app.include_router(router=todo_router, prefix="/todo")