from fastapi import FastAPI

from app.routes import users_router, workrecords_router, worktypes_router

app = FastAPI()
app.include_router(workrecords_router)
app.include_router(worktypes_router)
app.include_router(users_router)
