### 00:10
## which pairs are fully contained...



# .2345678.  2-8
# ..34567..  3-7
# .....6...  6-6
# ...456...  4-6
# these two contain the other.

# for each line, split by ,
# could take one pair, for each number see if in range of other pair, if yes, try with other number
# would need to reverse as well.
# return number of contained pairs.
# will need granular access
### 00:15
# another lesson, don't even read the probelm description; go to where they tell you the problem. lol


## test if a number is within a range

def is_in_range(left, right):
    left = list(map(int, left))
    right = list(map(int, right))
    # print(left,right)

    if right[0] <= (left[0] or left[1]) <= right[1]: # just swapped or for and for the first assignment
        # print("first")
        return 1
    elif left[0] <= (right[0] or right[1]) <= left[1]:
        # print("second")
        return 1
    else:
        return 0

with open('04input.txt', 'r') as f:
    pairs = f.readlines()
# rucks = [i.strip() for i in rucks]
sample = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

total = 0
lst = sample.splitlines()
for line in pairs:
    pairs = line.split(",")
    left, right = pairs[0].split('-'), pairs[1].split('-') # there's a cleaner way, I just don't know it. yet.
    total += is_in_range(left, right)
print(f"first test: {total}")


# how many overlapping assignments


## thoughts:
# regex to split, right? or maybe not. 
### 00:32
# feel like I'm trying to do things perfectly. not right now. progress is what I'm looking for.
# getting a few things wrong.
# [5, 7] [7, 9] wrong
# [2, 6] [4, 8] wrong; 
# so why do they happen? 
### 00:51
# it's that value comparison, I remember this being tricky in the past too.
# that's cool, reading this I had no clue how I'd figure it out.
### 00:55
# and done. recognized that problem quickly.

## data structuring, and then operations.
# if it's mostly those two things, then they're both important.
#     a1,a2 = map(int,a.split("-")): 
        ## nice, this will split the characters, and then turn to ints in one line. nice.
## alt: s1,e1,s2,e2 = [int(x) for x in [s1,e1,s2,e2]]
    ## getting each value by itself still, though I prefer the map example.
## "destructuring"; someone else said the same thing. could even say that the zip example from 03.py is destructuring. Neat.
    ## but this re-emphasizes the idea I mentioned of (lol) data (de)structuring, and then operations.
    ## so getting familiar with the basics of those will help. cool.