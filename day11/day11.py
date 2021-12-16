# go through each item in the grid
# create an Octopus object for each item
# add the item to a has table indexed by it (row, col)
# add references to its neighbors (create them and add to the hash table)
# go to the next item in the list - see if it is already in the has table
# if it is then just setup references to its neighbors

class Octopus:
    def __init__(self, power_level, position):
        self.power_level = power_level
        self.position = position
        self.is_flashing = False

    def life_cycle(self):
        if self.power_level == 9:
            self.is_flashing = True
            self.power_level = 0
        else:
            self.power_level += 1


def load_data(filename):
    rows = []
    with open(filename) as data_file:
        for line in data_file:
            rows.append([int(num) for num in line.strip()])
    return rows


data = load_data("test.txt")
print(data[0][0])
