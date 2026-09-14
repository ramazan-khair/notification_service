from pydantic import BaseModel

from src.models import NotificationLog
from src.services.base import BaseService
from jinja2 import Template
from src.tasks.tasks import send_notification

import smtplib
from email.message import EmailMessage
import httpx


class NotificationService(BaseService):

    async def add_notification_log(self, data: NotificationLog):
        notificationlog = await self.db.notificationlogs.add(NotificationLog)
        await self.db.commit()
        return notificationlog

    async def send_notification(self, user_id: int, template_channel_id: int, data: dict[str, str]):
        template_channel = await self.db.templatechannels.get_one(id=template_channel_id)
        user = await self.db.users.get_one(id=user_id)

        send_notification.delay(
            template_channel.model_dump(),
            user.model_dump(),
            data
        )

    @staticmethod
    async def send_email(to_email: str, subject: str, message: str):
        msg = EmailMessage()
        msg["From"] = EMAIL_FROM
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(message)

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)

    @staticmethod
    async def send_sms(to_sms: str, message: str):
        client = Client(
            TWILIO_ACCOUNT_SID,
            TWILIO_AUTH_TOKEN
        )

        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=to_sms
        )

    @staticmethod
    async def send_telegram(chat_id: str, message: str):
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={
                    "chat_id": chat_id,
                    "text": message
                }
            )


