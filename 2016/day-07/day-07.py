from dataclasses import dataclass
import re
from typing_extensions import Self


@dataclass
class IP:
    supernet: list[str]
    hypernet: list[str]

    @classmethod
    def from_string(cls, s: str) -> Self:
        hypernet = re.findall(pattern=r"\[(.*?)\]", string=s)
        supernet = re.sub(pattern=r"\[.*?\]", repl="|", string=s).split("|")
        return cls(supernet=supernet, hypernet=hypernet)


def contains_abba(s: str) -> bool:
    return re.search(pattern=r"(.)(?!\1)(.)\2\1", string=s) is not None


def find_aba(s: str) -> list[str]:
    matches = re.finditer(pattern=r"(?=((.)(?!\2)(.)\2))", string=s)
    return [match.group(1) for match in matches]


def supports_ssl(ip: IP) -> bool:
    for supernet in ip.supernet:
        abas = find_aba(supernet)
        for aba in abas:
            for hypernet in ip.hypernet:
                if aba[1] + aba[0] + aba[1] in hypernet:
                    return True
    return False


def part_01(ips: list[IP]) -> int:
    count = 0
    for ip in ips:
        if any(contains_abba(hypernet) for hypernet in ip.hypernet):
            continue
        if any(contains_abba(supernet) for supernet in ip.supernet):
            count += 1
    return count


def part_02(ips: list[IP]) -> int:
    return sum([supports_ssl(ip) for ip in ips])


if __name__ == "__main__":
    with open("2016/day-07/input.txt") as f:
        ips = [IP.from_string(line.strip()) for line in f.readlines()]

    print(part_01(ips))
    print(part_02(ips))
