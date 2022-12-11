def get_inputs(file):
    lines = []
    with open(file, "r") as f:
        lines = f.readlines()
    return [
        [pair[0], int(pair[1]) if len(pair) == 2 else None]
        for pair in [line.rstrip().split(" ") for line in lines]
    ]


cycle_points = set([20, 60, 100, 140, 180, 220])


def get_signal_strength(ops):
    X = 1
    total = 0
    cycles = 0
    ops_index = 0
    wait = 0
    while True:
        cycles += 1
        if cycles in cycle_points:
            total += X * cycles

        if ops[ops_index][0] == "noop":
            ops_index += 1
        elif ops[ops_index][0] == "addx":
            if wait == 0:
                wait = 1
            else:
                wait -= 1
                if wait == 0:
                    X += ops[ops_index][1]
                    ops_index += 1

        if ops_index == len(ops):
            break
    return total


def build_crt_screen():
    screen = []
    for i in range(0, 6):
        screen.append([])
        for _ in range(0, 40):
            screen[i].append(".")
    return screen


def print_screen(screen):
    for row in screen:
        print("".join(row))


def draw_image_on_screen(ops, screen):
    X = 1
    total = 0
    cycles = 0
    ops_index = 0
    wait = 0
    screen_row = 0
    while True:
        screen_index = cycles % 40
        if cycles >= 40 and screen_index == 0:
            screen_row += 1
        cycles += 1

        if X - 1 <= screen_index <= X + 1:
            screen[screen_row][screen_index] = "#"

        if ops[ops_index][0] == "noop":
            ops_index += 1
        elif ops[ops_index][0] == "addx":
            if wait == 0:
                wait = 1
            else:
                wait -= 1
                if wait == 0:
                    X += ops[ops_index][1]
                    ops_index += 1

        if ops_index == len(ops):
            break

    return screen


def main():
    print(get_signal_strength(get_inputs("inputs/day_10_input.txt")))

    screen = build_crt_screen()

    print_screen(draw_image_on_screen(get_inputs("inputs/day_10_input.txt"), screen))


if __name__ == "__main__":
    main()
