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
        if self.power_level == 9:
            self.is_flashing = True
            self.power_level = 0
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


data = load_data("test.txt")
print(data[0][0])

octo = create_octopuses(data)
octo[(1, 1)].display()
