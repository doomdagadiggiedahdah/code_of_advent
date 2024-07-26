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
#print(total)


###### Pt.1 after review #######
with open('02input.txt', 'r') as f:
    rounds = f.readlines()
winners = {"X":"C", "Y":"A", "Z":"B", "A":"Z", "B":"X", "C":"Y"}
points = {"X":1, "Y":2, "Z":3}
total = 0
for round in rounds:
    plays = round.strip().split()
    total += points[plays[1]]
    if winners[plays[1]] == plays[0]:
        total += 6
    elif winners[plays[0]] == plays[1]:
        total += 0
    else:
        total += 3
#print(total)

## wow, this is so much nicer. This is really nice.





example = """A Y
B X
C Z
"""


with open('02input.txt', 'r') as f:
    rounds = f.readlines()
#rounds = example.splitlines()
winners      = {"X":"C", "Y":"A", "Z":"B", "A":"Z", "B":"X", "C":"Y"}
ties         = {"A":"X", "B":"Y", "C":"Z"}
result_score = {"X": 0, "Y": 3, "Z": 6}
points       = {"X": 1, "Y": 2, "Z": 3}
total = 0
for round in rounds:
    plays = round.strip().split()
    total += result_score[plays[1]]
    if plays[1] == "Z":
        shape = [i for i in winners if winners[i] == plays[0]][0]
    elif plays[1] == "X":
        shape = winners[plays[0]]
    elif plays[1] == "Y":
        shape = ties[plays[0]]
    total += points[shape]
print(total)
# coooool. got this on the first try too.

# seeing that I can also just map out the options by hand. but what does that look like?
# requires takes two inputs, gives shape back. Maybe this can be informed by `winners`.
# hey, doing it without a function. coo.
# what am I confused about? Let's start 







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
# gross. that took an hour (including the reading time, but still). Let's see next round.
# I did get it the first try though.

###### PT2 ######
# I think there will be some switching. I'm told directly that I'll win, that's the given this time.
# there's something about modulo 3 with the determining shapes / winner.
# you know, I think I could muscle through this, but what I'm looking to learn is better practices. 
# There's a practice here that I don't know.
# This is what I'm talking about: https://wooledge.org/~greg/advent/2022/2a 
# real clean. Let's take notes.


## did right:
    ## split the plays into sep vars.
## did not:
    ## tried to keep typing (or something) low by not listing out all the winning combos.
        ## actually, this is diff than what I had thought; I was going to do both win and losses. Didn't think about reversing it.
## in this case, the winning matrix was easy enough that I could've listed them out manually.
## I think the generalized version wasn't so bad though.