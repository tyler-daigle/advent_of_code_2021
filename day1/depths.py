# data = open("data.txt")

# curr = int(data.readline())
# inc = 0

# for line in data:
#     depth = int(line)
#     if depth > curr:
#         inc += 1
#     curr = depth
    
# print(inc)


def get_depths():
    data = ""
    with open("data.txt") as data_file:
        data = data_file.read()
    return [int(n) for n in data.split("\n")]
    
depths = get_depths()

curr = depths[0]
inc = 0
for d in depths[1:]:
    if d > curr:
        inc += 1
    curr = d
print(inc)

inc = 0
start = 0
end = 2
curr = sum(depths[start:end + 1])
for n in range(0, len(depths)):
    start += 1
    end += 1
    d = sum(depths[start:end+1])
    print(d)
    if d > curr:
        inc += 1
    curr = d
    
print(inc)

# print(curr)
# add up first three values
