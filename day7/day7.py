import sys

def load_data(filename):
    with open(filename) as data_file:
        return [int(num) for num in data_file.read().split(",")]

def sum_data(data):
    return sum(data)

def get_highest_freq(data):
    histo = {}
    for d in data:
        if not d in histo:
            histo[d] = 1
        else:
            histo[d] += 1

    max = 0
    most_freq = None

    for key, value in histo.items():
        if value > max:
            max = value
            most_freq = key

    return most_freq

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

        for fuel_cost in range(1,amount_to_move):
            fuel_used += fuel_cost

    return fuel_used

pos_data = load_data("test.txt")
pos_freq = get_highest_freq(pos_data)

fuel_amounts = []
for pos in pos_data:
    fuel_amounts.append(calc_fuel_used(pos_data, pos))

print(min(fuel_amounts))



