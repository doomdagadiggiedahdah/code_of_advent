"""
### 17:37
- phrase vs word
    - series of words sep by space
- how many are valid passwordS?
- no duplicate words
    - was going to say regex, but nay, I think of simpler

- each line: split by space, for each obj compare if equiv
- how do I do the comparison? for each part if 

- not doing this right. already at 10 minutes.
- alright, so what's the issue.
    - if there's a dupe, I want to quit that line.
    - also not referencing the right item at first.
- ok, getting the right lists to compare, good.
- now to get the correct comparisons
    - small test, :3 should give one password
    - I know I could put this into a nested list comp, but not now.
- what I'm confsed on is how to skip a whole line if a dupe is found.
    - what exactly is that? 
    - or count it if a whole line hasn't been tripped.
- let's spend more time on that. there's something I'm missing
    - if a 


- need to check if one string is elsewhere in the list. (oh hey, got the descruting down great. nice.)
- feel like I'm missing something.............another five min and I'm getting the answer.### 18:07
- there's prob a simpler way. what baout pop?

- thinking of removing the entries as they're tested. Janky. 
- god dammit. just saw a MUCH MUCH better way to do this. set(). trying again with taht in mind. damn.
### 18:14 -- 18:17
- hvae the lines, need to get the og set len
- didn't get it right originally....
- three minutes is more like it. dammit.

### 18:18 -- (18:32:56) 
# part 2
- # valid pass; changing the rules
    - invalid if any word's letters can be an anagram.
    - there's a sneaky way for this, I feel it.
- sort each chunk and then set? that would work.
- got the sorting, but it's a bit funky.
    - need to get the sorted back to a single string.
- cool. Got it down. the set() function really changed things. that made it all pretty great.

- glad I thought about the sneaky way to approach part 2. That was good.
- I had some issues with getting the sorted strings in the right data type. 
    - in retro, copying and trying out in the REPL would be good to try out here.
    - I remember that I had issues testing thing



the issue is that if I want to copy to REPL it's a pain in the ass
if I make adjustments in the code and I fuck it up, then it's hard to know what to go back to.
    - maybe the quick adjustment to make there is to comment out what works and then mark as SANITY
    - copy that section and then mess around with it all you want.


if set() hadn't of worked; I could've: also created another list and added 
something like this

def duh():
    check_double = []
    for i in ls:
        if i in check_double:
            return False
        check_double.append(i)
    return True

- anything else?
    - glad I recognized I could build directly off the first solution
        - just needed to sort the entries first and then go at it again.

"""

lines = open('04.in').read().splitlines()

part_1 = 0
for line in lines:
    line = line.split()
    len_before = len(line)
    len_after = len(set(line))
    if len_before == len_after:
        part_1 += 1
print(part_1)



part_2 = 0
for line in lines:
    line = line.split()
    line = [''.join(sorted(i)) for i in line]
    len_before = len(line)
    len_after = len(set(line))
    if len_before == len_after:
        part_2 += 1
print(part_2)















# leaving for public shaming
# lines = open('04.in', 'r').read().splitlines()
# part_1 = 0
# for line in lines[:3]:
#     parts = line.split()
#     for part_index in range(len(parts)):
#         # print(parts[part_index])
#         # print(parts[part_index+1:])
#         # print(part_index)
#         # print()
#         if parts[part_index] not in parts[part_index+1:]:
#             parts.pop(part_index)
#         else:
#             break
#     print("only want this once")
#     part_1 += 1
# print(part_1)