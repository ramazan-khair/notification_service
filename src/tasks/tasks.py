import asyncio
from datetime import datetime

from src.database import async_session_maker_null_pool
from src.schemas.contacts import ContactDTO
from src.schemas.loggs import LoggAdd
from src.schemas.templates import TemplateChannelDTO
from src.tasks.celery_app import celery_instance
from src.utils.db_manager import DBManager
from jinja2 import Template
from src.services.notifications import NotificationService as ns, NotificationService


async def send_notification_helper(
        template_channel: TemplateChannelDTO,
        contact: ContactDTO,
        data: dict[str, str]
):
    async with DBManager(session_factory=async_session_maker_null_pool) as db:
        template = Template(template_channel.body)
        result = template.render(**data)
        sent = False
        try:
            dict_channels = {
                "email": contact.email,
                "sms": contact.sms,
                "telegram": contact.tg_chat_id,
            }
            dict_func = {
                "email": ns.send_email,
                "sms": ns.send_sms,
                "telegram": ns.send_telegram,
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
                logg = LoggAdd(
                    user_id=contact.id,
                    status="success",
                    notification=result,
                    sent_at=datetime.utcnow(),
                )
            else:
                logg = LoggAdd(
                    user_id=contact.id,
                    status="skipped",
                    notification=result,
                    error=f"No contact for channel '{template_channel.channel}'",
                    sent_at=datetime.utcnow(),
                )
            await NotificationService(db).add_notification_log(logg)

        except Exception as e:
            logg = LoggAdd(
                user_id=contact.id,
                status="failed",
                notification=result,
                error=str(e),
                sent_at=datetime.utcnow(),
            )
            await NotificationService(db).add_notification_log(logg)


async def send_push_helper(
        template_channel: TemplateChannelDTO,
        contact: ContactDTO,
        fcm_token: str,
        data: dict[str, str]
):
    async with DBManager(session_factory=async_session_maker_null_pool) as db:
        template = Template(template_channel.body)
        result = template.render(**data)
        try:
            await ns.send_push(fcm_token, template_channel.subject, result)
            logg =LoggAdd(
                user_id=contact.id,
                status="success",
                notification=result,
                sent_at=datetime.utcnow(),
            )
            await NotificationService(db).add_notification_log(logg)
        except Exception as e:
            logg = LoggAdd(
                user_id=contact.id,
                status="failed",
                notification=result,
                error=str(e),
                sent_at=datetime.utcnow(),
            )
            await NotificationService(db).add_notification_log(logg)


@celery_instance.task(name="send_notification")
def send_notification(template_channel, contact, data):
    template_channel = TemplateChannelDTO.model_validate(template_channel)
    contact = ContactDTO.model_validate(contact)
    asyncio.run(
        send_notification_helper(
            template_channel,
            contact,
            data
        )
    )


@celery_instance.task(name="send_push_notification")
def send_push_notification(template_channel, contact, fcm_token, data):
    template_channel = TemplateChannelDTO.model_validate(template_channel)
    contact = ContactDTO.model_validate(contact)
    asyncio.run(
        send_push_helper(
            template_channel,
            contact,
            fcm_token,
            data
        )
    )