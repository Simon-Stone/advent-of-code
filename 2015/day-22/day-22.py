from itertools import product
from tqdm import tqdm

spell_choices = [
    "Shield",
    "Poison",
    "Recharge",
    "Magic Missile",
    "Drain",
]

tested_strategies = set()


def no_dupes(strategy):
    for idx, spell in enumerate(strategy):
        if spell in ["Shield", "Poison"]:
            if any(s == spell for s in strategy[idx + 1 : idx + 3]):
                return False
        if spell == "Recharge":
            if any(s == spell for s in strategy[idx + 1 : idx + 2]):
                return False
    return True


MAX_TURNS = 11
strategies = [
    strategy
    for strategy in product(spell_choices, repeat=MAX_TURNS)
    if no_dupes(strategy)
]
min_mana_cost = 10e6
for turns in tqdm(strategies, total=len(strategies)):
    is_untested = True
    for tested_strategy in tested_strategies:
        if tested_strategy == turns[: len(tested_strategy)]:
            is_untested = False
            break
    if not is_untested:
        continue

    boss_hp = 55
    boss_damage = 8
    player_hp = 50
    player_mana = 500
    mana_spent = 0
    n_turn = 0
    shield_timer = 0
    shield_value = 0
    poison_timer = 0
    recharge_timer = 0

    while boss_hp > 0 and player_hp > 0 and n_turn < len(turns):
        """--- Player turn ---"""
        player_hp -= 1
        if player_hp <= 0:
            tested_strategies.add(turns[: n_turn + 1])
            break

        if shield_timer > 0:
            shield_value = 7
            shield_timer -= 1

        if poison_timer > 0:
            boss_hp -= 3
            if boss_hp <= 0:
                min_mana_cost = min(mana_spent, min_mana_cost)
                tested_strategies.add(turns[: n_turn + 1])
                break
            poison_timer -= 1

        if recharge_timer > 0:
            player_mana += 101
            recharge_timer -= 1

        if turns[n_turn] == "Magic Missile":
            player_mana -= 53
            if player_mana < 0:
                tested_strategies.add(turns[: n_turn + 1])
                break
            boss_hp -= 4
            mana_spent += 53

        elif turns[n_turn] == "Drain":
            player_mana -= 73
            if player_mana < 0:
                tested_strategies.add(turns[: n_turn + 1])
                break
            boss_hp -= 2
            player_hp += 2
            mana_spent += 73

        elif turns[n_turn] == "Shield":
            player_mana -= 113
            if player_mana < 0 or shield_timer > 0:
                tested_strategies.add(turns[: n_turn + 1])
                break
            shield_timer = 6
            mana_spent += 113

        elif turns[n_turn] == "Poison":
            player_mana -= 173
            if player_mana < 0 or poison_timer > 0:
                tested_strategies.add(turns[: n_turn + 1])
                break
            poison_timer = 6
            mana_spent += 173

        elif turns[n_turn] == "Recharge":
            player_mana -= 229
            if player_mana < 0 or recharge_timer > 0:
                tested_strategies.add(turns[: n_turn + 1])
                break
            recharge_timer = 5
            mana_spent += 229

        if boss_hp <= 0:
            min_mana_cost = min(mana_spent, min_mana_cost)
            tested_strategies.add(turns[: n_turn + 1])
            break

        """--- Boss turn ---"""
        if shield_timer > 0:
            shield_value = 7
            shield_timer -= 1

        if poison_timer > 0:
            boss_hp -= 3
            if boss_hp <= 0:
                min_mana_cost = min(mana_spent, min_mana_cost)
                tested_strategies.add(turns[: n_turn + 1])
                break
            poison_timer -= 1

        if recharge_timer > 0:
            player_mana += 101
            recharge_timer -= 1

        player_hp -= boss_damage - shield_value

        if mana_spent > min_mana_cost:
            tested_strategies.add(turns[: n_turn + 1])
            break
        n_turn += 1

print(min_mana_cost)
