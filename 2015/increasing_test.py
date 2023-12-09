import re

input_data = open("./day06input.txt", "r").read().splitlines()



for line in input_data[15:19]:

    if "toggle" in line:
        print(line)
        print("toggle detected")
    elif "turn off" in line:
        print(line)
        print("turn off detected")
    elif "turn on" in line:
        print(line)
        print("turn on detected")


    numbers = re.findall(r'\d+', line)
    numbers = [int(i) for i in numbers]

    print(numbers)
    # print(numbers[1])
    # print(numbers[3])
    if numbers[0] < numbers[2] and numbers[1] < numbers[3]:
        continue
    else:
        print(f"{line} failed! Yikes!")
        break




