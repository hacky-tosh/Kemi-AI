from fastapi import FastAPI
from app.routes import course_router

app = FastAPI()

app.include_router(course_router)
