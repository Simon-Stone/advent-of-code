from collections import Counter
from dataclasses import dataclass
import re
from typing import Tuple


@dataclass
class Square:
    xy: Tuple[int, int]
    claim_id: str
    total_squares: int

    def __hash__(self) -> int:
        return hash(self.xy)

    def __eq__(self, value: object) -> bool:
        return self.xy == value.xy


@dataclass
class Claim:
    id: str
    from_left: int
    from_top: int
    width: int
    height: int

    def get_area(self):
        area = []
        for x in range(self.width):
            for y in range(self.height):
                area.append(
                    Square(
                        xy=(self.from_left + x, self.from_top + y),
                        claim_id=self.id,
                        total_squares=self.width * self.height,
                    )
                )
        return area

    @classmethod
    def from_string(cls, s):
        id = re.search(r"#([0-9]+)", s).group(1)
        from_left, from_top = re.search("([0-9]+),([0-9]+)", s).groups()
        width, height = re.search("([0-9]+)x([0-9]+)", s).groups()
        return cls(
            id=id,
            from_left=int(from_left),
            from_top=int(from_top),
            width=int(width),
            height=int(height),
        )


def part_01(claims):
    claimed = []
    for claim in claims:
        claimed.extend(claim.get_area())
    count = Counter(claimed)
    claimed_multiple = [c for c in set(claimed) if count[c] > 1]
    return len(claimed_multiple)


def part_02(claims):
    claimed = []
    for claim in claims:
        claimed.extend(claim.get_area())
    count = Counter(claimed)
    claimed_once = [c for c in set(claimed) if count[c] == 1]
    candidate_ids = set(c.claim_id for c in claimed_once)

    square_count = {
        candidate_id: len([c for c in claimed_once if c.claim_id == candidate_id])
        for candidate_id in candidate_ids
    }

    for claim in claims:
        if len(claim.get_area()) == square_count.get(claim.id):
            return claim.id


if __name__ == "__main__":
    with open("2018/day-03/input.txt") as f:
        claims = [Claim.from_string(line) for line in f.readlines()]

    print(part_01(claims))
    print(part_02(claims))
