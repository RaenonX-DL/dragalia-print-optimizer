from dataclasses import dataclass, field

from dlprintopt.enums import PrintParameter, get_status_base_rates, StatusParameter, DamageType
from dlprintopt.utils import is_prints_valid, get_print_effectiveness, multiply_items

from .calcparams import CalcParams
from .effectiveness import Effectiveness
from .wp import Wyrmprint

__all__ = ("PrintComp",)


@dataclass
class PrintComp:
    prints: list[Wyrmprint]

    print_effects: dict[PrintParameter, float] = field(init=False)

    def __post_init__(self):
        if not is_prints_valid(self.prints):
            raise ValueError("Invalid print comp")

        self.print_effects = get_print_effectiveness(self.prints)

    def get_prints_effectiveness(self, params: CalcParams) -> Effectiveness:
        effectivenesses: list[Effectiveness] = []

        for damage_type, distribution_ratio in params.damage_distribution.items():
            rates: dict[StatusParameter, float] = get_status_base_rates(params.additional_base)

            for param, rate in self.print_effects.items():
                rates[param.to_status] += rate

            effective_rate = multiply_items(
                rate for param, rate in rates.items()
                if (
                        damage_type in param.applicable_damage_types and
                        param not in (StatusParameter.CRT_RATE, StatusParameter.CRT_DAMAGE)
                )
            )
            crt_rate = rates[StatusParameter.CRT_RATE]
            cdmg_boost_rate = rates[StatusParameter.CRT_DAMAGE]

            effectivenesses.append(Effectiveness(
                base=effective_rate * distribution_ratio, crt_rate=crt_rate, cdmg_boost_rate=cdmg_boost_rate
            ))

        return sum(effectivenesses, start=Effectiveness(base=0, crt_rate=0, cdmg_boost_rate=0))

    def report_effectiveness(self, params: CalcParams):
        wp_names = " / ".join(wp.name for wp in self.prints)
        wp_effects = " / ".join(f"{param.name}: {rate}" for param, rate in self.print_effects.items())

        print(
            f"Prints: {wp_names}\n"
            f"Effects: {wp_effects}\n"
            f"Effectiveness: "
            f"{self.get_prints_effectiveness(params).rate_incl_crt:.5f}"
        )
