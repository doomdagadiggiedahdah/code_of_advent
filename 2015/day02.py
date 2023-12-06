"""
(2023.12.06__01.17.45) -- (2023.12.06__01.38.01) (whoops, didn't save the time for part two, but it was quick)

wasn't 1715567
sort didn't work on integers, needed to convert to ints first.
"""

input_text = open("./day02input.txt", "r").read().splitlines()
wrapping_paper = 0
ribbon = 0

for present in input_text:
    dimensions = present.split("x")

    dimensions = [int(x) for x in dimensions]
    dimensions.sort()
    # print(dimensions)        

    wrapping_paper += 2 * (dimensions[0] * dimensions[1])
    wrapping_paper += 2 * (dimensions[0] * dimensions[2])
    wrapping_paper += 2 * (dimensions[1] * dimensions[2])

    ribbon += 2 * dimensions[0] + 2 * dimensions[1]
    ribbon += dimensions[0] * dimensions[1] * dimensions[2]
    
    wrapping_paper += dimensions[0] * dimensions[1]

print(wrapping_paper)
print(ribbon)