def parse_map(input):
    lines = [line.strip("\n") for line in input]
    max_len = max([len(line) for line in lines]) - 1
    print(max_len)
    for i in range(len(lines)):
        lines[i] += " " * (max_len - len(lines[i]))
    return lines


def parse_instructions(input):
    instructions = []
    direction = "R"
    current_number = ""

    for i in range(len(input)):
        c = input[i]
        if c.isalpha() or i == len(input) - 1:
            instructions.append((direction, int(current_number)))
            current_number = ""
            direction = c
        else:
            current_number += c
    return instructions


def follow_instructions(map, instructions, debug=False):
    directions = ["U", "R", "D", "L"]
    facing_value = {"U": 3, "R": 0, "D": 1, "L": 2}

    current_direction = directions[0]
    current_x = 0
    current_y = 0

    for i in range(len(map[0])):
        if map[0][i] == ".":
            current_x = i
            break

    for instruction in instructions:
        direction = instruction[0]
        steps = instruction[1]

        if direction == "R":
            current_direction = directions[
                (directions.index(current_direction) + 1) % 4
            ]
        elif direction == "L":
            current_direction = directions[
                (directions.index(current_direction) - 1) % 4
            ]

        for s in range(steps):
            # print(f"Current direction: {current_direction}")
            # print(f"Current x: {current_x}")
            # print(f"Current y: {current_y}")
            if current_direction == "U":
                next_y = current_y - 1
                if next_y < 0:
                    next_y = len(map) - 1
                if map[next_y][current_x] == ".":
                    current_y = next_y
                elif map[next_y][current_x] == " ":
                    scan_y = next_y
                    while map[scan_y][current_x] == " ":
                        scan_y -= 1
                        if scan_y < 0:
                            scan_y = len(map) - 1
                    if map[scan_y][current_x] == ".":
                        current_y = scan_y
            elif current_direction == "R":
                next_x = current_x + 1
                if next_x >= len(map[current_y]):
                    next_x = 0
                if map[current_y][next_x] == ".":
                    current_x = next_x
                elif map[current_y][next_x] == " ":
                    scan_x = next_x
                    while map[current_y][scan_x] == " ":
                        scan_x += 1
                        if scan_x >= len(map[current_y]):
                            scan_x = 0
                    if map[current_y][scan_x] == ".":
                        current_x = scan_x
            elif current_direction == "D":
                next_y = current_y + 1
                if next_y >= len(map):
                    next_y = 0
                if map[next_y][current_x] == ".":
                    current_y = next_y
                elif map[next_y][current_x] == " ":
                    scan_y = next_y
                    while map[scan_y][current_x] == " ":
                        scan_y += 1
                        if scan_y >= len(map):
                            scan_y = 0
                    if map[scan_y][current_x] == ".":
                        current_y = scan_y
            elif current_direction == "L":
                next_x = current_x - 1
                if next_x < 0:
                    next_x = len(map[current_y]) - 1
                if map[current_y][next_x] == ".":
                    current_x = next_x
                elif map[current_y][next_x] == " ":
                    scan_x = next_x
                    while map[current_y][scan_x] == " ":
                        scan_x -= 1
                        if scan_x < 0:
                            scan_x = len(map[current_y]) - 1
                    if map[current_y][scan_x] == ".":
                        current_x = scan_x

    row = current_y + 1
    col = current_x + 1
    print(f"Row: {row}, Col: {col}, Facing val: {facing_value[current_direction]}")

    return (1000 * row) + (4 * col) + facing_value[current_direction]


def get_final_password_part1(input_file, debug=False):
    with open(input_file) as f:
        lines = f.readlines()

    map = parse_map(lines[:-2])

    instructions = parse_instructions(lines[-1])

    if debug:
        # Print out the grid
        for row in map:
            print(row)

        print(instructions)

    return follow_instructions(map, instructions, debug)


def construct_cube(map, size=50):
    cube = []
    row = 0

    for row in range(0, len(map), size):
        for col in range(0, len(map[row]), size):
            if map[row][col] == " ":
                continue
            face = []
            for i in range(size):
                face.append([c for c in map[row + i][col : col + size]])
            cube.append(face)
    return cube


def get_final_password_part2(input_file, cube_size=50, debug=False):
    with open(input_file) as f:
        lines = f.readlines()

    cube = construct_cube(parse_map(lines[:-2]), cube_size)
    # print the cube
    for face in cube:
        for row in face:
            print(row)
        print()

    directions = ["U", "R", "D", "L"]
    facing_value = {"U": 3, "R": 0, "D": 1, "L": 2}

    current_direction = directions[0]
    current_face = 0
    current_x = 0
    current_y = 0

    return 0


def test_get_final_password():
    assert get_final_password_part1("inputs/day_22_test_input.txt") == 6032


def test_get_final_password_real():
    assert get_final_password_part1("inputs/day_22_input.txt") == 65368


def test_get_final_password_part2():
    assert get_final_password_part2("inputs/day_22_test_input.txt", 4) == 5031


def test_get_final_password_part2_real():
    assert get_final_password_part2("inputs/day_22_input.txt") == 1985
