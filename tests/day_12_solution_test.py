import sys

from dataclasses import dataclass, field
from itertools import product
from typing import Iterable


DAY = 12


@dataclass
class Coordinate:
    x: int
    y: int

    def distance_to(self, other: "Coordinate") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


@dataclass
class MapPoint:
    height: int
    visited: bool = False
    cost_to_reach: int = None
    previous_point: Coordinate = None


@dataclass
class HeightMap:
    start: Coordinate = None
    end: Coordinate = None
    points: list[list[MapPoint]] = field(default_factory=list)

    def reachable_points(self, origin: Coordinate) -> Iterable[Coordinate]:

        possible_moves = [
            Coordinate(x, y)
            for (x, y) in [
                (origin.x - 1, origin.y),
                (origin.x + 1, origin.y),
                (origin.x, origin.y - 1),
                (origin.x, origin.y + 1),
            ]
            if 0 <= x < len(self.points[0]) and 0 <= y < len(self.points)
        ]
        max_height = self.points[origin.y][origin.x].height + 1

        for point in possible_moves:
            if self.point_at(point).height <= max_height:
                yield point

    def point_at(self, coordinate: Coordinate):
        return self.points[coordinate.y][coordinate.x]

    def walk(self, queue: list[tuple[int, Coordinate, Coordinate]] = None) -> None:
        if not queue:
            queue = [(0, self.start, self.start)]
        cycles = 0
        while queue:
            cycles += 1
            curr_cost, curr_point, prev_point = queue.pop(0)
            if not self.point_at(curr_point).visited:
                self.point_at(curr_point).cost_to_reach = curr_cost
                self.point_at(curr_point).visited = True
                self.point_at(curr_point).previous_point = prev_point
                if curr_point == self.end:
                    break
                else:
                    curr_cost += 1
                    for next_point in self.reachable_points(curr_point):
                        queue.append((curr_cost, next_point, curr_point))
                    queue.sort(key=lambda l: l[0])
        print(f"Completed in {cycles} cycles")


def load_map(input) -> HeightMap:
    height_map = HeightMap()
    for row in input:
        height_map.points.append([])
        for point in row:
            if point == "S":
                height_map.start = Coordinate(
                    x=len(height_map.points[-1]), y=len(height_map.points) - 1
                )
                point = "a"
            elif point == "E":
                height_map.end = Coordinate(
                    x=len(height_map.points[-1]), y=len(height_map.points) - 1
                )
                point = "z"
            height_map.points[-1].append(MapPoint(height=ord(point) - ord("a")))
    return height_map


def part_1(input) -> int:
    m = load_map(input)
    m.walk()
    return m.point_at(m.end).cost_to_reach


def part_2(input) -> int:
    m = load_map(input)
    queue = []
    for (x, y) in product(range(len(m.points[0])), range(len(m.points))):
        coord = Coordinate(x, y)
        if m.point_at(coord).height == 0:
            queue.append((0, coord, coord))
    m.walk(queue=queue)
    return m.point_at(m.end).cost_to_reach


def test_get_shorted_path():
    input = []
    with open("inputs/day_12_test_input.txt") as f:
        for line in f:
            input.append(line.strip())

    assert part_1(input) == 31


def test_get_shorted_path_real():
    input = []
    with open("inputs/day_12_input.txt") as f:
        for line in f:
            input.append(line.strip())

    assert part_1(input) == 339


def test_get_shorted_path_2():
    input = []
    with open("inputs/day_12_test_input.txt") as f:
        for line in f:
            input.append(line.strip())

    assert part_2(input) == 29


def test_get_shorted_path_2_real():
    input = []
    with open("inputs/day_12_input.txt") as f:
        for line in f:
            input.append(line.strip())

    assert part_2(input) == 332
