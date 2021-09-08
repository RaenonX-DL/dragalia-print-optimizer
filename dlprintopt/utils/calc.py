from typing import Iterable

__all__ = ("multiply_items",)


def multiply_items(items: Iterable[float]) -> float:
    ret = 1

    for item in items:
        ret *= item

    return ret
