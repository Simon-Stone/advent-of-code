from dataclasses import dataclass
import re
from typing_extensions import Self


@dataclass
class Marker:
    n_char: int
    n_rep: int

    @classmethod
    def from_string(cls, s: str) -> Self:
        match = re.search(r"([0-9]+)x([0-9]+)", s)
        if match:
            return cls(n_char=int(match.group(1)), n_rep=int(match.group(2)))
        raise ValueError("Could not parse string into Marker: ", s)

    def apply(self, bits: list[str]) -> str:
        bit = ""
        for _ in range(self.n_char):
            bit += bits.pop(0)
        return bit * self.n_rep


def get_marker(file: list[str]) -> Marker:
    marker_string = ""
    while True:
        marker_string += file.pop(0)
        if file[0] == ")":
            file.pop(0)
            break
    return Marker.from_string(marker_string)


def decompress(file: str) -> str:
    decompressed_file = ""
    bits = list(file)
    while bits:
        if bits[0] == "(":
            marker = get_marker(bits)
            decompressed_file += marker.apply(bits)
        else:
            decompressed_file += bits.pop(0)
    return decompressed_file


def part_01(files: list[str]) -> list[int]:
    decompressed_sizes: list[int] = []
    for file in files:
        decompressed_sizes.append(len(decompress(file)))
    return decompressed_sizes


def process_bits(bits: list[str]) -> int:
    marker = get_marker(bits)
    decompressed_size = 0
    i = 0
    while i < marker.n_char:
        if bits[0] != "(":
            decompressed_size += 1 * marker.n_rep
            bits.pop(0)
            i += 1
        else:
            decompressed_size += process_bits(bits) * marker.n_rep
            i += 5
    return decompressed_size


def part_02(files: list[str]) -> list[int]:
    decompressed_sizes: list[int] = []
    for file in files:
        bits = list(file)
        decompressed_size = 0
        while bits and bits[0] != "(":
            decompressed_size += 1
            bits.pop(0)
        if bits:
            decompressed_size += process_bits(bits)
        decompressed_sizes.append(decompressed_size)
    return decompressed_sizes


if __name__ == "__main__":
    with open("2016/day-09/test2.txt") as f:
        files = f.read().split("\n")
    # print(part_01(files))
    print(part_02(files))
