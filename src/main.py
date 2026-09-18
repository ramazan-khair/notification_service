import sys
from pathlib import Path

from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.api.templates import router as templates_router
from src.api.notifications import router as notification_router

app = FastAPI()


app.include_router(templates_router)
app.include_router(notification_router)

