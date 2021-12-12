def build_digit(digit_data):
    # digit_data = {8: "abcdef", 4: "defg", etc...}
     
    segments = {0:"", 1:"", 2:"",3:"",4:"",5:"",6:"",7:""}

    # gcbe = 4
    # fdgacbe = 8

def load_data(filename):
    with open(filename) as data_file:        
        data = []
        for line in data_file:
            p,o = line.strip().split("|")
            data.append({"pattern":p, "output": o})
        return data

def find_easy_digits(data):
    # 1 4 7 8
    # 2 4 3 7
    count = 0
    for display in data:
        output = display["output"].split(" ")
        for o in output:
            if len(o) in [2,4,3,7]:
                count += 1
    return count

data = load_data("data.txt")
print(find_easy_digits(data))