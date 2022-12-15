with open('../inputs/input.txt', 'r') as f:
    lines = f.read().strip().split("\n\n")
    loads_per_elf = [load.split("\n") for load in lines]
    calories_per_elf = [sum([int(cals) for cals in load]) for load in loads_per_elf]
    calories_per_elf.sort()
    highest_cals = calories_per_elf[-1]
    highest_three_total_cals = sum(calories_per_elf[-3:])

    print("The largest load was {:,} calories.".format(highest_cals))
    print("The top 3 largest loads were: {:,}.".format(highest_three_total_cals))