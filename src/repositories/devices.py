from src.models.devices import Device
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import DeviceDataMapper


class DevicesRepository(BaseRepository):
    model = Device
    mapper = DeviceDataMapper