from itertools import product, combinations

from dlprintopt.enums import PrintType, PrintParameter, StatusParameter, DamageType, Affinity, DamageOnStatus
from dlprintopt.model import CalcParams, Wyrmprint, PrintComp, Effect

prints_r5: dict[str, Wyrmprint] = {
    "SD_40": Wyrmprint(
        name="SD +40%", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.4)]
    ),
    "ATK_20": Wyrmprint(
        name="ATK +20%", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2)]
    ),
    "CRT_14": Wyrmprint(
        name="CRT +14%", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.14)],
    ),
    "CDMG_22": Wyrmprint(
        name="CDMG +22%", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.22)]
    ),
    # "PUN_30": Wyrmprint(
    #     name="異常特攻 +30%", type=PrintType.R5,
    #     effects=[Effect(effect_param=PrintParameter.PUNISHER_POISON, effect_rate=0.3)]
    # ),
    "PUN_25": Wyrmprint(
        name="異常特攻 +25%", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.PUNISHER_SHADOWBLIGHT, effect_rate=0.25)]
    ),
    "DDMG_18": Wyrmprint(
        name="龍化傷害 +18%", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.18)]
    ),
    "BK_30": Wyrmprint(
        name="BK 特攻 +30%", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.PUNISHER_BK, effect_rate=0.3)]
    ),
    "FS_50": Wyrmprint(
        name="FS +50%", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=0.5)],
        affinity_type=Affinity.FS
    ),
}

prints_r4: dict[str, Wyrmprint] = {
    "SD_20": Wyrmprint(
        name="SD +20%", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2)],
        affinity_type=Affinity.ATK,
    ),
    "SD_20_2": Wyrmprint(
        name="SD +20%", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2)]
    ),
    "CRT_12": Wyrmprint(
        name="CRT +12%", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.12)],
    ),
    "FS_40": Wyrmprint(
        name="FS +40%", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=0.4)],
        affinity_type=Affinity.FS
    ),
    "CDMG_17": Wyrmprint(
        name="CDMG +17%", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.17)]
    ),
    "DDMG_14": Wyrmprint(
        name="龍化傷害 +14%", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.14)]
    ),
    "BK_25": Wyrmprint(
        name="BK 特攻 +25%", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.PUNISHER_BK, effect_rate=0.25)]
    ),
}

prints_sindom: dict[str, Wyrmprint] = {
    "SINDOM_SD_20": Wyrmprint(
        name="SD +20%", type=PrintType.SINDOM,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2)],
    ),
    "SINDOM_SD_20_2": Wyrmprint(
        name="SD +20%", type=PrintType.SINDOM,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2)],
    ),
    "SINDOM_CRT_4": Wyrmprint(
        name="CRT +4%", type=PrintType.SINDOM,
        effects=[Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.04)],
        affinity_type=Affinity.FS,
    ),
    "SINDOM_SWD": Wyrmprint(
        name="聖劍讚歌", type=PrintType.SINDOM,
        effects=[Effect(enables_affinity=Affinity.ATK)]
    ),
    "SINDOM_FS": Wyrmprint(
        name="銳槍讚歌", type=PrintType.SINDOM,
        effects=[Effect(enables_affinity=Affinity.FS)]
    ),
}

prints_kaleido: dict[str, Wyrmprint] = {
    "KS_ATK": Wyrmprint(
        name="ATK +20%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
        ],
    ),
    "KS_ATK_FS": Wyrmprint(
        name="ATK +20%、FS -50%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
            Effect(effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=-0.5),
        ],
    ),
    "KS_ATK_CDMG": Wyrmprint(
        name="ATK +20% / CDMG +15%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
            Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15),
        ],
    ),
    "KS_SD": Wyrmprint(
        name="SD +40%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.4),
        ],
    ),
    "KS_SD_ATK": Wyrmprint(
        name="SD +40% / ATK +20%、FS -50%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.4),
            Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
            Effect(effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=-0.5),
        ],
    ),
    "KS_SD_CDMG": Wyrmprint(
        name="SD +40% / CDMG +15%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.4),
            Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15),
        ],
    ),
    "KS_CRT_ATK": Wyrmprint(
        name="CRT +15% / ATK +20%、FS -50%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.15),
            Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
            Effect(effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=-0.5),
        ],
    ),
    "KS_CRT": Wyrmprint(
        name="CRT +15%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.15),
        ],
    ),
    "KS_CRT_CDMG": Wyrmprint(
        name="CRT +15% / CDMG +15%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.15),
            Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15),
        ],
    ),
    "KS_CDMG": Wyrmprint(
        name="CDMG +15%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15),
        ],
    ),
    "KS_FS": Wyrmprint(
        name="FS 傷害 +50%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=0.5),
        ],
    ),
    "KS_FS_CDMG": Wyrmprint(
        name="FS 傷害 +50% / CDMG +15%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=0.5),
            Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15),
        ],
    ),
    "KS_DDMG": Wyrmprint(
        name="龍化傷害 +18%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.18),
        ],
    ),
    "KS_DDMG_ATK": Wyrmprint(
        name="龍化傷害 +18% / ATK +20%、FS -50%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.18),
            Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
            Effect(effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=-0.5),
        ],
    ),
    "KS_DDMG_CDMG": Wyrmprint(
        name="龍化傷害 +18% / CDMG +15%", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.18),
            Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15),
        ],
    ),
    "KS_NONE": Wyrmprint(
        name="(無)", type=PrintType.KALEIDO,
        effects=[],
    ),
}

additional_base: dict[StatusParameter, float] = {
    StatusParameter.ATK_PASSIVE: 1.0,
    StatusParameter.CRT_RATE: 0.02
}

damage_distribution: dict[DamageType, float] = {
    DamageType.NORMAL: 0,
    DamageType.SKILL: 0.4,
    DamageType.FS: 0.4,
    DamageType.DRAGON: 0.14,
    DamageType.DRAGON_SKILL: 0.06,
}

damage_status_distribution: dict[DamageOnStatus, float] = {
    DamageOnStatus.PRE_OD: 0,
    DamageOnStatus.OD: 0.6,
    DamageOnStatus.BK: 0.4
}

params: CalcParams = CalcParams(
    additional_base=additional_base,
    damage_distribution=damage_distribution,
    damage_status_distribution=damage_status_distribution,
)


def check_by_count(counts: list[tuple[int, int, int, int]]):
    for r5_count, r4_count, ks_count, sindom_count in counts:
        print(f"--- R5 x {r5_count} / R4 x {r4_count} / KS x {ks_count} / Sindom x {sindom_count} ---")
        r5_combinations = combinations(prints_r5.values(), r5_count)
        r4_combinations = combinations(prints_r4.values(), r4_count)
        kaleido_combinations = combinations(prints_kaleido.values(), ks_count)
        sindom_combinations = combinations(prints_sindom.values(), sindom_count)

        comps = [
            PrintComp(prints=r5_picked + r4_picked + kaleido_picked + sindom_picked, params=params)
            for r5_picked, r4_picked, kaleido_picked, sindom_picked
            in product(r5_combinations, r4_combinations, kaleido_combinations, sindom_combinations)
        ]

        most_effective_comp = None
        for idx, comp in enumerate(comps):
            current_comp = comp

            if idx % 1000 == 0:
                print(f"{idx} / {len(comps)}")

            if not most_effective_comp or current_comp.effectiveness > most_effective_comp.effectiveness:
                most_effective_comp = comp
                continue

        if not most_effective_comp:
            print("Empty print comp")
            continue

        most_effective_comp.report_effectiveness()
        print()


def get_most_effective_of_ks(r5_count: int, r4_count: int, sindom_count: int, ks_print: Wyrmprint) -> PrintComp:
    r5_combinations = combinations(prints_r5.values(), r5_count)
    r4_combinations = combinations(prints_r4.values(), r4_count)
    sindom_combinations = combinations(prints_sindom.values(), sindom_count)

    comps = [
        PrintComp(prints=r5_picked + r4_picked + (ks_print,) + sindom_picked, params=params)
        for r5_picked, r4_picked, sindom_picked
        in product(r5_combinations, r4_combinations, sindom_combinations)
    ]

    most_effective_comp = None
    for comp in comps:
        current_comp = comp

        if not most_effective_comp or current_comp.effectiveness > most_effective_comp.effectiveness:
            most_effective_comp = comp
            continue

    if not most_effective_comp:
        raise ValueError("Empty print comp")

    return most_effective_comp


def check_all_count():
    check_by_count([
        (r5_count, r4_count, ks_count, sindom_count)
        for r5_count, r4_count, ks_count, sindom_count
        in product([1, 2, 3], [1, 2], [1], [1, 2])
    ])


def check_partial_count():
    # R5 / R4 / KS / SINDOM
    counts: list[tuple[int, int, int, int]] = [
        (3, 2, 1, 2),
        (2, 2, 1, 2),
        (3, 1, 1, 2),
    ]

    check_by_count(counts)


def check_full():
    r5_count = 3
    r4_count = 2
    ks_count = 1
    sindom_count = 2

    r5_combinations = combinations(prints_r5.values(), r5_count)
    r4_combinations = combinations(prints_r4.values(), r4_count)
    kaleido_combinations = combinations(prints_kaleido.values(), ks_count)
    sindom_combinations = combinations(prints_sindom.values(), sindom_count)

    comps = [
        PrintComp(prints=r5_picked + r4_picked + kaleido_picked + sindom_picked, params=params)
        for r5_picked, r4_picked, kaleido_picked, sindom_picked
        in product(r5_combinations, r4_combinations, kaleido_combinations, sindom_combinations)
    ]

    for idx, comp in enumerate(comps):
        if idx % 1000 == 0:
            print(f"{idx} / {len(comps)}")

        comp.load_effectiveness()

    for idx, comp in enumerate(sorted(
            comps,
            key=lambda comp: comp.effectiveness,
            reverse=True
    )):
        if idx > 50:
            break

        comp.report_effectiveness()
        print()


def check_comp_each_ks():
    counts = [
        (3, 2, 2),
        (3, 1, 2),
        (2, 2, 2),
    ]

    for r5_count, r4_count, sindom_count in counts:
        print(f"--- R5 x {r5_count} / R4 x {r4_count} / Sindom x {sindom_count} ---")

        comp_of_count = []

        for ks_print in prints_kaleido.values():
            if ks_print.name in ("KS_ATK_FS", "KS_FS", "KS_FS_CDMG"):
                continue

            comp_of_count.append((ks_print, get_most_effective_of_ks(r5_count, r4_count, sindom_count, ks_print)))

        lowest_effectiveness = next(
            comp for comp in comp_of_count if prints_kaleido["KS_NONE"] in comp[1].prints
        )[1].effectiveness.rate_incl_crt

        for ks_print, comp in sorted(comp_of_count, key=lambda item: item[1].effectiveness, reverse=True):
            wp_names = " | ".join(wp.name for wp in comp.prints if wp.type != PrintType.KALEIDO)

            effectiveness_formula = (
                f"=={comp.effectiveness.rate_incl_crt:.5f} / {lowest_effectiveness:.5f} - 100%[2f]=="
                if ks_print.effects else
                "-"
            )

            print(
                f"{ks_print.name} | "
                f"{comp.effectiveness.rate_incl_crt:.5f} | "
                f"{effectiveness_formula} | "
                f"{wp_names}"
            )

        print()
        print()


if __name__ == '__main__':
    check_comp_each_ks()
