import smtplib
from email.message import EmailMessage

from src.config import settings


msg = EmailMessage()
msg["From"] = settings.EMAIL_FROM
msg["To"] = "ramazanhajrullin864@icloud.com"
msg["Subject"] = "Тест Notification Service"
msg.set_content("Привет! Это тестовое письмо из Notification Service.")


with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
    server.starttls()
    server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
    server.send_message(msg)


print("Письмо успешно отправлено!")