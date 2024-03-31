import pydantic


class ServiceConfig(pydantic.BaseModel):
    """Конфигурация сервиса"""

    target_width: int
    """Целевая ширина изображения"""
    target_height: int
    """Целевая высота изображения"""
