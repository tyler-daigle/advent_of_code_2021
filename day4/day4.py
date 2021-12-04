BOARD_WIDTH = 5
BOARD_HEIGHT = 5

class Card:
    
    def __init__(self):
        self.rows = []        

    def __str__(self):
        s = ""
        for row in self.rows:
            for num in row:
                s += "{0} ".format(num["value"])                
            s += "\n"

        return s

    def add_row(self, row):
        self.rows.append([{"value" :int(n), "marked":False} for n in row])        

    def find(self, num):
        for row in range(0, len(self.rows)):            
            for col in range(0, len(self.rows[row])):                
                if self.rows[row][col]["value"] == num:
                    return (row, col)
        return (-1,-1)

    def mark(self, row, col):
        self.rows[row][col]["marked"] = True

    def find_and_mark(self, num):
        row, col = self.find(num)
        if row != -1:
            self.mark(row,col)
            return True
        else:
            return False
            
    def unmark(self, row, col):
        self.rows[row][col]["marked"] = False        

    def check_if_marked(self, row, col):
        return self.rows[row][col]["marked"]        

    def check_for_winner(self):
        row_count = [x * 0 for x in range(0, BOARD_HEIGHT)]
        col_count = [x * 0 for x in range(0, BOARD_WIDTH)]

        # if row_count or col_count for any values == 5 then there is a winner
        curr_row = 0

        for rows in self.rows:
            curr_col = 0
            for col in rows:
                if col["marked"] == True:
                    row_count[curr_row] += 1
                    col_count[curr_col] += 1
                curr_col += 1
            curr_row += 1
               
        return BOARD_HEIGHT in row_count or BOARD_WIDTH in col_count
        
    def calc_sum_unmarked(self):
        sum = 0

        for row in self.rows:
            for col in row:
                if col["marked"] == False:
                    sum += col["value"]
        return sum

def load_data(filename, height = BOARD_HEIGHT):
    nums = None
    cards = []
    
    with open(filename) as data_file:
        # first line is the number list
        nums = [int(n) for n in data_file.readline().strip().split(",")]
        data_file.readline() # remove first blank line
        card = Card()

        for line in data_file:
            if line.strip() == "":
                # blank line add card to cards[] and start new card
                cards.append(card)
                card = Card()                
                continue
    
            card.add_row(line.split())

        cards.append(card)
    return [nums, cards]

nums, cards = load_data("test.txt")

winner = False
card_num = 0
last_num = 0
for num in nums:    
    if winner:
        break
    # play the number
    for card in cards:
        card.find_and_mark(num)

    # then check for winner
    card_num = 0
    for card in cards:        
        if card.check_for_winner():
            winner = True
        else:
            card_num += 1

    last_num = num
        
print(card_num, "Wins with", last_num)
print(cards[card_num].calc_sum_unmarked() * last_num)


#     print(card)


# curr_card = cards[0]
# curr_card.mark(0,0)
# curr_card.mark(1,0)
# curr_card.mark(2,0)
# curr_card.mark(3,0)
# curr_card.mark(4,0)
# result = curr_card.check_for_winner()
# print(curr_card.check_if_marked(0,0))
# curr_card.find_and_mark(23)
# print(curr_card.check_if_marked(0,0))
# print(result)

    