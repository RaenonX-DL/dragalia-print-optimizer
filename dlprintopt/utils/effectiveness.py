from collections import Counter
from typing import TYPE_CHECKING

from dlprintopt.const import CDMG_RATE
from dlprintopt.enums import Affinity, PrintParameter
if TYPE_CHECKING:
    from dlprintopt.model import Wyrmprint

__all__ = ("get_print_effectiveness", "get_expected_crt_effectiveness")


def get_print_effectiveness(prints: list["Wyrmprint"]) -> dict[PrintParameter, float]:
    rates: dict[PrintParameter, float] = {}
    has_affinity_enabled: dict[Affinity, bool] = {
        affinity: (
                any(wp for wp in prints if wp.enables_affinity == affinity)
                and any(wp for wp in prints if wp.affinity_type == affinity)
        )
        for affinity in Affinity
    }
    affinity_counter: Counter[Affinity, int] = Counter(wp.affinity_type for wp in prints if wp.affinity_type)

    # Add print effects
    for wp in prints:
        param = wp.effect_param

        # Print may not have any effect on stats
        if param is None:
            continue

        rate = wp.effect_rate

        if param not in rates:
            rates[param] = rate
        else:
            rates[param] += rate

    # Add affinity effects (by count)
    for affinity, count in affinity_counter.items():
        effect = affinity.get_effect_at_count(count)
        if not effect:
            continue

        print_param, rate = effect
        rates[print_param] = rate

    # Add affinity effects (force-enabled)
    for affinity, is_effective in has_affinity_enabled.items():
        if not is_effective:
            continue

        print_param, rate = affinity.effect_at_max
        rates[print_param] = rate

    # Calculate max value
    ret: dict[PrintParameter, float] = {}
    for param, rate in rates.items():
        if max_value := param.max_value:
            ret[param] = min(rate, max_value)
        else:
            ret[param] = rate

    return ret


def get_expected_crt_effectiveness(crt_rate: float, cdmg_boost_rate: float) -> float:
    return 1 * (1 - crt_rate) + (CDMG_RATE + cdmg_boost_rate) * crt_rate
