import networkx as nx
import re
from itertools import pairwise, permutations


def make_tuple(line):
    m = re.match(r"([A-Za-z]*?) to ([A-Za-z]*?) = ([0-9]*)", line)
    return m.group(1), m.group(2), int(m.group(3))


def get_stops(edges):
    stops = set()
    for edge in edges:
        stops.add(edge[0])
        stops.add(edge[1])
    return stops


def part01(edges):
    G = nx.Graph()

    G.add_weighted_edges_from(edges)

    stops = get_stops(edges)

    shortest_trip = None
    for possible_route in permutations(stops):
        distance = 0
        for a, b in pairwise(possible_route):
            distance += G.get_edge_data(a, b)["weight"]
        if not shortest_trip or distance < shortest_trip:
            shortest_trip = distance

    return shortest_trip


def part02(edges):
    G = nx.Graph()

    G.add_weighted_edges_from(edges)

    stops = get_stops(edges)

    longest_trip = None
    for possible_route in permutations(stops):
        distance = 0
        for a, b in pairwise(possible_route):
            distance += G.get_edge_data(a, b)["weight"]
        if not longest_trip or distance > longest_trip:
            longest_trip = distance

    return longest_trip


if __name__ == "__main__":
    with open("2015/day-09/input.txt") as f:
        edges = [make_tuple(line) for line in f.readlines()]
    print(part01(edges))
    print(part02(edges))
