from src.day_4_solution import (
    count_contains_in_file,
    count_overlaps_in_file,
)


def test_pair_contains_in_file():
    assert count_contains_in_file("inputs/day_4_test_input.txt") == 2


def test_pair_overlaps_in_file():
    assert count_overlaps_in_file("inputs/day_4_test_input.txt") == 4
