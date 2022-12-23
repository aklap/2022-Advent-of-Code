def get_count(pairs):
    counts = {
        'subsets': 0,
        'intersections': 0,
    }

    def is_subset(a, b):
        return a.issubset(b) or b.issubset(a)

    def is_intersection(a, b):
        return not a.isdisjoint(b)

    for pair in pairs:
        [a_start, a_end], [b_start, b_end] = pair
        a = set(range(int(a_start), int(a_end) + 1))
        b = set(range(int(b_start), int(b_end) + 1))
        counts['subsets'] += (1 if is_subset(a, b) else 0)
        counts['intersections'] += (1 if is_intersection(a, b) else 0)
    return counts


with open('../inputs/input.txt', 'r') as f:
    sections = f.read().splitlines()
    pairs = [[pair.split('-') for pair in pair.split(',')] for pair in sections]
    counts = get_count(pairs)
    print("No. sections with subsets: {}".format(counts['subsets']))
    print("No. intersecting sections: {}".format(counts['intersections']))
