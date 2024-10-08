"""
### 15:54 -- (16:15:27) 
- "How much fuel must they spend to align to that position?"
- track position, alignment, use these to get fule

- they need to be on same hor pos.
- thinking take all crabs, find min amount of fuel needed.

- take all positions (range(min,max of in)), DONE
- compute how much fuel it'd take for each iter
- stor min in var and print

### 16:16 -- 16:47
- adjust the computation of how many fuels.
    - immediately scared of how to compute the incremental costs.
    - maybe I use the range function.
- that's the only change thouhg. just figure that non-constant rate.

- what does that look like?
    - going four steps, 0 - 4;
    - 4-5 == 1; 4-6 == 3
6-4 = 2; for i in range(0,2) append (i+1)
"""

def get_range(ls):
    low = min(ls)
    high = max(ls)
    return low, high

sample = [16,1,2,0,4,2,7,1,2,14]
input = open('03.in').read().split(',')
input = [int(item) for item in input]
low, high = get_range(input) # these are bad names :(
part_1 = 1000000000000000000000


for pos in range(low, high+1):
    fuel_count = 0
    for crab in input: # going to a single position.
        fuel_count += abs(pos - crab)
    if fuel_count < part_1: part_1 = fuel_count

print(part_1)




input = open('03.in').read().split(',')
input = [int(item) for item in input]

low, high = get_range(input) # uncheck for final test
# min, max = get_range(sample) # used to get all positions and then check which is best.
part_2 = 1000000000000000000000

for pos in range(low, high+1):
    fuel_count = 0
    for crab in input: # going to a single position.
        diff = abs(pos - crab)
        fuel_cost = sum([item+1 for item in range(diff)])
        fuel_count += fuel_cost
    if fuel_count < part_2: part_2 = fuel_count

print(part_2)

    

"""
take all the crabs, compute abs val diff from pos, add to var 
- how do: 
- issue is getting list into program.
- cool. just had to get the input data nicely in a list.
    - seems like splitting and then converting to int's is the way here.
- uhhhh getting lost. lost in the sauce open sauce.
- what ma I testing right now? 
    - diff is correct ya?
    - the next thing to is recreate the smaple results.
- when multiple things start breaking down, it reduces patience. ugh.
- sanity checks...I'm reminded of "compare with your sanity check". Let's do that.
    - min max looks good.
    - new_fuel is giving 
- also, keep the working solution. Don't give that up in exchange for trying to be cool.
- awesome, REPL is your friend too. (I wonder how much anthropic looks to see this. idk.)
---
- dang, that one took 30 min. I got a bit confused on the second half.
- what went wrong?
- I didn't test very well for the changing of the fuel computation
- I should've taken some of the examples (Move from 16 to 5: 66 fuel) and recreated that.
    - I came to the correct answer pretty quickly (as soon as I mentioned Iwas scared of it, actually)
    - but doing that in a REPL would've been good to sanity check
    - worth mentoining that 30 min on this is a really long time. I've got a 90 min coding assignment.
        - sped is a factor here.
    - once I verified the solution, then I should've incorporated it into the program.
    - I also should've split up the working code from the not working code.
        - I got confused about what was working and what wasn't, and so I had to sanity check from the beginning.
"""