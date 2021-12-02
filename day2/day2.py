commands = []
with open("data.txt") as data_file:
    for data in data_file:
        commands.append(data)

class SubCommand:    
    def __init__(self, command_string):
        self.direction, self.amount = command_string.split(" ")
        self.amount = int(self.amount)
        
command_list = []

for command in commands:    
    command_list.append(SubCommand(command))

depth = 0
pos = 0
aim = 0

for command in command_list:
    if command.direction == "forward":
        pos += command.amount 
        depth += aim * command.amount
    elif command.direction == "down":
        aim += command.amount
    else: # up
        aim -= command.amount

print(depth, pos)
print(depth * pos)