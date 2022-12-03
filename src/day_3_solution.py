import string

all_chars = list(string.ascii_letters)


priorities = dict((all_chars[i], i + 1) for i in range(0, len(all_chars)))

print(priorities)


def get_sum_item_priorities(file: str):
    sum_priorities = 0

    with open(file) as file:
        while line := file.readline().rstrip():
            n = len(line)
            compartment_1 = set()
            for i in range(0, n // 2):
                compartment_1.add(line[i])

            for i in range(n // 2, n):
                if line[i] in compartment_1:
                    sum_priorities += priorities[line[i]]
                    break

    return sum_priorities


def get_sum_badges_priorities(file: str):
    sum_priorities = 0
    elf_count = 0
    first_elf = set()
    first_2_elves_shared = set()

    with open(file) as file:
        while line := file.readline().rstrip():
            elf_count += 1
            for char in line:
                if elf_count == 1:
                    first_elf.add(char)
                elif elf_count == 2:
                    if char in first_elf:
                        first_2_elves_shared.add(char)
                elif char in first_2_elves_shared:
                    sum_priorities += priorities[char]
                    break
            if elf_count == 3:
                elf_count = 0
                first_elf = set()
                first_2_elves_shared = set()

    return sum_priorities
