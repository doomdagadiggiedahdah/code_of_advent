"""
### 19:47 -- 20:05
- another valid password thing.

line is policy and the password
- (loving split more than regex)
- NTS: this is more of a getting from stage 1 to 2 than 2 to 3. making sure I can do the problems.

TODO:
- check if letter is in password at positions
- whoops, read wrong. positions == how man ytimes included.
- get count of string

- how do?
    - misread the problem (but I did solve that first one quickly)
    - but then on the second time I forgot about the ':' that was in the letter.
        - tat was giving no results.


### 20:08 -- ### 20:16
- valid pword with new interp, now it's describing positions
- still didn't read it right, damn
- cool. got that somewhat quickly. I'm reading too fast and missing importatnt deatils.
- did recognize that I was about to fuck up a comparison and saved that. 

"""

sample = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

lines = open('02.in').read().splitlines()
# lines = sample.splitlines()

part_1 = 0
for line in lines:
    positions, letter, pword = line.split()
    start, stop = positions.split('-')
    if int(start) <= pword.count(letter[0]) <= int(stop) : 
        part_1 += 1
print(part_1)




lines = open('02.in').read().splitlines()
# lines = sample.splitlines()

part_2 = 0
for line in lines:
    positions, letter, pword = line.split()
    start, stop = positions.split('-')
    start, stop = int(start), int(stop)

    if (letter[0] in pword[start-1]) ^  (letter[0] in pword[stop-1]):
        part_2 += 1
print(part_2)

