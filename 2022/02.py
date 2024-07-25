example = """A Y
B X
C Z
"""
#rounds = example.splitlines()

## excited to see this optimized 
def determine_winner(opp_act, self_act):
    opp_moves  = "ABC"
    self_moves = "XYZ"
    op_m  = opp_moves.index(opp_act) 
    slf_m = self_moves.index(self_act)
    result = op_m - slf_m
    if op_m == slf_m:
        return 3
    if result == -1 or result == 2:
        return 6
    if result == 1 or result == -2:
        return 0

with open('02input.txt', 'r') as f:
    rounds = f.readlines()
shape_score = {"X":1, "Y":2, "Z":3}
total = 0
for round in rounds:
    opponent_action, self_action = round.strip().split(" ")
    total += determine_winner(opponent_action, self_action) + shape_score[self_action]
print(total)




###########

## (2024.07.25__14.02.54) -- (15:02:14) 
# score is shape you selected + outcome of round.
# need to set up win conditions. I wonder what the efficient way to do this is.
# then take each line and add to a total.
# get the shape first.
# the win conds is really what I'm not sure about. let's get everything else.
# cool, now just the win stuff. I could write it out the hard way. Yeah sure.
# actually that's way too long. How about a tie?
# the ordering I can work with. if they're the same index, that's a tie.
# got a tie. How about a win? thinking something with modulo
# optimized the shape_score; just a dictionary. Cool to see that.
# gross. that took an hour. Let's see next round.