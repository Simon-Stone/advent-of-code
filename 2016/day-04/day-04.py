from collections import Counter
from dataclasses import dataclass
import string
from typing_extensions import Self


@dataclass
class Room:
    name: str
    sector_id: int
    checksum: str

    @classmethod
    def from_string(cls, s: str) -> Self:
        s = s.strip()
        name = "-".join(s.split("-")[:-1])
        sector_id, checksum = s[-2::-1].split("-", maxsplit=1)[0][::-1].split("[")
        return cls(name=name, sector_id=int(sector_id), checksum=checksum)

    def is_valid(self) -> bool:
        count = Counter(sorted(self.name.replace("-", "")))
        most_common = "".join([c for c, _ in count.most_common(5)])
        return most_common == self.checksum

    def decrypt(self) -> str:
        return "".join([_shift_letter(c, self.sector_id) for c in self.name])


def _shift_letter(x: str, n: int) -> str:
    if x == "-":
        return " "
    return string.ascii_lowercase[
        (string.ascii_lowercase.index(x.lower()) + n) % len(string.ascii_lowercase)
    ]


def part_01(rooms: list[Room]) -> int:
    return sum(room.sector_id for room in rooms if room.is_valid())


def part_02(rooms: list[Room]):
    for room in rooms:
        if room.decrypt().strip() == "northpole object storage":
            return room.sector_id


if __name__ == "__main__":
    with open("2016/day-04/input.txt") as f:
        rooms = [Room.from_string(r) for r in f.readlines()]

    print(part_01(rooms))
    print(part_02(rooms))
