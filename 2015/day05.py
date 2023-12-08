"""
(2023.12.06__15.53.44) -- (2023.12.06__16.32.52) 

string verification. 
Needs to have:
3 vowels
can't have two same letters next to eachother
can't have ab, cd, pq, or xy in it.

double letters. 
should be able to get the regex for a single letter
if letter at index i is == index i+1, break. Else increase PAYLOAD_BOI
don't even need regex, if 

Could also have a single test per criteria, if it trips then a number is added, take the length of the og doc and subtract out the others.

Man I read the instructions wrong. Damn.
It <b>needs</b> to contain multiple letters in a row, jesus. Starting over.

Need to find how many vowels in the string.

Ok, the pattern that I'm seeing is that I'm getting confused with where I should put the success metric. Sounds like control flow tbh.
For ex: I didn't put PAYLOAD in the right place and it ended up being tripped on multiple times for a single string.
            - putting the break statement in after it met all criteria it needed to tripped it only once.
What ended up being helpful for this was putting in print statements to see where the logic was being tripped (or not).
Before running, I would imagine the output that I wanted, and if the program went against that I would know exactly where to look.


Another helpful thing, I can slice through the list I'm working on to find a small range that has the edge cases I'm looking for
If the code I'm writing isn't being tested by the input, I can move around to find that range to work on.
Also makes sense why the AOC videos I wanted would try out their algos only on the example inputs.
--------------------------------------------------------------------------
(2023.12.06__17.51.06) -- (2023.12.06__18.41.40) 

New patterns to find.
- If any pair of letters are repeated, but not inclusive (like "xxx" wouldn't count)
    - Can do this with taking two characters from a string, replacing them and then matching
    - iterate on each char of the line
- AND a pattern of a single letter, other letter, then first letter again. 
    - I can do regex with a variable right? Like {line[letter]}\w{line[letter]}

I know that my code for the second one works, I just need to put it in the right
I don't like how I'm putting this code together tbh. I have to rely on stops a lot and that seems shaky. Not solid.
I got this part working because of putting in breaks at the right places (the loops would run until they either proved wrong or were satisfied.)

And there's still something I can learn from not having the add to PAYLOAD in the right places. I'm not thinking about the termination of cycles correctly.
Finding out what it is that I want to complete should give a hint as to where I want the update to come in.
As well as noting whether or not I want the loop to stop after a certain event happening.

Also realized that I could've tested the FBF_match easier (without needing re), in this case I'm only working with letters so I could've just done line[l] == line[l+2]
"""

import re 
input_data = open("./day05input.txt", "r").read().splitlines()

bad_combos = ["ab", "cd", "pq", "xy"]
PAYLOAD_BOI = 0


### Part Two ###
for line in input_data:

    for letter in range(len(line)-1):
        match_me = line[letter] + line[letter + 1]
        # print(match_me)
        subbed_line = re.sub(match_me, "..", line, count=1)
        # print(subbed_line)

        if match_me in subbed_line:
            print() # This has to keep going, 
            # print(f"{line} checking for FBF_match now")

            for l in range(len(line)-1):
                FBF_match = re.search(f'{line[l]}[a-z]{line[l]}', line)
                # print(FBF_match)
                if FBF_match:
                    PAYLOAD_BOI += 1
                    break
            break

print(PAYLOAD_BOI)







### Part One ###
# for line in input_data:
#     print(line)
#     # get rid of bad combos. the single line goes to next checkpoint.
#     if any(i in line for i in bad_combos):
#         # print(f"{line} had a bad character")
#         continue
#     # else:
#     #     print(f"{line} had ZERO bad characters")
    
#     # Vowel count
#     vowel_count = 0
#     vowel_map = map(line.count, "aeiou")

#     for i in vowel_map:
#         vowel_count += i
#     # print(f"Num of vowels {vowel_count}")
#     if vowel_count < 3:
#         continue

#     # double letters
#     for letter in range(len(line)-1):
#         if line[letter] == line[letter+1]:
#             # print(line)
#             PAYLOAD_BOI += 1
#             # print("This one made it \n")
#             break
#         # else:
#         #     print("hit the braeks")

# print(PAYLOAD_BOI)