from dataclasses import dataclass

from dlprintopt.enums import StatusParameter, DamageOnStatus, DamageType

__all__ = ("CalcParams",)


@dataclass
class CalcParams:
    additional_base: dict[StatusParameter, float]
    damage_distribution: dict[DamageType, float]
    damage_status_distribution: dict[DamageOnStatus, float]
