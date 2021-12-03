nums = []
with open("data.txt") as num_file:
    for line in num_file:
        nums.append(line.strip())

def count_bits(bit_string):
    bits = []
    for bit in bit_string:
        b = [0,0]
        if bit == "0":
            b[0] += 1
        else:
            b[1] += 1
        bits.append(b) 
    return bits

def add_bit_counts(a, b):
    if len(a) != len(b):
        raise Exception("Bad arrays in add_bit_counts()")
    sum = []
    
    for i in range(0, len(a)):
        s = [a[i][0] + b[i][0], a[i][1] + b[i][1]]
        sum.append(s)
    return sum

def calc_gamma_rate(bit_counts):
    bit_string = ""

    for bit_count in bit_counts:
        if bit_count[1] > bit_count[0]:
            bit_string += "1"
        else:
            bit_string += "0"

    return bit_string

def calc_epsilon(gamma_value):
    epsilon = ""
    # just reverse the values
    for g in gamma_value:
        if g == "0":
            epsilon += "1"
        else:
            epsilon += "0"
    return epsilon

def calc_oxygen_rating(nums):
    o2_vals = nums.copy()
    bit_pos = 0

    while len(o2_vals) > 1:
        
        total = count_bits(o2_vals[0])
        for val in o2_vals[1:]:
            bit_counts = count_bits(val)
            total = add_bit_counts(bit_counts, total)        
        
        bit_to_find = ""
        # find which value occurs most in bit_pos
        if total[bit_pos][0] > total[bit_pos][1]:
            bit_to_find = "0"
        else:
            bit_to_find = "1"

        temp_vals = []
        # loop through o2_vals and keep the ones that have the right bit in the right spot
        for val in o2_vals:
            if val[bit_pos] == bit_to_find:
                temp_vals.append(val)
        
        o2_vals = temp_vals
        bit_pos += 1        

    return int(o2_vals[0],2)

def calc_co_rating(nums):
    co_vals = nums.copy()
    bit_pos = 0

    while len(co_vals) > 1:
        total = count_bits(co_vals[0])
        for val in co_vals[1:]:
            bit_counts = count_bits(val)
            total = add_bit_counts(bit_counts, total)        
        
        bit_to_find = ""
        # find which value occurs least in bit_pos
        if total[bit_pos][0] < total[bit_pos][1] or total[bit_pos][0] == total[bit_pos][1]:
            bit_to_find = "0"
        else:
            bit_to_find = "1"

        temp_vals = []
        # loop through o2_vals and keep the ones that have the right bit in the right spot
        for val in co_vals:
            if val[bit_pos] == bit_to_find:
                temp_vals.append(val)
        
        co_vals = temp_vals
        bit_pos += 1        

    return int(co_vals[0],2)


total = count_bits(nums[0])

for num in nums[1:]:
    bits = count_bits(num)
    total = add_bit_counts(total, bits)

gamma = calc_gamma_rate(total)
epsilon = calc_epsilon(gamma)

print(int(gamma, 2) * int(epsilon, 2))
# print(calc_epsilon(calc_gamma_rate(total)))

print(calc_oxygen_rating(nums) * calc_co_rating(nums))
