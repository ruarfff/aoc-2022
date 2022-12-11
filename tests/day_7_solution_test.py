def get_dir_sizes(lines: list[str]) -> dict[str, int]:
    pwd: str = ""
    dirs: dict[str, int] = {"/": 0}

    for line in lines:
        line = line.rstrip("\n")
        if line == "$ ls":
            continue
        elif line == "$ cd /":
            pwd = "/"
        elif line == "$ cd ..":
            pwd = "/".join(pwd.split("/")[:-2]) + "/"
        elif line.startswith("$ cd"):
            pwd += line.split(" ")[-1] + "/"
        elif line.startswith("dir "):
            dirs[pwd + line.split(" ")[-1] + "/"] = 0
        else:
            dirs[pwd] += int(line.split(" ")[0])

    return {k: sum([dirs[l] for l in dirs if l.startswith(k)]) for k in dirs}


inputs = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


def process_inputs(inputs):
    dir_sizes = get_dir_sizes(lines=inputs)
    return sum([dir_sizes[d] for d in dir_sizes if dir_sizes[d] <= 100000])


def process_input_from_file(file):
    dir_sizes = {}
    with open(file) as f:
        lines = f.readlines()
        dir_sizes = get_dir_sizes(lines=lines)
    return sum([dir_sizes[d] for d in dir_sizes if dir_sizes[d] <= 100000])


def test_get_directory_sizes():
    assert process_inputs(inputs) == 95437


def test_get_directory_sizes_real_input():
    assert process_input_from_file("inputs/day_7_input.txt") == 1555642


def test_the_other_bit():
    dir_sizes = {}
    with open("inputs/day_7_input.txt") as f:
        lines = f.readlines()
        dir_sizes = get_dir_sizes(lines=lines)
        space_available = 70000000 - dir_sizes["/"]
        space_needed = 30000000 - space_available
    assert (
        min([dir_sizes[d] for d in dir_sizes if dir_sizes[d] >= space_needed])
        == 5974547
    )
