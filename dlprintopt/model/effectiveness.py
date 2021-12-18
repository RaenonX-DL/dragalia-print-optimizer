from dataclasses import dataclass, field

from dlprintopt.const import CDMG_RATE
from dlprintopt.utils import get_expected_crt_effectiveness

__all__ = ("Effectiveness",)


@dataclass
class Effectiveness:
    base: float = field(default=None)
    crt_rate: float = field(default=None)
    cdmg_boost_rate: float = field(default=None)

    rate_no_crt: float = field(default=None)
    rate_incl_crt: float = field(default=None)
    rate_all_crt: float = field(default=None)

    def __post_init__(self):
        self.rate_no_crt = (
            self.rate_no_crt
            if self.rate_no_crt is not None
            else self.base
        )
        self.rate_incl_crt = (
            self.rate_incl_crt
            if self.rate_incl_crt is not None else
            self.base * get_expected_crt_effectiveness(self.crt_rate, self.cdmg_boost_rate)
        )
        self.rate_all_crt = (
            self.rate_all_crt
            if self.rate_all_crt is not None else
            self.base * (CDMG_RATE + self.cdmg_boost_rate)
        )

    def __gt__(self, other: "Effectiveness"):
        return self.rate_incl_crt > other.rate_incl_crt

    def __add__(self, other: "Effectiveness"):
        return Effectiveness(
            rate_no_crt=self.rate_no_crt + other.rate_no_crt,
            rate_incl_crt=self.rate_incl_crt + other.rate_incl_crt,
            rate_all_crt=self.rate_all_crt + other.rate_all_crt,
        )

    def __radd__(self, other: "Effectiveness"):
        return self + other

    def __repr__(self):
        return f"Normal: {self.rate_incl_crt:.5f}\n" \
               f"No CRT: {self.rate_no_crt:.5f}\n" \
               f"All CRT: {self.rate_all_crt:.5f}"
