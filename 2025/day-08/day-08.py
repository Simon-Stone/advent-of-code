from dataclasses import dataclass
from functools import reduce
from itertools import combinations
import operator
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


@dataclass
class JunctionBox:
    pos: tuple[int, ...]

    def __hash__(self):
        return hash(self.pos)

    @classmethod
    def from_string(cls, s: str):
        return cls(pos=tuple(int(v) for v in s.split(",")))


def distance(a: JunctionBox, b: JunctionBox) -> int:
    return sum((x - y) ** 2 for x, y in zip(a.pos, b.pos))


def sort_pairs(
    junction_boxes: list[JunctionBox],
) -> list[tuple[JunctionBox, JunctionBox]]:
    pairs = [*combinations(junction_boxes, r=2)]
    distances = [distance(*pair) for pair in pairs]
    return [pairs for _, pairs in sorted(zip(distances, pairs))]


def wire_boxes(
    boxes: tuple[JunctionBox, JunctionBox], circuits: list[set[JunctionBox]]
) -> list[set[JunctionBox]]:
    a, b = boxes
    circuit_with_a = None
    circuit_with_b = None
    for circuit in circuits:
        if a in circuit:
            circuit_with_a = circuit
        if b in circuit:
            circuit_with_b = circuit
    if circuit_with_a is None and circuit_with_b is None:
        circuits.append({a, b})
    elif circuit_with_a is None and circuit_with_b is not None:
        circuit_with_b.add(a)
    elif circuit_with_a is not None and circuit_with_b is None:
        circuit_with_a.add(b)
    elif circuit_with_a != circuit_with_b:
        circuits.remove(circuit_with_b)
        circuit_with_a.update(circuit_with_b)
    return circuits


def part_1(junction_boxes: list[JunctionBox]) -> int:
    sorted_pairs = sort_pairs(junction_boxes)
    circuits: list[set[JunctionBox]] = []
    for boxes in sorted_pairs[:1000]:
        circuits = wire_boxes(boxes, circuits)
    sorted_circuits = sorted([len(circuit) for circuit in circuits], reverse=True)
    return reduce(operator.mul, sorted_circuits[:3])


def part_2(junction_boxes: list[JunctionBox]) -> int | None:
    sorted_pairs = sort_pairs(junction_boxes)
    circuits: list[set[JunctionBox]] = []
    wired_boxes: set[JunctionBox] = set()
    for boxes in sorted_pairs:
        circuits = wire_boxes(boxes, circuits)
        wired_boxes.update(boxes)
        if len(wired_boxes) == len(junction_boxes):
            return boxes[0].pos[0] * boxes[1].pos[0]
    return None


def draw_connections(junction_boxes: list[JunctionBox]):
    sorted_pairs = sort_pairs(junction_boxes)
    circuits: list[set[JunctionBox]] = []
    wired_boxes: set[JunctionBox] = set()
    connections = []  # Store the actual connections made

    for boxes in sorted_pairs:
        circuits = wire_boxes(boxes, circuits)
        wired_boxes.update(boxes)
        connections.append(boxes)  # Store this connection
        if len(wired_boxes) == len(junction_boxes):
            break

    # Create 3D plot
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection="3d")

    # Plot all junction boxes as points
    x_coords = [box.pos[0] for box in junction_boxes]
    y_coords = [box.pos[1] for box in junction_boxes]
    z_coords = [box.pos[2] for box in junction_boxes]

    ax.scatter(
        x_coords, y_coords, z_coords, c="red", s=50, alpha=0.7, label="Junction Boxes"
    )

    # Draw connections between connected junction boxes
    for box_a, box_b in connections:
        ax.plot(
            [box_a.pos[0], box_b.pos[0]],
            [box_a.pos[1], box_b.pos[1]],
            [box_a.pos[2], box_b.pos[2]],
            "b-",
            alpha=0.6,
            linewidth=1,
        )

    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_zlabel("Z Coordinate")
    ax.set_title(
        f"Junction Box Circuits\n{len(circuits)} circuits, {len(connections)} connections"
    )
    ax.legend()

    plt.tight_layout()
    plt.show()

    return circuits, connections


if __name__ == "__main__":
    with open("2025/day-08/test.txt") as f:
        junction_boxes = [JunctionBox.from_string(s) for s in f.readlines()]

    print("Part 1:", part_1(junction_boxes))
    print("Part 2:", part_2(junction_boxes))
    draw_connections(junction_boxes)
