def parse_card(card):
    return map(
        lambda x: set(map(int, x.split())), card.strip().split(":")[1].split("|")
    )


def part_01(cards):
    score = 0
    for card in cards:
        winners, my_numbers = parse_card(card)
        if n_winners := len(winners.intersection(my_numbers)):
            score += 2 ** (n_winners - 1)
    return score


def part_02(cards):
    n_cards = []
    n_winners = []
    for card in cards:
        n_cards.append(1)
        winners, my_numbers = parse_card(card)
        n_winners.append(len(winners.intersection(my_numbers)))
    for card_idx in range(len(n_cards)):
        for offset in range(1, n_winners[card_idx] + 1):
            n_cards[card_idx + offset] += n_cards[card_idx]
    return sum(n_cards)


if __name__ == "__main__":
    with open("./2023/day-04/input.txt") as f:
        cards = f.readlines()

    print(part_01(cards))
    print(part_02(cards))
