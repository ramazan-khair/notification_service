from celery import Celery

from src.config import settings

celery_instance = Celery(
    "tasks",
    broker = settings.REDIS_BROKER,
    include = [
        "src.tasks.tasks"
    ]
)