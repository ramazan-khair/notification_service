from firebase_admin import messaging

from src.config import settings
from src.models import NotificationLog
from src.services.base import BaseService


import smtplib
from email.message import EmailMessage
import httpx


class NotificationService(BaseService):

    async def add_notification_log(self, data: NotificationLog):
        notificationlog = await self.db.notificationlogs.add(data)
        await self.db.commit()
        return notificationlog

    async def send_notification(self, user_id: int, template_channel_id: int, data: dict[str, str]):
        from src.tasks.tasks import send_notification
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
        msg["From"] = settings.EMAIL_FROM
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(message)

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
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
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

        async with httpx.AsyncClient(
            proxy="socks5://127.0.0.1:10808"
        ) as client:
            response = await client.post(
                url,
                json={
                    "chat_id": chat_id,
                    "text": message
                }
            )

    @staticmethod
    async def send_push(token: str, title: str, body: str):
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=token,
        )

        response = messaging.send(message)




