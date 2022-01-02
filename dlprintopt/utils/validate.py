from collections import Counter
from typing import TYPE_CHECKING

from dlprintopt.enums import PrintType

if TYPE_CHECKING:
    from dlprintopt.model import Wyrmprint

__all__ = ("is_prints_valid",)


def is_prints_valid(prints: list["Wyrmprint"]) -> bool:
    type_counter = Counter(map(lambda wp: wp.type, prints))

    for print_type in PrintType:
        if type_counter[print_type] > print_type.max_count:
            return False

    return True
