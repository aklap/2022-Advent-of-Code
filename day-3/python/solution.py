import string


def get_priority_score(item):
    PRIORITIES_SCORE = dict(zip(string.ascii_lowercase \
                + string.ascii_uppercase, list(range(1, 53))))
    return PRIORITIES_SCORE[item]


def get_sum(rucksacks):
    sum = 0
    for rucksack in rucksacks:
        midpt = int(len(rucksack) / 2)
        left = rucksack[0:midpt]
        right = rucksack[midpt:]
        misplaced_item = set(left).intersection(set(right)).pop()
        sum += get_priority_score(misplaced_item)
    return sum


def get_group_sum(badges, size):
    sum = 0
    for i in range(0, len(badges), size):
        badge = set(badges[i]).intersection(set(badges[i+1])).intersection(set(badges[i+2])).pop()
        sum += get_priority_score(badge)
    return sum


def display(sum):
    print("Priorities sum is {:,}.".format(sum))


with open('../inputs/input.txt', 'r') as f:
    lines = f.read().splitlines()
    display(get_sum(lines))
    display(get_group_sum(lines, 3))