### 10:34
# this was annoying last night, let's try again.
# I think I misunderstood
# "first position where the four most cent chars are all different."

### 10:44
# ok, got it.
# so take the slice, see if four unique values, if yes return index + 4, else continue
### 10:51. amazing what understanding the problem does.
### 10:55. got the next one too. I want to abstract this though.


samples ="""\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""
# def get_index(line, l_ind, offset):
#     if len(set(line[l_ind:l_ind + offset])) == offset:
#         print(l_ind+offset)
#         return 1
#     else:
#          return 0


def get_index(line, l_ind, offset):
   return print(l_ind+offset) if len(set(line[l_ind:l_ind + offset])) == offset else 0

lines = samples.splitlines()
lines = open('06.txt').read().splitlines()

for line in lines:
    for l_ind in range(len(line)):
        if get_index(line, l_ind, 4) != 0:
            break

for line in lines:
    for l_ind in range(len(line)):
        if get_index(line, l_ind, 14) != 0:
            break