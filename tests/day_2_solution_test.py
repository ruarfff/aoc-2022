from src.day_2_solution import (
    total_score_for_guide,
    total_score_from_input,
    total_score_with_new_strategy,
)


def test_total_score_for_guide():
    strategy_guide = [("A", "Y"), ("B", "X"), ("C", "Z")]
    assert total_score_for_guide(strategy_guide) == 15


def test_total_score_from_input():
    assert total_score_from_input("inputs/day_2_test_input.txt") == 15


def test_total_score_for_new_strategy():
    assert total_score_with_new_strategy("inputs/day_2_test_input.txt") == 12
