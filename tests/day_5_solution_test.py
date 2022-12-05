from src.day_5_solution import get_crate_on_top, crate_mover_9000, crate_mover_9001


def test_get_crate_on_top():
    assert get_crate_on_top("inputs/day_5_test_input.txt", crate_mover_9000) == "CMZ"


def test_get_crate_on_top_real():
    assert get_crate_on_top("inputs/day_5_input.txt", crate_mover_9000) == "VRWBSFZWM"


def test_crate_mover_9001():
    assert get_crate_on_top("inputs/day_5_test_input.txt", crate_mover_9001) == "MCD"
    assert get_crate_on_top("inputs/day_5_input.txt", crate_mover_9001) == "RBTWJWMCF"
