import re
import pandas as pd


def part_01(games):
    n_red = 12
    n_green = 13
    n_blue = 14
    return (
        games.groupby(level="game")
        .max()
        .query("red <= @n_red and green <= @n_green and blue <= @n_blue")
        .index.to_series()
        .sum()
    )


def part_02(games):
    return games.groupby(level="game").max().product(axis="columns").sum()


def parse_games(lines):
    game_records = []
    for line in lines:
        game_id = int(re.match(r"Game ([0-9]+):", line).group(1))
        sets = line.strip().split(":")[1].split(";")
        for set_id, set in enumerate(sets):
            game_record = {"game": game_id, "set": set_id + 1}
            cubes = set.split(", ")
            for cube in cubes:
                n, color = cube.strip().split(" ")
                game_record[color] = int(n)
            game_records.append(game_record)
    return pd.DataFrame.from_records(game_records).set_index(["game", "set"])


if __name__ == "__main__":
    with open("./2023/day-02/input.txt") as f:
        lines = f.readlines()

    games = parse_games(lines)
    print(games)
    print(part_01(games))
    print(part_02(games))
