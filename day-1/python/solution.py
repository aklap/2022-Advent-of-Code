with open('../inputs/input.txt', 'r') as f:
    loads = [load.split("\n") for load in f.read().strip().split("\n\n")]
    calories_per_elf = [sum([int(cals) for cals in load]) for load in loads]
    biggest_caloric_load = sorted(calories_per_elf)[-1]
    top_three_caloric_loads = sum(sorted(calories_per_elf)[-3:])
    print("The largest load was {:,} calories.".format(biggest_caloric_load))
    print("The top 3 largest loads were: {:,}.".format(top_three_caloric_loads))
