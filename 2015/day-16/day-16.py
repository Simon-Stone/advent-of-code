from dataclasses import dataclass, fields
import re


@dataclass
class Sue:
    index: int = None
    children: int = None
    cats: int = None
    samoyeds: int = None
    pomeranians: int = None
    akitas: int = None
    vizslas: int = None
    goldfish: int = None
    trees: int = None
    cars: int = None
    perfumes: int = None

    def from_string(self, s: str):
        self.index = re.match(r"Sue ([0-9]+):", s).group(1)
        _, compounds = s.split(":", maxsplit=1)
        for compound in compounds.split(", "):
            name, value = compound.split(": ")
            setattr(self, name.strip(), int(value))
        return self

    def __eq__(self, other):
        for field in fields(self):
            if field.name == "index":
                continue
            if getattr(self, field.name) is not None and getattr(
                self, field.name
            ) != getattr(other, field.name):
                return False
        return True


@dataclass
class RealSue:
    index: int = None
    children: int = None
    cats: int = None
    samoyeds: int = None
    pomeranians: int = None
    akitas: int = None
    vizslas: int = None
    goldfish: int = None
    trees: int = None
    cars: int = None
    perfumes: int = None

    def from_string(self, s: str):
        self.index = re.match(r"Sue ([0-9]+):", s).group(1)
        _, compounds = s.split(":", maxsplit=1)
        for compound in compounds.split(", "):
            name, value = compound.split(": ")
            setattr(self, name.strip(), int(value))
        return self

    def __eq__(self, other):
        for field in fields(self):
            if field.name == "index":
                continue
            a = getattr(self, field.name)
            b = getattr(other, field.name)
            if a is None:
                continue
            if field.name in ["cats", "trees"]:
                if a <= b:
                    return False
            if field.name in ["pomeranians", "goldfish"]:
                if a >= b:
                    return False
            if a != b:
                return False
        return True


def part_01(sues):
    target_sue = Sue(
        children=3,
        cats=7,
        samoyeds=2,
        pomeranians=3,
        akitas=0,
        vizslas=0,
        goldfish=5,
        trees=3,
        cars=2,
        perfumes=1,
    )
    candidates = []
    for sue in sues:
        if sue == target_sue:
            candidates.append(sue)
    return candidates


def part_02(sues):
    target_sue = RealSue(
        children=3,
        cats=7,
        samoyeds=2,
        pomeranians=3,
        akitas=0,
        vizslas=0,
        goldfish=5,
        trees=3,
        cars=2,
        perfumes=1,
    )
    candidates = []
    for sue in sues:
        if sue == target_sue:
            candidates.append(sue)
    return candidates


if __name__ == "__main__":
    with open("./2015/day-16/input.txt") as f:
        sues = [Sue().from_string(line) for line in f.readlines()]

    print(part_01(sues))

    with open("./2015/day-16/input.txt") as f:
        sues = [RealSue().from_string(line) for line in f.readlines()]
    print(part_02(sues))
