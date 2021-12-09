import math

def load_data(filename):
    with open(filename) as data_file:
        return [int(num) for num in data_file.read().split(",")]

def calc_fuel_used(data, pos):
    fuel_used = 0
    for num in data:
        amount_to_move = 0
        if num == pos:
            continue # skip the ones that don't move
        if num > pos:
            amount_to_move = num - pos
        else:
            amount_to_move = pos - num

        for fuel_cost in range(1,amount_to_move + 1):
            fuel_used += fuel_cost
        # fuel_used += amount_to_move

    return fuel_used

data = load_data("data.txt")

data.sort()
median = math.floor(len(data) / 2)
print(data[median])
print(calc_fuel_used(data, data[median]))

possible_values = []
for num in data:
    print(num)
    possible_values.append(calc_fuel_used(data,num))

print(min(possible_values))
