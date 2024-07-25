with open("./day01input.txt", "r") as f:
    cals = f.read()
elves = cals.split("\n\n")
talley = []
max_cal = 0
for i in range(len(elves)):
    elf_split = elves[i].split("\n")
    elf_cal = 0
    for j in elf_split:
        if j.isdigit():
            elf_cal += int(j)
    if elf_cal > max_cal:
        max_cal = elf_cal
    talley.append(elf_cal)
print(max_cal)
talley.sort(reverse=True)
print(sum(talley[0:3])) 

# solution after reading through others
with open("./day01input.txt", "r") as f:
    file = f.readlines()
elf_cal = 0
elves = []
for line in file:
    strip_line = line.strip()
    if strip_line != "":
        elf_cal += int(strip_line)
    else:
        elves.append(elf_cal)
        elf_cal = 0
print(max(elves), sum(sorted(elves)[-3:]))


## (2024.07.24__09.13.08) 
# happy reindeer
# counting cals of a specific elf. 
# delineate elves by the double \n\n, 
# (09:17:23) -- (09:26:58) Awesome, got it on the first try :)
# combine into a dict, find max, return
# needs a name. For now, just needs the highest cal though.

# ok, now need to get the top three. I can store all values in a list, sort, add top three together.
# (09:31:33) -- (09:35:30) SWEET
# now let's compare my approach to others.
##################################################

#What do I notice? My code is verbose. 
#Also notice that I made up a rule (associate elf with a number) that may've held me back.
#I like readlines(). "Return all lines in the file, as a list where each line is an item in the list object:"
# readlines() is nice, for the double line just returns a single \n entry.
# lines 2 and 3 are redundant, I only use cals for that next line and could get rid of it. less cog load.
# I can consolidate 15 and 16 as well. 15 can just be sorted(talley), and then slice the last three [-3:]
# I like this solution: https://topaz.github.io/paste/#XQAAAQAcAgAAAAAAAAAyGUj/TzprcPQUiCsZq7fVyyVND7dHE7uPgW+W4M0z+wF5rSMUbIX4sEs/MjQ15WVktJsqmi8znOfx4zG0bFSd/0et6BtPkJQU9VCOpfP72HgNg6SULc3zbWtdzXkwpD7XYPXSkUB0/qUwVkkEY0Roub28jsUReHuOIY1XvMcd5Nhe8pjtjMXYfb64rdw6MHbfj9izfSQ+ILa/dv1MVQFryMACgi1dzpXCe1/AVvhAjZr1QbBmpmemlWfLNdS8eSoKwDbv9mKzoXayA1UCuvjdHy2ZFPlntTa6NB4kBMwghl5NqDljQEUoM30mRpcYoP5H0wLOlY5o0cDf+jFsSwh7FDDjrQJybSwp/Q69Cg==
    # It ends with calling the same object but one grabs the max, the other grabs top three.
    # seeing max, that's a nice way to get around the comparison I'm doing. store them all, run max.
# cool explanation of yield: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
# So where am I understanding, and where am I not?
    # not: processing the file. readlines() is cool, can't complete how that ends though
    # returning top 3 and the max, got it.
    # so turning lines into elves, I don't fully get.
# I think I can use readlines() and still use the strip().
# and now go through every line. If it's an empty string, that means it's a new elf. So what?
    # that's a sign to take current values, sum, and append to list.
# cool. Spent about an hour on this. I like the biggest takeaway of have one ultimate object (the list)
# and then operations are easy on that.