from enum import Enum, auto

__all__ = ("DamageType",)


class DamageType(Enum):
    NORMAL = auto()
    SKILL = auto()
    DRAGON = auto()
    DRAGON_SKILL = auto()
    FS = auto()
