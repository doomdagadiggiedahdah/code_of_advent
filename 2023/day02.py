"""
(2023.12.04__12.34.03) -- (got distracted phone call from friend and lunch)
problem was kind of confusing at first, but seems to make sense.
-- basically, there's a big ol list of games that I want to check to see 
1. which would be possible with the new dice config and then
2. take the numbers from those games that have been played and add them all up (regex again)

Thoughts?
- split a game to a single line DONE
- chunk each game to a list sep'd by (semi-)colons (edit: and commas! now can go through each game straight away)
- check each iteration against the dice config and if over the amount of dice break
    - This needs to match color to color, and then check the number. Unsure of how to do that right now
    - within each item of the list, split item by comma (will "7 green, 5 red, 3 blue;" be split into three sections?), "case" statement for rgb and then remove letters, compare values 
- else, take game number and add to PAYLOAD_BOI


lil fuzzzy on the dice numbers, the check and then logic of accepting.
easy to associate game number with it's results and add if need be.
how can I compare just one?

I've got the right colors matching with eachother. Now I need to compare the values of COLORS with the value of the game result.
ok I've got this, now I just need to add the game numbers to PAYLOAD_BOI. So I need to know when the logic check is complete, and if a failure has happened or not.

Yeah I'm not thinking of something. So if all a game's elements are checked and nothing goes over, then the game number is added to PAYLOAD. So, when does that logic finish?

Ok, got the adding down, but even the failing games are being added...

oh man that was hard for abit. 

Ultimately, I had tried to do too much in one chunk of code. What I ended up doing was creating logic that would determine if the game was bad or not, 
added that to the bad list, created a set out of bad list to get rid of any duplicates, and then made a list of all the good games, 
which was everything at first, and then subtracted all the bad games from that. 
From that, I got the game number and added all the good ones.


#### PART TWO ####
What's the fewest number of each cube needed to play each individual game?
Ex. Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green == 6 blue, 4 red, 2 green

Need to get this for each game ^^^

It says "for each game", I'm assuming that's ALL games, not just the GOOD_GAMES

Finally, "what is the sum of the power of these sets?"

I will still need to go through each line, find the smallest number for each color.
Store the smallest number in a list (or multiply it right then, can use *= )
then add up all those numbers.

Let's find a way to get the smallest number of each color in a line.

(( I'm seeing in real time why it's good to name your variables descriptive names. Your code acts as comments ))

I want to do the lowest number comparison now. I need have the game section's color and number, and then compare that to COLORS.
"""

import re

with open("./day02input.txt", "r") as f:
    input_data = f.read().splitlines()


## Part Two ##
PAYLOAD_BOI = 0 # for the final answer

for single_game_line in input_data: # go through each game
    
    POWER_STORE = 1 # Master Plan: take the values of COLORS and multiply each by this, then add result to PAYLOAD_BOI
    split_game_into_chunks = re.split("[:;,]", single_game_line)
    COLORS = {"red" : 0, 
              "green" : 0,
              "blue" : 0}
    
    for game_element in split_game_into_chunks: # iterating through each color or game chunk; output [' 9 green']

        # print(game_element)
        for k, v in COLORS.items(): # begin compare of COLORS values with largest dice values
            single_die_elem_breakdown = re.split(" ", game_element) # output ['', '9', 'green'], 
            if k in single_die_elem_breakdown: # match colors together
                # print("this hit 1")
                if int(single_die_elem_breakdown[1]) > int(v): # find the largest number of dice needed
                    # print("this hit 2")
                    COLORS.update({k: single_die_elem_breakdown[1]})
            # print(COLORS)

    for color, value in COLORS.items():
        POWER_STORE *= int(value) # execute master plan
        # print(single_game_line) # sanity checking
        # print(COLORS)
        # print(str(POWER_STORE) + "\n\n")
    PAYLOAD_BOI += POWER_STORE

print(f" the answer is {PAYLOAD_BOI}")



## Part One ##

# GOOD_GAMES = []
# BAD_GAMES = []
# PAYLOAD_BOI = 0
# COLORS = {"red" : 12,
#           "green" : 13,
#           "blue" : 14}


# # I am so sorry
# for i in range(len(input_data)): # iterate through all games

#     split_list_into_chunks = re.split("[:;,]", input_data[i]) # splits a game into chunks of color (and game number). eg ['Game 1', ' 7 blue', ' 9 red'...
#     GOOD_GAMES.append(split_list_into_chunks[0])
#     print(f"added {split_list_into_chunks[0]} to GOOD_GAMES")

#     for a in range(len(split_list_into_chunks)): # goes through all elems ^^ of a single game
#         for k, v in COLORS.items(): # matching COLORS with the game stats for comparison
#             matching_colors = re.split(" ", split_list_into_chunks[a])

#             if k in matching_colors: # gets the COLORS and relevant game on the same line 
#                 game_color_number = re.sub('\D', '', split_list_into_chunks[a]) # prints out the number of the game's color's result (like 7 for "7 blue")

#                 if int(game_color_number) > v:
#                     BAD_GAMES.append(split_list_into_chunks[0])

# #remove duplicates
# BAD_GAMES = set(BAD_GAMES)

# # remove bad from the good
# for i in BAD_GAMES:
#     if i in GOOD_GAMES:
#         print(f"removing: {i}")
#         GOOD_GAMES.remove(i)

# # SUMMATION
# for i in GOOD_GAMES:
#     game_number = int(re.sub('\D', '', i)) # Splits out the game number to be added to PAYLOAD_BOI
#     PAYLOAD_BOI += game_number
# print(f"answer should be: {int(PAYLOAD_BOI)}")