import sys

def load_data(filename):
    with open(filename) as data_file:
        return [int(num) for num in data_file.read().split(",")]

def create_histogram(data):
    histo = {}
    for d in data:
        if d in histo:
            histo[d] += 1
        else:
            histo[d] = 1
    return histo

def calc_least_fuel(histogram):
    # assume that moving the least crabs is the correct answer?
    # so that is the position that already has the most crabs
    most = 0
    crab_pos = None
    possible_pos = []

    for key, value in histogram.items():
        print(key)
        if value >= most:
            crab_pos = key
            most = value
            possible_pos.append(crab_pos)
            print(key, value)
        
    print(possible_pos)
    fuel_amounts = []
    # calc how far each crab is from that position
    for try_pos in possible_pos:
        fuel_used = 0
        crab_pos = try_pos
        for key, value in histogram.items():
            if key == crab_pos:
                continue # skip the crab that is already there
            
            pos = key
            num_crabs = value
            if pos > crab_pos:
                fuel_used += (pos - crab_pos) * num_crabs
            else:
                fuel_used += (crab_pos - pos) * num_crabs
        fuel_amounts.append(fuel_used)
    # print("Most Crabs At: ", crab_pos)
    # print("Fuel used: ", fuel_used)
    return min(fuel_amounts)

pos_data = load_data("data.txt")

print(calc_least_fuel(create_histogram(pos_data)))

