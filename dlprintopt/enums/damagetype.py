from enum import Enum, auto

__all__ = ("DamageType",)


class DamageType(Enum):
    SKILL = auto()
    DRAGON = auto()
    FS = auto()
