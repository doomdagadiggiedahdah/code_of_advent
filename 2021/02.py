"""
### 15:21 -- (15:40:14) 
"What do you get if you multiply your final horizontal position by your final depth?"
- get the final hor pos and final depth, mul
- parse input for directions, and then update state

- I had trouble with the match/case setup. 
the match statement was before expecting `action`; changing it to action.split() gave the right format.

### 15:41 -- (15:50:47) 
part two: same question pos x depth
- interpret input dif
- track aim
- that took longer than I thought it would.

- I saw zero as the answer, broke apart the mult and saw one answer was 0
- I think I hadn't included the instruction to update it.
- but also, I had been giving `aim += int(aim)` instead of `aim += int(step)`
- I'm happy about the troubleshooting thoughts I had.
- also had the insight to start writing things down when I didn't know what was going on.
    - maybe that's what openAI trained o1 to do.

"""

actions = open('02.in').read().splitlines()
horizontal_pos = 0
depth = 0

for action in actions:
    match action.split():
        case 'forward', step: horizontal_pos += int(step)
        case 'down', step: depth += int(step)
        case 'up', step: depth -= int(step)
print(f"First answer: {horizontal_pos * depth}")

## pt 2
horizontal_pos = 0
depth = 0
aim = 0

for action in actions:
    match action.split():
        case 'forward', step: horizontal_pos += int(step); depth += (aim * int(step))
        case 'down', step: aim += int(step)
        case 'up', step: aim -= int(step)
print(f"Second answer: {horizontal_pos * depth}")

"""
- not getting anything 
- (broke apart final answer to see depth has NO num)
"""