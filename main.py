from src.day_1_solution import most_cals, top_3_cals
from src.day_2_solution import total_score_from_input, total_score_with_new_strategy
from src.day_3_solution import get_sum_item_priorities, get_sum_badges_priorities

if __name__ == "__main__":
    print("**** Day 1 ****")
    print(most_cals("inputs/day_1_input.txt"))
    print(top_3_cals("inputs/day_1_input.txt"))

    print("**** Day 2 ****")
    print(total_score_from_input("inputs/day_2_input.txt"))
    print(total_score_with_new_strategy("inputs/day_2_input.txt"))

    print("**** Day 3 ****")
    print(get_sum_item_priorities("inputs/day_3_input.txt"))
    print(get_sum_badges_priorities("inputs/day_3_input.txt"))
