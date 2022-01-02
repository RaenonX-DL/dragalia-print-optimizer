from dataclasses import dataclass
from typing import Optional

from dlprintopt.enums import Affinity, PrintParameter

__all__ = ("Effect",)


@dataclass
class Effect:
    effect_param: Optional[PrintParameter] = None
    effect_rate: Optional[float] = None

    enables_affinity: Optional[Affinity] = None
