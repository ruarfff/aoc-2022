from src.day_10_solution import get_signal_strength, get_inputs


def test_get_signal_strength():
    assert get_signal_strength(get_inputs("inputs/day_10_test_input.txt")) == 13140


def test_get_signal_strength_real():
    assert get_signal_strength(get_inputs("inputs/day_10_input.txt")) == 17840
