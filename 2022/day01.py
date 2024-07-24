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
    #if elf_cal > max_cal:
        #max_cal = elf_cal
    talley.append(elf_cal)

talley.sort(reverse=True)
print(sum(talley[0:3])) 



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
