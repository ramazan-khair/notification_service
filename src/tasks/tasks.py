import asyncio
from datetime import datetime

from pydantic import BaseModel

from src.database import async_session_maker_null_pool
from src.schemas.notifications import NotifcationLogAdd
from src.schemas.templates import TemplateChannelDTO
from src.schemas.users import UserDTO
from src.tasks.celery_app import celery_instance
from src.utils.db_manager import DBManager
from jinja2 import Template
from src.services.notifications import NotificationService as ns, NotificationService


async def send_notification_helper(
        template_channel: TemplateChannelDTO,
        user: UserDTO,
        data: dict[str, str]
):
    async with DBManager(session_factory=async_session_maker_null_pool) as db:
        template = Template(template_channel.body)
        result = template.render(**data)
        sent = False
        try:
            dict_channels = {
                "email": user.email,
                "sms": user.sms,
                "telegram": user.telegram,
                "push_token": user.push_token
            }
            dict_func = {
                "email": ns.send_email,
                "sms": ns.send_sms,
                "telegram": ns.send_telegram,
                "push": ns.send_push
            }

            for k, v in dict_channels.items():
                if template_channel.channel == k and v:
                    func = dict_func[k]
                    if k == "email" or k == "push":
                        await func(v, template_channel.subject, result)
                    else:
                        await func(v, result)
                    sent = True

            if sent:
                notificationlog = NotifcationLogAdd(
                    user_id=user.id,
                    status="success",
                    notification=result,
                    sent_at=datetime.utcnow(),
                )
            else:
                notificationlog = NotifcationLogAdd(
                    user_id=user.id,
                    status="skipped",
                    notification=result,
                    error=f"No contact for channel '{template_channel.channel}'",
                    sent_at=datetime.utcnow(),
                )
            await NotificationService(db).add_notification_log(notificationlog)

        except Exception as e:
            notificationlog = NotifcationLogAdd(
                user_id=user.id,
                status="failed",
                notification=result,
                error=str(e),
                sent_at=datetime.utcnow(),
            )
            await NotificationService(db).add_notification_log(notificationlog)


@celery_instance.task(name="send_notification")
def send_notification(template_channel, user, data):
    template_channel = TemplateChannelDTO.model_validate(template_channel)
    user = UserDTO.model_validate(user)
    asyncio.run(
        send_notification_helper(
            template_channel,
            user,
            data
        )
    )