import pydantic
from fastapi import File

class ServiceOutput(pydantic.BaseModel):
    """Датаконтракт выхода сервиса"""

    x1: int = pydantic.Field(default=0)
    """Верхний левый угол"""
    y1: int = pydantic.Field(default=0)
    """Верхний левый угол"""
    x2: int = pydantic.Field(default=0)
    """Правый нижний угол"""
    y2: int = pydantic.Field(default=0)
    """Правый нижний угол"""
    classe: str = 'undefined'
    """Класс объекта"""