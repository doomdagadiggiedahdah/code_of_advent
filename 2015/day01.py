"""
(2023.12.06__01.03.28) -- (2023.12.06__01.12.36) 
( = go up 1x
) = go down 1x

Talley the number, cross out, and give result.
This was WAY easier than 2023's levels so far, jeez.
"""

level_count = 0

input_text = open("./day01input.txt", "r").read()

for i in range(len(input_text)):
    if input_text[i] == "(":
        level_count += 1
    else:
        level_count -= 1
    if level_count == -1:
        print(i+1)
        break
    
print(level_count)