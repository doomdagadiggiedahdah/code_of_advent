import re

# Import webpage (meh, I'll copy/paste to not call the site so much)
with open("./day01input.txt", "r") as f:
    input_data = f.read().splitlines() # .splitlines() gives a list of each line. This is nice.

PAYLOAD_BOI = 0
# strip all numbers and print
for i in input_data:
    # print(input_data[i] + "::: result of :::: " + re.sub('\D', '', input_data[i])) # manual check to see the regex
    # ok, I can get all of the numbers out. now what?
    just_numbers = re.sub('\D', '', i)
    # print(int(just_numbers[0] + just_numbers[-1]))
    PAYLOAD_BOI += int(just_numbers[0] + just_numbers[-1])
    # need to take the first and last numbers, combine them, and then add them. The last two steps happen for both of these "streams"
print(PAYLOAD_BOI)






""" Rough plan of attack:
Import the webpage
read one line at a time
strip out all the letters
??Not sure how to go about the number selection. Thinking: if len(list_of_nums) == 1, add, else take index 0 and end and .... (do something)
?? What's the end goal? I want to take the two numbers, and make a 10's digit and 1's digit (can do the char, print, int() trick)
And then I can just add all those values together, submit the end result. (this has the danger of not knowing which lines are causing problems. ?Write tests?)
?store each value into a dictionary? (would be helpful for troubleshooting purposes but not necessary)
(It'd be really helpful to return a `head` of some of the lines to manually compare)
"""



# Thoughts section (2023.12.03__15.42.19) -- (2023.12.03__16.38.59) 

# skip straight to the end and see "What is the sum of all of the calibration values?"
# I see some examples above and the answers, regex comes to mind
# Or look at the string, find all numbers and add to list, take first and last indexes and add them together
# Importante: "On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number."
# Alright, I think I've got enough to go for it.
# Essentially: I'll be given a series of lines of text that I need to extract the numbers from, combine them in a certain way and then add them allllll up.
# (Neat, there is a webpage that hosts all the lines, I can grab that I'm sure.)
# Also, I'll be using ChatGPT on this not to gen code, but to talk through more standardized ways to do this.
# One thing I really liked was writing a solution to a problem, feeding it into ChatGPT and then having it explain what is it that I could do better.
# But then taking the time to work through the code in my head to see why it actually was better. Master as the needle, the student the thread.

"""
this took a lil over an hour (which doesn't feel right, I think I got distracted at some point, my music has only been playing for 43 minutes)
but either way this was nice and calm.
Doign the write out to make sure I understood the problem was good and then I went right to the answer. The code I wrote was pretty straightforward.
I didn't have to do a lot of searching for alt methods, I had a few questions I googled and everything came together right away. This was relaxing.
"""