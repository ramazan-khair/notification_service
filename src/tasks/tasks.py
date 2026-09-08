from pydantic import BaseModel

from src.database import async_session_maker_null_pool
from src.utils.db_manager import DBManager
from jinja2 import Template
from src.services.notifications import NotificationService as ns


async def send_notification_helper(
        template_channel: BaseModel,
        user: BaseModel,
        data: dict[str, str]
):
        template = Template(template_channel.body)
        result = template.render(**data)
        if template_channel.channel == "email" and user.email:
            await ns.send_email(user.email, template_channel.subject, result)
        elif template_channel.channel == "sms" and user.sms:
            await ns.send_sms(user.sms, result)
        elif template_channel.channel == "telegram" and user.telegram:
            await ns.send_telegram(user.telegram, result)