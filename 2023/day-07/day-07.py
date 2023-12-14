from dataclasses import dataclass, field
import enum
from functools import total_ordering
from collections import Counter
from typing import Union


@total_ordering
class Cards(str):
    order = "23456789TJQKA"

    def __eq__(self, other):
        return super.__eq__(self, other)

    def __lt__(self, other):
        for a, b in zip(self, other):
            if Cards.order.index(a) < Cards.order.index(b):
                return True
            if Cards.order.index(a) > Cards.order.index(b):
                return False
        return False


@total_ordering
class CardsWithWild(Cards):
    order = "J23456789TQKA"

    def __eq__(self, other):
        return super.__eq__(self, other)

    def __lt__(self, other):
        for a, b in zip(self, other):
            if CardsWithWild.order.index(a) < CardsWithWild.order.index(b):
                return True
            if CardsWithWild.order.index(a) > CardsWithWild.order.index(b):
                return False
        return False


@total_ordering
class HandType(enum.Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

    def __lt__(self, other):
        return self.value < other.value

    @classmethod
    def from_cards(cls, cards, with_wild=False):
        card_count = Counter(cards)

        if not with_wild or "J" not in cards:
            top_2_cards = card_count.most_common(2)
            if top_2_cards[0][1] > 3:
                return cls(top_2_cards[0][1] + 1)
            if top_2_cards[0][1] == 3 and len(top_2_cards) == 2:
                if top_2_cards[1][1] == 2:
                    return cls(4)
                return cls(3)
            if top_2_cards[0][1] == 2 and len(top_2_cards) == 2:
                if top_2_cards[1][1] == 2:
                    return cls(2)
                return cls(1)
            return cls(0)
        # With wildcards
        n_wild = card_count["J"]
        del card_count["J"]
        top_2_cards = card_count.most_common(2)

        if not top_2_cards:
            return cls(6)
        if n_wild >= 4:
            return cls(6)
        if top_2_cards[0][1] + n_wild > 3:
            return cls(min(top_2_cards[0][1] + n_wild + 1, 6))
        # Maximum one wild
        if top_2_cards[0][1] + n_wild == 3:
            if top_2_cards[1][1] == 2:
                return cls(4)
            return cls(3)
        return cls(top_2_cards[0][1] + n_wild - 1)


@total_ordering
@dataclass
class Hand:
    cards: Union[Cards, CardsWithWild]
    bid: int
    with_wild: bool = False
    type: HandType = field(init=False)

    def __post_init__(self):
        self.type = HandType.from_cards(self.cards, self.with_wild)

    def __eq__(self, other):
        return self.type == other.type and self.cards == other.cards

    def __lt__(self, other):
        if self.type == other.type:
            return self.cards < other.cards
        else:
            return self.type < other.type

    @classmethod
    def from_string(cls, s, with_wild=False):
        cards, bid = s.split()
        if with_wild:
            return cls(cards=CardsWithWild(cards), bid=int(bid), with_wild=with_wild)
        return cls(cards=Cards(cards), bid=int(bid))


def part_01(lines):
    hands = [Hand.from_string(line) for line in lines]
    return sum(rank * hand.bid for rank, hand in enumerate(sorted(hands), start=1))


def part_02(lines):
    hands = sorted([Hand.from_string(line, with_wild=True) for line in lines])
    return sum(rank * hand.bid for rank, hand in enumerate(hands, start=1))


if __name__ == "__main__":
    with open("./2023/day-07/input.txt") as f:
        lines = f.readlines()

    print(part_01(lines))
    print(part_02(lines))
