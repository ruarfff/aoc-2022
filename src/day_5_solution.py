def build_stacks(stack_lines: list[str], num_stacks: int):
    stacks = []
    for i in range(0, num_stacks):
        stacks.append([])

    for line in reversed(stack_lines):
        stacks_index = 0
        for i in range(1, len(line), 4):
            if line[i].strip():
                stacks[stacks_index].append(line[i])

            stacks_index += 1

    return stacks


def get_instructions_for_line(line: str):
    words = line.split(" ")
    how_many = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5])

    return how_many, from_stack, to_stack


def crate_mover_9000(line: str, stacks: list[list[str]]):
    how_many, from_stack, to_stack = get_instructions_for_line(line)

    for i in range(0, how_many):
        stacks[to_stack - 1].append(stacks[from_stack - 1].pop())

    return stacks


def crate_mover_9001(line: str, stacks: list[list[str]]):
    how_many, from_stack, to_stack = get_instructions_for_line(line)

    to_move = []
    for i in range(0, how_many):
        to_move.insert(0, stacks[from_stack - 1].pop())

    stacks[to_stack - 1] = stacks[to_stack - 1] + to_move

    return stacks


def process_input(file: str):
    num_stacks = 0
    index = 0
    lines = []
    with open(file) as f:
        lines = f.readlines()
        stack_lines = []
        stacks = []

        for line in lines:
            index += 1
            current_line = line.rstrip("\n")

            stack_lines.append(current_line)
            # End of building stacks indicated by empty line
            if not line.strip():
                num_stacks = int(
                    [
                        section
                        for section in stack_lines[-2].split(" ")
                        if section.isdigit()
                    ][-1]
                )
                stacks = build_stacks(stack_lines[:-2], num_stacks)
                break
    instructions = lines[index:]

    return stacks, instructions


def get_crate_on_top(file: str, stack_processor):
    stacks, instructions = process_input(file)
    for line in instructions:
        stacks = stack_processor(line, stacks)

    stack_tops = ""
    for stack in stacks:
        if len(stack) > 0:
            stack_tops += stack.pop()

    return stack_tops
