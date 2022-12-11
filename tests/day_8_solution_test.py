def build_grid(file):
    grid = []
    with open(file=file) as f:
        lines = f.readlines()
        for line in lines:
            grid.append([int(n) for n in list(line.strip())])
    return grid


def get_visible_trees(file):
    grid = build_grid(file=file)

    num_visible = (len(grid[0]) * 2 + len(grid) * 2) - 4

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            current_tree = grid[i][j]
            if current_tree == 0:
                continue
            visible = False

            for k in range(j + 1, len(grid[0])):
                if grid[i][k] >= current_tree:
                    break
                elif k == len(grid[0]) - 1:
                    visible = True

            if not visible:
                for k in range(j - 1, -1, -1):
                    if grid[i][k] >= current_tree:
                        break
                    elif k == 0:
                        visible = True

            if not visible:
                for k in range(i + 1, len(grid)):
                    if grid[k][j] >= current_tree:
                        break
                    elif k == len(grid) - 1:
                        visible = True

            if not visible:
                for k in range(i - 1, -1, -1):
                    if grid[k][j] >= current_tree:
                        break
                    elif k == 0:
                        visible = True

            if visible:
                num_visible += 1

    return num_visible


def get_highest_viewing_score(file):
    grid = build_grid(file=file)
    highest_view_score = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            current_tree = grid[i][j]
            left_score = 0
            right_score = 0
            up_score = 0
            down_score = 0

            for k in range(j + 1, len(grid[0])):
                right_score += 1
                if grid[i][k] >= current_tree:
                    break

            for k in range(j - 1, -1, -1):
                left_score += 1
                if grid[i][k] >= current_tree:
                    break

            for k in range(i + 1, len(grid)):
                down_score += 1
                if grid[k][j] >= current_tree:
                    break

            for k in range(i - 1, -1, -1):
                up_score += 1
                if grid[k][j] >= current_tree:
                    break

            view_score = up_score * left_score * down_score * right_score
            if view_score > highest_view_score:
                highest_view_score = view_score

    return highest_view_score


def test_get_visible_trees():
    assert get_visible_trees("inputs/day_8_test_input.txt") == 21


def test_get_highest_viewing_score():
    assert get_highest_viewing_score("inputs/day_8_test_input.txt") == 8


def test_get_visible_trees_real_input():
    assert get_visible_trees("inputs/day_8_input.txt") == 1823


def test_get_highest_viewing_score_real_input():
    assert get_highest_viewing_score("inputs/day_8_input.txt") == 211680
