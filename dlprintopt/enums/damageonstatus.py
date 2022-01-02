from enum import Enum, auto

__all__ = ("DamageOnStatus",)


class DamageOnStatus(Enum):
    PRE_OD = auto()
    OD = auto()
    BK = auto()
