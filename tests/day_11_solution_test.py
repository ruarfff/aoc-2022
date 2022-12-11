import operator
from math import prod

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}


def parse_monkey_business(input_file):
    lines = []
    monkeys = []
    with open(input_file) as f:
        lines = f.readlines()

    monkey_index = 0
    monkey = {}
    for line in lines:
        parts = line.strip().split(":")
        if len(parts) == 1:
            monkey_index += 1
            continue

        first_part = parts[0]
        second_part = parts[1]

        if first_part.startswith("Monkey"):
            monkey = {}
            monkeys.append(monkey)
        elif first_part == "Starting items":
            monkeys[monkey_index]["items"] = [
                int(item) for item in second_part.split(",")
            ]
        elif first_part == "Operation":
            monkeys[monkey_index]["operation"] = second_part.split("=")[1].split(" ")[
                -2:
            ]
            if monkeys[monkey_index]["operation"][1] != "old":
                monkeys[monkey_index]["operation"][1] = int(
                    monkeys[monkey_index]["operation"][1]
                )
        elif first_part == "Test":
            monkeys[monkey_index]["test"] = int(second_part.split(" ")[-1])
        elif first_part == "If true":
            monkeys[monkey_index]["if_true"] = second_part.split(" ")[-1]
        elif first_part == "If false":
            monkeys[monkey_index]["if_false"] = second_part.split(" ")[-1]

    return monkeys


def calculate_monkey_business(input_file, turns, do_calm=False):
    monkeys = parse_monkey_business(input_file)

    inspections = {}

    cap = prod(monkey["test"] for monkey in monkeys)

    for _ in range(turns):
        i = 0

        for monkey in monkeys:
            monkey_key = f"Monkey-{i}"
            i += 1

            while monkey["items"]:
                test_val = monkey["test"]
                inspections[monkey_key] = inspections.get(monkey_key, 0) + 1
                item = monkey["items"][0]
                value = monkey["operation"][1]
                if value == "old":
                    value = item
                worry_level = ops[monkey["operation"][0]](item, value)
                if do_calm:
                    worry_level //= 3
                else:
                    worry_level = worry_level % cap

                monkey["items"][0] = worry_level

                throw_to = (
                    int(monkey["if_true"])
                    if worry_level % test_val == 0
                    else int(monkey["if_false"])
                )
                monkeys[throw_to]["items"].append(monkey["items"].pop(0))

    inspection_list = sorted(inspections.values())
    return inspection_list[-1] * inspection_list[-2]


def test_calculate_monkey_business():
    assert calculate_monkey_business("inputs/day_11_test_input.txt", 20, True) == 10605


def test_calculate_monkey_business_real():
    assert calculate_monkey_business("inputs/day_11_input.txt", 20, True) == 88208


def test_calculate_monkey_business_big():
    assert (
        calculate_monkey_business("inputs/day_11_test_input.txt", 10000) == 2713310158
    )


def test_calculate_monkey_business_big_real():
    assert calculate_monkey_business("inputs/day_11_input.txt", 10000) == 21115867968
