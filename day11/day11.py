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
        self.neighbors = []

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def life_cycle(self):
        if self.is_flashing:
            return

        if self.power_level > 9:
            self.power_level = 0
            self.is_flashing = True
        else:
            self.power_level += 1

    def display(self):
        print("({0}, {1})".format(self.position[0], self.position[1]))
        print("Power Level: {0}".format(self.power_level))
        print(self.neighbors)


def load_data(filename):
    rows = []
    with open(filename) as data_file:
        for line in data_file:
            rows.append([int(num) for num in line.strip()])
    return rows


def get_neighbors(pos, max_row, max_col):
    neighbors = []
    row, col = pos
    # up
    if row > 0:
        neighbors.append((row - 1, col))
        # up-left
        if col > 0:
            neighbors.append((row - 1, col - 1))
        # up-right
        if col < max_col - 1:
            neighbors.append((row - 1, col + 1))

    # down
    if row < max_row - 1:
        neighbors.append((row + 1, col))
        # down-left
        if col > 0:
            neighbors.append((row + 1, col - 1))
        # down-right
        if col < max_col - 1:
            neighbors.append((row + 1, col + 1))
    # left
    if col > 0:
        neighbors.append((row, col - 1))
    # right
    if col < max_col - 1:
        neighbors.append((row, col + 1))

    return neighbors


def create_octopuses(data):
    # data is split into rows and columns
    max_row = len(data)
    max_col = len(data[0])
    octopi = {}

    for row in range(0, max_row):
        for col in range(0, max_col):
            pos = (row, col)
            if pos not in octopi:
                octopi[pos] = Octopus(data[row][col], pos)

            neighbors = get_neighbors(pos, max_row, max_col)
            octopi[pos].set_neighbors(neighbors)

    return octopi


def print_grid(octopi, rows, cols):
    for row in range(0, rows):
        s = ""
        for col in range(0, cols):
            s += str(octopi[(row, col)].power_level)
        print(s)


data = load_data("test.txt")

octo = create_octopuses(data)
num_rows = 5
num_cols = 5
print_grid(octo, num_rows, num_cols)
for i in range(0, 2):
    for row in range(0, num_rows):
        print("Life Cycle {0}".format(i))
        for col in range(0, num_cols):
            octo[(row, col)].life_cycle()

# while something is flashing
flashers = set()
for pos, oct in octo.items():
    if oct.is_flashing:
        print("{0} is flashing".format(pos))
        flashers.add(pos)

# need to remove duplicates from flashers

for f in flashers:
    print("Flaher: ", f)

for flashing in flashers:
    # get all the neighbors of the flashing octo and execute a lifecyle on them

    # TODO: the same neighbor is being added multiple times
    neighbors = octo[flashing].neighbors

    for n in neighbors:
        octo[n].life_cycle()
        # stop the octo from flashing
        octo[n].is_flashing = False

print_grid(octo, num_rows, num_cols)

# 45654
# 51115
# 61116
# 51115
# 45654
