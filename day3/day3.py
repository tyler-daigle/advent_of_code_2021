nums = []
with open("test.txt") as num_file:
    for line in num_file:
        nums.append(int(line,2))

num_bits = 5
gamma_vals = []

# use bitwise AND and a mask of 2^12 to check if the bits are set
# gamma_vals[] is an array of arrays. One two element array for each bit. position 0 is for 
# counting the zero values and position 1 is for counting the 1 values.

# setup the aray
for i in range(0, num_bits ):
    gamma_vals.append([0,0])

for num in nums:
    mask = 2 ** (num_bits- 1) # reset the mask each time

    for i in range(0, num_bits): # check each bit using the mask
        if num & mask != 0: # if the value is anything other than 0 the bit was set
            gamma_vals[i][1] += 1
        else: # we get zero so the bit was not set
            gamma_vals[i][0] += 1
        mask = mask >> 1 # right shift to check the next bit

val = 0
pos = 0
for bit in gamma_vals[::-1]:
    if bit[1] > bit[0]: # if more 1s than 0s set the bit on
        val += 2 ** pos
    pos += 1

gamma = val
# epsilon = val ^ 0b1111_1111_1111
epsilon = val ^ 0b11111

print(gamma)
print(epsilon)
print(gamma * epsilon)
print(gamma_vals)

# for part 2 use gamma as the mask?
# mask = 0b1000_0000_0000
mask = 0b10000

oxygen_nums = nums.copy()
curr_nums = oxygen_nums
mask_to_use = gamma

for bit in range(0, num_bits):
    # print('{0:05b}'.format(mask))
    temp_nums = []
    find = 0    
    if gamma_vals[bit][1] > gamma_vals[bit][0]:
        # looking for 1 because the bit is set
        find = 1
    else:
        find = 0    

    for num_index in range(0, len(curr_nums)):
        if find == 1:
            if curr_nums[num_index] & mask: # if bit is set to 1
                print("Found 1",'{0:05b}'.format(mask), bin(curr_nums[num_index]))
                temp_nums.append(curr_nums[num_index])
        else: # looking for 0
            if not curr_nums[num_index] & mask:  # if bit is set to 0
                print("Found 0",'{0:05b}'.format(mask), bin(curr_nums[num_index]))
                temp_nums.append(curr_nums[num_index])
    mask = mask >> 1
    curr_nums = temp_nums
    if len(temp_nums) == 1:
        print(temp_nums)
    # print(len(oxygen_nums))
    
    #find the missing index from nums_to_remove
    # for n in nums_to_remove:
    #     print(n)
    #     oxygen_nums.pop(n)

# 223 <--- using gamma as mask_to_use
# 3886 <--- using epsilon as mask_to_use

# print(len(nums_to_remove))
print("what")
for num in curr_nums:
    print('{0:012b}'.format(num))
# print(curr_nums)
# print(oxygen_nums)