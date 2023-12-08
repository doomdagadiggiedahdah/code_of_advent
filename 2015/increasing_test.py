import re

input_data = open("./day06input.txt", "r").read().splitlines()



for line in input_data[15:19]:

    words = line.split(" ")
    print(words)
    if words[1] != "off" and words[1] != "on":
        print(line)
        print(f"Toggle gottem ")
        # Then this is toggle
    else:
        if words[1] == "on": # turn that shit up
            print(line)
            print(words[1])
        else: # turn that shit off
            print(line)
            print(words[1])


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




