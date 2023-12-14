from itertools import cycle
import re
from math import lcm


def part_01(directions, nodes):
    current_node = nodes["AAA"]
    for count, direction in enumerate(cycle(directions.strip()), start=1):
        next_node = current_node[direction]
        if next_node == "ZZZ":
            return count
        current_node = nodes[next_node]


def part_02(directions, nodes):
    current_nodes = [node for name, node in nodes.items() if name.endswith("A")]
    cycles = []
    for count, direction in enumerate(cycle(directions.strip()), start=1):
        next_nodes = [node[direction] for node in current_nodes]
        finished_node = None
        for node in next_nodes:
            if node.endswith("Z"):
                finished_node = node
                cycles.append(count)
        if finished_node:
            next_nodes.pop(next_nodes.index(finished_node))
        if next_nodes:
            current_nodes = [nodes[next_node] for next_node in next_nodes]
        else:
            return lcm(*cycles)


def parse_nodes(nodes):
    n = dict()
    for node in nodes:
        current, left, right = re.findall(
            r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)", node
        )[0]
        n[current] = {"L": left, "R": right}
    return n


if __name__ == "__main__":
    with open("./2023/day-08/input.txt") as f:
        directions, _, *nodes = f.readlines()

    nodes = parse_nodes(nodes)
    print(part_01(directions, nodes))
    print(part_02(directions, nodes))
