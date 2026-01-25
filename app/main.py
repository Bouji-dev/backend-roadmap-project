from fastapi import FastAPI
from app.api.v1.routes import users

app = FastAPI(title='Backend Roadmap Project')

app.include_router(
    users.router,
    prefix='/api/v1'
)


