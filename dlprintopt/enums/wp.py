from enum import Enum, auto

__all__ = ("PrintType",)


class PrintType(Enum):
    R5 = auto()
    R4 = auto()
    SINDOM = auto()
    KALEIDO = auto()

    @property
    def max_count(self) -> int:
        return _type_max_count[self]


_type_max_count: dict[PrintType, int] = {
    PrintType.R5: 3,
    PrintType.R4: 2,
    PrintType.SINDOM: 2,
    PrintType.KALEIDO: 1,
}
