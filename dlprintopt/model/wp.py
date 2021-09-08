from dataclasses import dataclass
from typing import Optional

from dlprintopt.enums import Affinity, PrintParameter, PrintType

__all__ = ("Wyrmprint",)


@dataclass
class Wyrmprint:
    name: str

    type: PrintType

    effect_param: Optional[PrintParameter] = None
    effect_rate: Optional[float] = None

    affinity_type: Optional[Affinity] = None
    enables_affinity: Optional[Affinity] = None
