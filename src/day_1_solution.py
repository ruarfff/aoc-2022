def get_cals(file: str):
    cals = []
    blocks = []
    with open(file) as f:
        f.seek(0)
        blocks = f.read().split("\n\n")
    for line in blocks:
        elf = line.splitlines()
        foods = []
        for food in elf:
            foods.append(int(food))
        cals.append(sum(foods))

    return cals


def most_cals(file: str):
    return sorted(get_cals(file))[-1]


def top_3_cals(file: str):
    return sum(sorted(get_cals(file), reverse=True)[:3])
