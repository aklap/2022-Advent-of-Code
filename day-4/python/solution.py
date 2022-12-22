def is_subset(a, b):
    return a.issubset(b) or b.issubset(a)


def is_intersection(a, b):
    return not a.isdisjoint(b)


def get_count(pairs):
    subset_count = 0
    intersect_count = 0
    for pair in pairs:
        [a_start, a_end], [b_start, b_end] = pair
        a = set(range(int(a_start), int(a_end) + 1))
        b = set(range(int(b_start), int(b_end) + 1))
        subset_count += (1 if is_subset(a, b) else 0)
        intersect_count += (1 if is_intersection(a, b) else 0)
    return (subset_count, intersect_count)


with open('../inputs/input.txt', 'r') as f:
    sections = f.read().splitlines()
    pairs = [[pair.split('-') for pair in pair.split(',')] for pair in sections]
    subset_count, intersect_count = get_count(pairs)
    print("Number of sections with subsets: {}".format(subset_count))
    print("Number of subsets with intersections: {}".format(intersect_count))
