"""
(2023.12.06__01.47.47) -- (2023.12.06__02.01.59) 
(2023.12.06__02.13.19) -- (2023.12.06__02.20.20) 

How do I keep memory for this? Stored in a grid?
I keep a counter. And now what? 
create a dictionary that stores the state of the grid and tells how many times it's 
been there? Only need the number of houses, not a count of presents.

They take turns huh, so if index odd, it goes to one, even the other.
but the houses delievered to need to be kept track of still.

"""

input_data = open("./day03input.txt", "r").read()

grid_counter = [0, 0]
robo_counter = [0, 0]
state_record = []
counter = 0

for i in input_data:
    if counter % 2 == 0:
        if i == "^":
            grid_counter[0] += 1
        elif i == "v":
            grid_counter[0] -= 1
        elif i == ">":
            grid_counter[1] += 1
        elif i == "<":
            grid_counter[1] -= 1

    else:
        if i == "^":
            robo_counter[0] += 1
        elif i == "v":
            robo_counter[0] -= 1
        elif i == ">":
            robo_counter[1] += 1
        elif i == "<":
            robo_counter[1] -= 1


    counter += 1
    # print(counter)
    state_record.append(f"{grid_counter[0]} : {grid_counter[1]}")
    state_record.append(f"{robo_counter[0]} : {robo_counter[1]}")
    # print(len(state_record))

state_record = set(state_record)
# print(state_record)
print(len(state_record))