from enum import Enum, auto
from typing import Optional

__all__ = ("StatusParameter", "get_status_base_rates", "PrintParameter",)


class StatusParameter(Enum):
    ATK_PASSIVE = auto()
    FS_DMG = auto()
    SKILL_DMG = auto()
    CRT_RATE = auto()
    CRT_DAMAGE = auto()
    PUNISHER = auto()


def get_status_base_rates(additional_rates: dict[StatusParameter, float]) -> dict[StatusParameter, float]:
    ret: dict[StatusParameter, float] = {
        StatusParameter.ATK_PASSIVE: 1,
        StatusParameter.FS_DMG: 1,
        StatusParameter.SKILL_DMG: 1,
        StatusParameter.CRT_RATE: 0.02,
        # Base included when calculating effectiveness
        StatusParameter.CRT_DAMAGE: 0,
        StatusParameter.PUNISHER: 1,
    }
    for param, rate in additional_rates.items():
        ret[param] += rate

    return ret


class PrintParameter(Enum):
    ATK_PASSIVE_PRINT = auto()
    ATK_PASSIVE_AFFINITY = auto()
    FS_DMG_PRINT = auto()
    FS_DMG_AFFINITY = auto()
    SKILL_DMG = auto()
    CRT_RATE = auto()
    CRT_DAMAGE = auto()
    PUNISHER_POISON = auto()
    PUNISHER_STORMLASH = auto()

    @property
    def max_value(self) -> Optional[float]:
        return _print_param_max_val[self]

    @property
    def to_status(self) -> StatusParameter:
        return _print_param_to_status[self]


_print_param_to_status: dict[PrintParameter, StatusParameter] = {
    PrintParameter.ATK_PASSIVE_PRINT: StatusParameter.ATK_PASSIVE,
    PrintParameter.ATK_PASSIVE_AFFINITY: StatusParameter.ATK_PASSIVE,
    PrintParameter.SKILL_DMG: StatusParameter.SKILL_DMG,
    PrintParameter.FS_DMG_PRINT: StatusParameter.FS_DMG,
    PrintParameter.FS_DMG_AFFINITY: StatusParameter.FS_DMG,
    PrintParameter.CRT_RATE: StatusParameter.CRT_RATE,
    PrintParameter.CRT_DAMAGE: StatusParameter.CRT_DAMAGE,
    PrintParameter.PUNISHER_POISON: StatusParameter.PUNISHER,
    PrintParameter.PUNISHER_STORMLASH: StatusParameter.PUNISHER,
}

_print_param_max_val: dict[PrintParameter, Optional[float]] = {
    PrintParameter.ATK_PASSIVE_PRINT: 0.2,
    PrintParameter.ATK_PASSIVE_AFFINITY: None,
    PrintParameter.FS_DMG_PRINT: 0.5,
    PrintParameter.FS_DMG_AFFINITY: None,
    PrintParameter.SKILL_DMG: 0.4,
    PrintParameter.CRT_RATE: 0.15,
    PrintParameter.CRT_DAMAGE: 0.25,
    PrintParameter.PUNISHER_POISON: 0.3,
    PrintParameter.PUNISHER_STORMLASH: 0.25,
}
