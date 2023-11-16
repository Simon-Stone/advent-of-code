from dataclasses import dataclass
from itertools import product


@dataclass
class Ingredient:
    name: str = ""
    capacity: int = 0
    durability: int = 0
    flavor: int = 0
    texture: int = 0
    calories: int = 0

    def from_string(self, s):
        self.name, properties = s.split(": ")
        for property in properties.split(", "):
            name, value = property.split(" ")
            setattr(self, name, int(value))
        return self


@dataclass
class Cookie:
    ingredients: list[(int, Ingredient)]

    def get_calories(self):
        calories = 0
        for amount, ingredient in self.ingredients:
            calories += amount * ingredient.calories
        return calories

    def get_score(self):
        capacity_score = 0
        durability_score = 0
        flavor_score = 0
        texture_score = 0
        for amount, ingredient in self.ingredients:
            capacity_score += amount * ingredient.capacity
            durability_score += amount * ingredient.durability
            flavor_score += amount * ingredient.flavor
            texture_score += amount * ingredient.texture

        if any(
            [
                capacity_score < 0,
                durability_score < 0,
                flavor_score < 0,
                texture_score < 0,
            ]
        ):
            return 0
        return capacity_score * durability_score * flavor_score * texture_score


def part_01(ingredients):
    n_ingredients = len(ingredients)
    amount = dict()
    best_score = 0
    best_cookie = None
    for tsps in product(range(101), repeat=n_ingredients):
        if sum(tsps) != 100:
            continue
        for idx, ingredient in enumerate(ingredients):
            amount[ingredient.name] = tsps[idx]
        c = Cookie(
            ingredients=[
                (amount[ingredient.name], ingredient) for ingredient in ingredients
            ]
        )
        if (score := c.get_score()) > best_score:
            best_score = score
            best_cookie = c

    return best_cookie, best_score


def part_02(ingredients):
    n_ingredients = len(ingredients)
    amount = dict()
    best_score = 0
    best_cookie = None
    for tsps in product(range(101), repeat=n_ingredients):
        if sum(tsps) != 100:
            continue
        for idx, ingredient in enumerate(ingredients):
            amount[ingredient.name] = tsps[idx]
        c = Cookie(
            ingredients=[
                (amount[ingredient.name], ingredient) for ingredient in ingredients
            ]
        )
        if c.get_calories() != 500:
            continue

        if (score := c.get_score()) > best_score:
            best_score = score
            best_cookie = c

    return best_cookie, best_score


if __name__ == "__main__":
    with open("./2015/day-15/input.txt") as f:
        ingredients = [Ingredient().from_string(line) for line in f.readlines()]
    print(part_01(ingredients))
    print(part_02(ingredients))
