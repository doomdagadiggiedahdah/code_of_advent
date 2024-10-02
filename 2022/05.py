### (10 min so far) 01:41
# goal: which crate will end up on top of each stack
# reminded of soething (zip?) that "turns cols into row, rows into cols"
# destructuring...the starting imgae? ok, easy.
# crates are moved one at a time


## interpret instructions
    ## num_move; fr to: strip all but digits, those are args now
    ## "one at a time"
## move_boxes()


## rotate to better strucutre.
## I think destructuring will be the hardest here.
## one thing I could do is regex for the 
## hmmm.
## idk. how would I do the very first thing?

## get the indexes of all numbers
## move that 

## wow, way more beautiful: https://www.reddit.com/r/adventofcode/comments/zd1hqy/comment/iz089dp/
## jesus this has taken a long time ### 02:31; about an hour.
## I'm really enjoying this process though.

import numpy as np

sample = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

drawing, instructions = sample.split("\n\n")
# with open('04input.txt', 'r') as f:
#     pairs = f.read().spl
drawing, instructions = open('05input.txt', 'r').read().split("\n\n")

lines = list(drawing.splitlines())
lines = [list(i) for i in lines]
matrix = np.rot90(lines, -1, (0,1))

operate_on_me = [''.join(item).strip() for item in matrix if item[0].isdigit()] # this is close enough
# numbers_only = [''.join(item) for item in matrix if item[0].isdigit()] # this is close enough
# operate_on_me = [item[1:] for item in numbers_only] # finaly got it. but at what cost.

# now what. needto process the instructions. jesus. over an hour for destructuring. maybe I needed it.
# for i in operate_on_me:
#     print(i)
# print()

instructions = instructions.splitlines()
for line in instructions:

    num_move, from_col, to_col = [int(s) for s in line.split() if s.isdigit()] # ya boi is leraning
    give_to = operate_on_me[to_col-1] ### give to

    for length in range(num_move):
        take_me = operate_on_me[from_col-1][-1]
        operate_on_me[to_col-1] += take_me
        operate_on_me[from_col-1] = operate_on_me[from_col-1][:-1]

    # for i in operate_on_me:
    #     print(i)
    # print()
    # print()

print(''.join([item[-1][0] for item in operate_on_me]))

# now what. how do I move one? let's print the cols first
# I've got the thing to move, now need to move it.
# couple things: need to remove RH space from the strings. done
# I want to remove a string, save that, then add it. 
# find the char, add to given, take from taken
# just get the last digits of each 
### 03:57 holy shit dude. first try. yikes. that's cool. also, I'm tired.