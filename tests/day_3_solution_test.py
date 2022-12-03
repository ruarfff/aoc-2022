from src.day_3_solution import get_sum_item_priorities, get_sum_badges_priorities


def test_item_priorities_sum_():
    assert get_sum_item_priorities("inputs/day_3_test_input.txt") == 157


def test_item_priorities_sum_with_real_input():
    assert get_sum_item_priorities("inputs/day_3_input.txt") == 7795


def test_sum_badges_priorities():
    assert get_sum_badges_priorities("inputs/day_3_test_input.txt") == 70
