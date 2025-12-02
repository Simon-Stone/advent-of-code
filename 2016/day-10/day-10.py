from dataclasses import dataclass, field
import re
from typing_extensions import Self
from collections import defaultdict

OUTPUTS: defaultdict[int, int] = defaultdict(int)


@dataclass
class Bot:
    values: list[int] = field(default_factory=list)
    low_to: Self | None | int = None
    high_to: Self | None | int = None

    def add_value(self, x: int) -> None:
        self.values.append(x)
        if len(self.values) == 2:
            self.activate()

    def activate(self):
        if isinstance(self.low_to, Bot):
            self.low_to.add_value(min(self.values))
        elif isinstance(self.low_to, int):
            OUTPUTS[self.low_to] = min(self.values)
        elif self.low_to is None:
            pass

        if isinstance(self.high_to, Bot):
            self.high_to.add_value(max(self.values))
        elif isinstance(self.high_to, int):
            OUTPUTS[self.high_to] = max(self.values)
        elif self.high_to is None:
            pass


def find_bot(bots: dict[int, Bot], x: int, y: int) -> int | None:
    for bot_idx in bots:
        if x in bots[bot_idx].values and y in bots[bot_idx].values:
            return bot_idx
    return None


def process_instructions(instructions: list[str]) -> defaultdict[int, Bot]:
    bots: defaultdict[int, Bot] = defaultdict(Bot)
    for instruction in instructions:
        match = re.search(r"value ([0-9]+) goes to bot ([0-9]+)", instruction)
        if match:
            bot_idx = int(match.group(2))
            value = int(match.group(1))
            if (bot := bots.get(bot_idx)) is not None:
                bot.add_value(value)
            else:
                bots[bot_idx] = Bot()
                bots[bot_idx].add_value(value)
        match = re.search(
            r"bot ([0-9]+) gives low to (bot|output) ([0-9]+) and high to (bot|output) ([0-9]+)",
            instruction,
        )
        if match:
            bot_idx = int(match.group(1))
            low_target = match.group(2)
            low_idx = int(match.group(3))
            bots[bot_idx].low_to = bots[low_idx] if low_target == "bot" else low_idx
            high_target = match.group(4)
            high_idx = int(match.group(5))
            bots[bot_idx].high_to = bots[high_idx] if high_target == "bot" else high_idx
    return bots


def part_01(instructions: list[str]):
    bots = process_instructions(instructions)
    return find_bot(bots, 61, 17)


def part_02(instructions: list[str]):
    _ = process_instructions(instructions)
    return OUTPUTS[0] * OUTPUTS[1] * OUTPUTS[2]


if __name__ == "__main__":
    with open("2016/day-10/input.txt") as f:
        instructions = f.read().split("\n")
    print(part_01(sorted(instructions)))
    print(part_02(sorted(instructions)))
