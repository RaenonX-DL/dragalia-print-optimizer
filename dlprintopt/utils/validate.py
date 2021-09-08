from typing import TYPE_CHECKING

from dlprintopt.enums import PrintType

if TYPE_CHECKING:
    from dlprintopt.model import Wyrmprint

__all__ = ("is_prints_valid",)


def is_prints_valid(prints: list["Wyrmprint"]) -> bool:
    r5_count = len([wp for wp in prints if wp.type == PrintType.R5])
    r4_count = len([wp for wp in prints if wp.type == PrintType.R4])
    sindom_count = len([wp for wp in prints if wp.type == PrintType.SINDOM])

    return r5_count <= 3 and r4_count <= 2 and sindom_count <= 2
