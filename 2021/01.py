# How many measurements are larger than the previous measurement?
### 14:40 -- (15:02:40) 
### 15:05 -- (15:16:21) 


sample = """\
199
200
208
210
200
207
240
269
260
263
"""

cycle = sample.splitlines()
cycle = open('01.in').read().splitlines()
cycle = [int(item) for item in cycle]

count = 0
for index in range(len(cycle)):
    try:
        ## get prev num, compare it to current, count
        prev = cycle[index-1]
    except:
        continue
    if cycle[index] > prev:
        count += 1
# print(count)


## need to get the next three indexes, add together and then com[pare]
# need :2 for two values.

next_sample = """\
607
618
618
617
647
716
769
792
"""

cycle = next_sample.splitlines()
cycle = open('01.in').read().splitlines()
cycle = [int(item) for item in cycle]

count = 0
for index in range(1, len(cycle)):
    try:
        # next three
        prev = cycle[index-1:index+2] #this is being counted twice...
        curr = cycle[index:index+3]
    except:
        print(index)
        continue

    print(curr, prev)
    if sum(curr) > sum(prev):
        count += 1
print(count)


"""
hmmmm
I'm not getting the right values in the lists used for comparison.
    note: writing out the exact point I was having an issue with got me to look at the right probelm


quick reflections:
- I wasn't getting the right indexes in the beginning of #2, the prev / curr were only going to :2 instead of :index+2 (or +3)
- think I did pretty well for the first one, forgot how to import the file.
- writing out the "hmmm" comment was good. 
    - wasn't sure what to look at, so I wrote my exact mistake and then got it.



"""