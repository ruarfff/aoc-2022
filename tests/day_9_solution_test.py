def build_movements(file):
    movements = []
    with open(file=file) as f:
        lines = f.readlines()
        for line in lines:
            motions = line.strip().split(" ")
            movements.append((motions[0], int(motions[1])))
    return movements


def move_tail(head, tail):
    directions = [x - y for x, y in zip(head, tail)]

    if abs(directions[0]) > 1 or abs(directions[1]) > 1:
        tail[:] = [
            x + (1 if y >= 1 else -1 if y <= -1 else 0)
            for x, y in zip(tail, directions)
        ]


def move_knots(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    old_x, old_y = tail

    if (abs(x_diff) == 2) and (abs(y_diff) == 2):
        tail[0] += x_diff // 2
        tail[1] += y_diff // 2
    else:
        if abs(x_diff) == 2:
            tail[0] += x_diff // 2
            tail[1] = head[1]
        elif abs(y_diff) == 2:
            tail[1] += y_diff // 2
            tail[0] = head[0]

    new_x, new_y = tail
    return (new_x != old_x) or (new_y != old_y)


def get_visited(file, size):
    movements = build_movements(file=file)
    rope = []
    for _ in range(0, size):
        rope.append([0, 0])

    visits = set()
    head = rope[0]
    tail = rope[-1]
    visits.add(str(tail))

    for movement in movements:
        direction = movement[0][0]
        distance = movement[1]
        for n in range(int(distance)):
            if direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            elif direction == "R":
                head[0] += 1
            else:
                head[0] -= 1
            moved = True
            for n in range(1, len(rope)):
                if moved:
                    moved = move_knots(rope[n - 1], rope[n])
            if moved:
                visits.add(str(rope[-1]))

    return len(visits)


def test_get_visited():
    assert get_visited("inputs/day_9_test_input.txt", 2) == 13


def test_get_visited_2():
    assert get_visited("inputs/day_9_test_input2.txt", 10) == 36


def test_get_visited_real_input():
    assert get_visited("inputs/day_9_input.txt", 2) == 5513


def test_get_visited_real_input2():
    assert get_visited("inputs/day_9_input.txt", 10) == 2427


def test_get_visited_3():
    assert get_visited("inputs/day_9_test_input.txt", 10) == 1
