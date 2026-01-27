from fastapi import FastAPI

from app.api.v1.routes import users
from app.core.exceptions import AppException
from app.core.handlers import app_exception_handler


app = FastAPI(title='Backend Roadmap Project')

app.include_router(
    users.router,
    prefix='/api/v1'
)

app.add_exception_handler(
    AppException,
    app_exception_handler
)

