def is_overlapping(line, option=None):
    [a_start, a_end], [b_start, b_end] = line
    a = set(range(int(a_start), int(a_end)+1))
    b = set(range(int(b_start), int(b_end)+1))
    if option == 'contained':
            return a.issubset(b) or b.issubset(a)
    elif option =='intersecting':
            return not a.isdisjoint(b)


def get_count(lines, option=None):
    count = 0
    for line in lines:
        count += int(is_overlapping(line, option))
    return count


with open('../inputs/input.txt', 'r') as f:
    lines = [[pair.split('-') for pair in line.strip().split(',')] for line in f.readlines()]
    total = get_count(lines, 'contained')
    print("The number of sections that were a subset of another was {}".format(total))
    total = get_count(lines, 'intersecting')
    print("The number of sections that intersected was {}".format(total))
