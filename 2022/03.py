### 22:59
# ruck has two compartments meant for an item type
# list of items in each ruck; we find errors
# item type is def'd by a single up/low case letter
# The list of items for each rucksack is given as characters all on a single line
    ## each line == ruck.
### 23:04

test_input = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

sample_1 = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
"""

sample_2 = """\
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

with open('03input.txt', 'r') as f:
    rucks = f.readlines()
rucks = [i.strip() for i in rucks]

def get_prio(common):
    if common.islower():
        num = ord(common) - 96
    elif common.isupper():
        num = ord(common) - 38
    else:
        print(common)
        print("ahhhh")
    return num

# test_list = test_input.split()
total = 0
for i in rucks:
    num = 0
    ruck_size = len(i) // 2
    common = list(set(i[:ruck_size]) & set(i[ruck_size:]))[0]
    total += get_prio(common)
print(total)
    

# get size
# split each ruch
# find common
# associate with prio / add to talley
### 23:09
# ahh. getting the prio 
### 23:26 # ok, about 30 min start to finish. 

#### pt 2
### 23:27
# common between three lines

## get three rucks
    ## could split into three rows off the bat? that'd be easier.
    ## split, take every three, then combine?
## find common
## same ord thing

test = sample_1 + sample_2
# rucks = test.splitlines()

total = 0
i = iter(rucks)
groups_of_three = list(zip(i,i,i))

for i in groups_of_three:
    common = list(set(i[0]) & set(i[1]) & set(i[2]))[0]
    total += get_prio(common)
print(total)


### 23:39
# ok, zip to save the day.
# what's happening. 
# I'm getting confused.
# I'm getting different results each time. hmm.
# I'm geting everything three groups. sure.
### 00:05 ## jeeeez. you know, that felt longer than it was. 

## what was the lesson? the split lines were causing trouble.
## could've also made a function out of the sets; I think there's a way to do this with any number of variables so it's robust.