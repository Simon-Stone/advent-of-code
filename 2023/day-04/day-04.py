def part_01(cards):
    score = 0
    for card in cards:
        winners, my_numbers = map(
            lambda x: set(map(int, x.split())), card.strip().split(":")[1].split("|")
        )
        if n_winners := len(winners.intersection(my_numbers)):
            score += 2 ** (n_winners - 1)
    return score


def part_02(x):



if __name__ == "__main__":
    with open("./2023/day-04/input.txt") as f:
        cards = f.readlines()

    print(part_01(cards))
    print(part_02())
