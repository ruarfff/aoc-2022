# A,X = Rock
# B,Y = Paper
# C,Z = Scissors
# rock > scissors
# paper > rock
# scissors > paper
move_map = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}


move_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def total_score_for_guide(strategy_guides):

    score = 0

    for move in strategy_guides:
        col_1 = move[0]
        col_2 = move[1]

        score += move_scores[col_2]

        if move_map[col_1] == col_2:
            # draw
            score += 3
        elif (
            col_1 == "C"
            and col_2 == "X"
            or col_1 == "A"
            and col_2 == "Y"
            or col_1 == "B"
            and col_2 == "Z"
        ):
            # win
            score += 6
        else:
            # lose
            score += 0

    return score


def convert_moves_new_strategy(strategy_guides):
    def determine_move(move):
        col_1 = move[0]
        col_2 = move[1]
        choice = ""

        if col_2 == "X":
            if col_1 == "A":
                choice = "Z"
            elif col_1 == "B":
                choice = "X"
            elif col_1 == "C":
                choice = "Y"
        elif col_2 == "Y":
            choice = move_map[col_1]
        elif col_2 == "Z":
            if col_1 == "A":
                choice = "Y"
            elif col_1 == "B":
                choice = "Z"
            elif col_1 == "C":
                choice = "X"
        return (col_1, choice)

    return [determine_move(move) for move in strategy_guides]


# Read input from file with 2 characters per line and assign to tuples in a list
def get_strategy_guides(file: str):
    strategy_guides = []
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            strategy_guides.append((line[0], line[2]))
    return strategy_guides


def total_score_from_input(file: str):
    strategy_guides = get_strategy_guides(file)
    return total_score_for_guide(strategy_guides)


def total_score_with_new_strategy(file: str):
    strategy_guides = get_strategy_guides(file)
    return total_score_for_guide(convert_moves_new_strategy(strategy_guides))
