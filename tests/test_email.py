import asyncio

from src.services.notifications import NotificationService


async def main():
    await NotificationService.send_email(
        to_email="ramazanhajrullin864@icloud.com",
        subject="Тест Notification Service",
        message="Привет! Это тестовое письмо из моего NotificationService."
    )

    print("Письмо успешно отправлено!")

    if __name__ == "__main__":
        asyncio.run(main())