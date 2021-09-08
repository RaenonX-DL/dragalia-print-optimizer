from enum import Enum, auto

__all__ = ("PrintType",)


class PrintType(Enum):
    R5 = auto()
    R4 = auto()
    SINDOM = auto()
