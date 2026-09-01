from datetime import date

from pydantic import BaseModel


class UserRegistered(BaseModel):
    username: str
    email: str


class PaymentSuccess(BaseModel):
    username: str
    transaction_id: str
    amount: float
    currency: str


class OrderShipped(BaseModel):
    username: str
    order_id: int
    tracking_number: str
    delivery_date: date

