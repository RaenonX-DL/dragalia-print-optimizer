from dataclasses import dataclass, field

from dlprintopt.const import CDMG_RATE
from dlprintopt.utils import get_expected_crt_effectiveness

__all__ = ("Effectiveness",)


@dataclass
class Effectiveness:
    base: float
    crt_rate: float
    cdmg_boost_rate: float

    rate_no_crt: float = field(init=False)
    rate_incl_crt: float = field(init=False)
    rate_all_crt: float = field(init=False)

    def __post_init__(self):
        self.rate_no_crt = self.base
        self.rate_incl_crt = self.base * get_expected_crt_effectiveness(self.crt_rate, self.cdmg_boost_rate)
        self.rate_all_crt = self.base * (CDMG_RATE + self.cdmg_boost_rate)

    def __gt__(self, other: "Effectiveness"):
        return self.rate_incl_crt > other.rate_incl_crt

    def __repr__(self):
        return f"Normal: {self.rate_incl_crt:.5f}\n" \
               f"No CRT: {self.rate_no_crt:.5f}\n" \
               f"All CRT: {self.rate_all_crt:.5f}"
