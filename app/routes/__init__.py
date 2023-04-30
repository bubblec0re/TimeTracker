from fastapi import APIRouter

from .workrecords import workrecords_router
from .worktypes import worktypes_router
from .users import users_router

router = APIRouter()
router.include_router(workrecords_router)
router.include_router(worktypes_router)
router.include_router(users_router)
