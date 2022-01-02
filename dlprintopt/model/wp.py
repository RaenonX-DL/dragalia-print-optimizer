from dataclasses import dataclass
from typing import Optional

from dlprintopt.enums import Affinity, PrintType
from .effect import Effect

__all__ = ("Wyrmprint",)


@dataclass
class Wyrmprint:
    name: str

    type: PrintType

    effects: list[Effect]

    affinity_type: Optional[Affinity] = None
