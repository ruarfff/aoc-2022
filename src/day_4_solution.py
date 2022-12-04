def parse_pairs(pairs):
    return (
        tuple(int(section) for section in pairs[0].split("-")),
        tuple(int(section) for section in pairs[1].split("-")),
    )


def get_pairs_from_file(file: str):
    pairs = []
    with open(file) as f:
        # Convert to a list of tuples of ints
        pairs = [
            tuple(s for s in line.rstrip("\n").split(",")) for line in f.readlines()
        ]
    return pairs


def is_contained(pair1, pair2):
    return (
        pair1[0] >= pair2[0]
        and pair1[1] <= pair2[1]
        or pair2[0] >= pair1[0]
        and pair2[1] <= pair1[1]
    )


def is_overlap(pair1, pair2):    
    return pair1[0] <= pair2[1] and pair2[0] <= pair1[1]


def count_match(pairs, match_function):
    matched = 0
    for pair in pairs:
        pair1, pair2 = parse_pairs(pair)
        if match_function(pair1=pair1, pair2=pair2):
            matched += 1
    return matched


def count_contains_in_file(file: str):
    return count_match(get_pairs_from_file(file), is_contained)


def count_overlaps_in_file(file: str):
    return count_match(get_pairs_from_file(file), is_overlap)
