"""
(2023.12.04__12.34.03) --
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

"""

import re

with open("./day02input.txt", "r") as f:
    input_data = f.read().splitlines()

GOOD_GAMES = []
BAD_GAMES = []
PAYLOAD_BOI = 0
COLORS = {"red" : 12,
          "green" : 13,
          "blue" : 14}


# I am so sorry
for i in range(len(input_data)): # iterate through all games

    split_list_into_chunks = re.split("[:;,]", input_data[i]) # splits a game into chunks of color (and game number). eg ['Game 1', ' 7 blue', ' 9 red'...
    GOOD_GAMES.append(split_list_into_chunks[0])
    print(f"added {split_list_into_chunks[0]} to GOOD_GAMES")

    for a in range(len(split_list_into_chunks)): # goes through all elems ^^ of a single game
        for k, v in COLORS.items(): # matching COLORS with the game stats for comparison
            matching_colors = re.split(" ", split_list_into_chunks[a])

            if k in matching_colors: # gets the COLORS and relevant game on the same line 
                game_color_number = re.sub('\D', '', split_list_into_chunks[a]) # prints out the number of the game's color's result (like 7 for "7 blue")

                if int(game_color_number) > v:
                    BAD_GAMES.append(split_list_into_chunks[0])

#remove duplicates
BAD_GAMES = set(BAD_GAMES)

# remove bad from the good
for i in BAD_GAMES:
    if i in GOOD_GAMES:
        print(f"removing: {i}")
        GOOD_GAMES.remove(i)

# SUMMATION
for i in GOOD_GAMES:
    game_number = int(re.sub('\D', '', i)) # Splits out the game number to be added to PAYLOAD_BOI
    PAYLOAD_BOI += game_number
print(f"answer should be: {int(PAYLOAD_BOI)}")