import pandas as pd
from tqdm import tqdm


def seed_to_location(seed):
    return humidity_to_location[
        temperature_to_humidity[
            light_to_temperature[
                water_to_light[
                    fertilizer_to_water[soil_to_fertilizer[seed_to_soil[int(seed)]]]
                ]
            ]
        ]
    ]


def location_to_seed(location):
    return seed_to_soil.reverse(
        soil_to_fertilizer.reverse(
            fertilizer_to_water.reverse(
                water_to_light.reverse(
                    light_to_temperature.reverse(
                        temperature_to_humidity.reverse(
                            humidity_to_location.reverse(location)
                        )
                    )
                )
            )
        )
    )


def has_seed(seed, seeds):
    for (
        seed_start,
        n_seeds,
    ) in zip(seeds[::2], seeds[1::2]):
        if seed_start <= seed < seed_start + n_seeds:
            return True
    return False


def part_01(seeds):
    return min([seed_to_location(seed) for seed in seeds])


def part_02(seeds):
    min_location_threshold = humidity_to_location.ranges.dest_start.min()
    candidates = humidity_to_location.reverse(min_location_threshold)

    return candidates


class AlmanacMap:
    def __init__(self, ranges) -> None:
        records = []

        for r in ranges:
            record = dict()
            record["dest_start"], record["source_start"], record["n"] = map(int, r)
            record["source_end"] = record["source_start"] + record["n"]
            record["dest_end"] = record["dest_start"] + record["n"]
            records.append(record)
        self.ranges = pd.DataFrame.from_records(records).sort_values("dest_start")

    def __getitem__(self, key):
        range = self.ranges.query("source_start <= @key < source_end")
        if range.empty:
            return key
        return (range["dest_start"] + key - range["source_start"]).values[0]

    def reverse(self, key):
        range = self.ranges.query("dest_start<= @key < dest_end")
        if range.empty:
            return key
        return (range["source_start"] + key - range["dest_start"]).values[0]


if __name__ == "__main__":
    with open("./2023/day-05/input.txt") as f:
        almanac = f.read()
    seeds, *maps = almanac.split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))

    seed_to_soil = AlmanacMap(map(str.split, maps[0].split(":")[1].strip().split("\n")))
    soil_to_fertilizer = AlmanacMap(
        map(str.split, maps[1].split(":")[1].strip().split("\n"))
    )

    fertilizer_to_water = AlmanacMap(
        map(str.split, maps[2].split(":")[1].strip().split("\n"))
    )
    water_to_light = AlmanacMap(
        map(str.split, maps[3].split(":")[1].strip().split("\n"))
    )
    light_to_temperature = AlmanacMap(
        map(str.split, maps[4].split(":")[1].strip().split("\n"))
    )
    temperature_to_humidity = AlmanacMap(
        map(str.split, maps[5].split(":")[1].strip().split("\n"))
    )
    humidity_to_location = AlmanacMap(
        map(str.split, maps[6].split(":")[1].strip().split("\n"))
    )
    print(part_01(seeds))
    print(part_02(seeds))
