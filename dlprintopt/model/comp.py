from dataclasses import dataclass, field
from typing import Optional, Sequence

from dlprintopt.enums import PrintParameter, get_status_base_rates, StatusParameter
from dlprintopt.utils import is_prints_valid, get_print_effectiveness, multiply_items

from .calcparams import CalcParams
from .effectiveness import Effectiveness
from .wp import Wyrmprint

__all__ = ("PrintComp",)


@dataclass
class PrintComp:
    prints: Sequence[Wyrmprint]
    params: CalcParams

    print_effects: dict[PrintParameter, float] = field(init=False)

    _effectiveness: Optional[Effectiveness] = None

    def __post_init__(self):
        if not is_prints_valid(self.prints):
            raise ValueError("Invalid print comp")

        self.print_effects = get_print_effectiveness(self.prints)

    def load_effectiveness(self) -> None:
        self._effectiveness = self._get_prints_effectiveness()

    @property
    def effectiveness(self) -> Effectiveness:
        if self._effectiveness:
            return self._effectiveness

        self.load_effectiveness()
        return self._effectiveness

    def _get_prints_effectiveness(self) -> Effectiveness:
        effectivenesses: list[Effectiveness] = []

        for damage_type, distribution_ratio in self.params.damage_distribution.items():
            if distribution_ratio <= 0:
                continue

            for damage_on_status, status_distribution_ratio in self.params.damage_status_distribution.items():
                if status_distribution_ratio <= 0:
                    continue

                rates: dict[StatusParameter, float] = get_status_base_rates(self.params.additional_base)

                for param, rate in self.print_effects.items():
                    rates[param.to_status] += rate

                effective_rate = multiply_items(
                    rate for param, rate in rates.items()
                    if (
                            damage_type in param.applicable_damage_types and
                            damage_on_status in param.applicable_damage_on_status and
                            param not in (StatusParameter.CRT_RATE, StatusParameter.CRT_DAMAGE)
                    )
                )
                crt_rate = rates[StatusParameter.CRT_RATE]
                cdmg_boost_rate = rates[StatusParameter.CRT_DAMAGE]

                effectivenesses.append(Effectiveness(
                    base=effective_rate * distribution_ratio * status_distribution_ratio,
                    crt_rate=crt_rate,
                    cdmg_boost_rate=cdmg_boost_rate
                ))

        return sum(effectivenesses, start=Effectiveness(base=0, crt_rate=0, cdmg_boost_rate=0))

    def report_effectiveness(self):
        wp_names = " / ".join(wp.name for wp in self.prints)
        wp_effects = " / ".join(
            f"{param.name}: {rate}"
            for param, rate in sorted(self.print_effects.items(), key=lambda item: item[0].name)
        )

        print(
            f"Prints: {wp_names}\n"
            f"Effects: {wp_effects}\n"
            f"Effectiveness: "
            f"{self.effectiveness.rate_incl_crt:.5f}"
        )
