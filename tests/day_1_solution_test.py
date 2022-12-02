from src.day_1_solution import most_cals, top_3_cals


def test_solution_with_test_input():
    assert most_cals("inputs/day_1_test_input.txt") == 24000


def test_top_3_cals_with_test_input():
    assert top_3_cals("inputs/day_1_test_input.txt") == 45000


def test_solution_with_input():
    assert most_cals("inputs/day_1_input.txt") == 66186


def test_top_3_cals_with_input():
    assert top_3_cals("inputs/day_1_input.txt") == 196804
