### 19:06
# get values from the lrtb, if shorter then yes
# all of the edge trees are visible.
# I'm thinking check if trees exist at all places, if no add point, else compute vis
# use tree index, not the object itself
# having trouble...take it easier then.
# I struggled with this for a bit, good thing I looked it up cuz it is more challenging for sure

# talking with GPT on how to approach this: skip the top and bottom rows entirely.

### 19:13
# the answer cmae to me in a dream
# ok, and then checking against the rest of the trees 


sample = """\
30373
25512
65332
33549
35390
"""

visible = 0
rows = sample.splitlines()

for row in range(1, len(rows)-1):
    len_col = len(rows[row])
    for tree in range(1, len_col-1):
        print(rows[row][tree])