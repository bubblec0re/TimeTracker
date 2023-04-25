from fastapi import FastAPI
from app.routes import worktypes_router, workrecords_router

app = FastAPI()
app.include_router(workrecords_router)
app.include_router(worktypes_router)
