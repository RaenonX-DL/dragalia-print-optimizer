from enum import Enum, auto
from typing import Optional

from .param import PrintParameter

__all__ = ("Affinity",)


PrintEffect = tuple[PrintParameter, float]


class Affinity(Enum):
    FS = auto()
    ATK = auto()

    @property
    def effect_at_max(self) -> PrintEffect:
        return _effect_at_max[self]

    def get_effect_at_count(self, count: int) -> Optional[PrintEffect]:
        return _effect_at_count[self].get(count)


_effect_at_count: dict[Affinity, dict[int, PrintEffect]] = {
    Affinity.FS: {
        2: (PrintParameter.FS_DMG_AFFINITY, 0.05),
        3: (PrintParameter.FS_DMG_AFFINITY, 0.08),
        4: (PrintParameter.FS_DMG_AFFINITY, 0.15),
    },
    Affinity.ATK: {
        4: (PrintParameter.ATK_PASSIVE_AFFINITY, 0.08),
    },
}

# noinspection PyUnresolvedReferences
_effect_at_max: dict[Affinity, PrintEffect] = {
    Affinity.FS: max(_effect_at_count[Affinity.FS].items(), key=lambda item: item[0])[1],
    Affinity.ATK: max(_effect_at_count[Affinity.ATK].items(), key=lambda item: item[0])[1],
}
