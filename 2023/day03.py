"""
(2023.12.05__10.33.17) -- 
Oh jeez, well I was going to say that this will be difficult, but maybe not. Just break it down.

Already seeing a possible route.

--- Ex ---
467..114..
...*......

I can see that there's a grid (input file has a set number of characters, 140), 
diagonally is acceptable and with 467 it takes up
three spaces, one down and one to the right is a symbol and makes it legit.

So roughly, determine whether a number is legit (like a hit box basically) DONE
Find out how to get the numbers as a cohesive unit (and then apply the hit box on that range?) 
Add acceptable numbers to payload.

--------
Can I get ALL numbers (as individual chunks, like "467" and "114" above) first? 
and then I can write a function to determine if legit
- yup, gotem
ok, thinking that if I can find the position of those (they are strings) then I can 
look around that position for symbols. So get position first.
- maybe use str.find(). This returns the lowest index (which scares me for repeated values on a string), 
- but I can designate the start point and just place the start after the first. Some finagling. If needed.

I've got all the numbers on a line, their positions, and length. Now what? I think it'd be the box check.
Let's just do a simple one, finding if a number has a symbol (not a period) same line, one space away.

Simple, same line box check:
I want to take the location, and see if there's a symbol on either side, if yes, print GOTTEM
how do I check if there's a symbol +/- 1 index away from a location? OR statement, 
if string[index+/- 1] == regex_for_symbols:
    print("YEET")
else:
    print("noooo")

Sweet, got a very basic version down. Now to generalize, 1. the symbols and 2. the lines and direction to test.
Also, a cheap way is to get the symbol that regex finds and check if it's a period, if so skip
"[^.]" ---  any character not a period
Oh, I can also just drop all symbols that are digits and periods

Box:

$$$
$x$
$$$

Looks like:
    input_data[-1]:-1, 0, +1
    input_data[0]: -1, +1
    input_data[+1]:-1, 0, +1

Those are all characters, I can grab them, put them in a string, and then do one check for qualChars, ya?

### Getting the Box ###
I think this is going to be big. Just remembered slices though, so that should simplify.
Ex. new = new.join(hhh[2:5])

I can make this way easier and just do three lines, slices of the length plus 1 on both sides. (indexError?)
Let's just try the same line slice. Get all chars from the same line.

Ok, I do have the character box, not as bad as I thought it would be. Now what? Let's verify a single case.
Also need to get it so the input_data index can be flexible, but that can come later.

This is weird, printing the index of line 2 (index 1) and asking for print(another[92]) =='s 4, but print(another[91]) == ".", which should be a "/"
Hmmm ok seems like 4 just isn't getting picked up...
OHHHHHHHH ok, got it. Index 92 is getting picked twice because of how I'm going through the line. Man. Headache. But now understanding.

Line 111 is using re.find() and is stopping when it finds the 4 of "470" and stops searching. Damn that seems like a problem.
I could get around this by having the search start after the index of the previous? I can already see it happening on other lines. Is that hard to do?
`try_this = another[93:].find("4")` on line 2 gives me `27` where input_data[27+93] == 4 like I'd hope. I should be able to take the index_displace value 
add it to the result of .find and get the actual value

Maybe there's a better way to do this though, this does feel shaky. I could also replace them in the string >:) then I have less janky shit going on.
Yeah, good thing I asked. `input_data[1] = re.sub(f"{number}", r"...", input_data[1])` works just fine (on line 2).

Alright, looking good for a single line, now to get it to scale. Right? Anything else first? I think we're good, just edge case handling.

SIDES:
if same_line_string == index[0], then don't do prev_line_string
if same_line_string == index[last_line_of_file], then don't do next_line_string

I'm really digging my stlying, I like how my code looks

### Numbers aren't being Caught. Why? An Essay ###

On line 136 `710.387` aren't being picked up when they should be. Let's debug.
find_all_nums_on_single_line is getting all the numbers on the line, that's good.
So I know that those numbers aren't being registered as winnders, which they should 
(having a lower number is a good sign that I'm missing values)
There's also a weird new line that's weird

Here we go, with the `re.sub(f"{number}", r"...", input_data[line_num_input])` I'm running it's replacing too many values.
Cool, `re.sub` has a `count=` parameter that I set to one

My first attempt was 505925 and that was too low, after that change am getting 466562. Others are falling behind.
Weird, on line 139 number 759 should be trippedbecause of the "-" diagonally from it, it's printed out the line before it, 
but not in the char_box....So let's see what's wrong with that.

If it's being recognized on the line before it but not from the char_box then must be something wrong with it.
Are there other diagonals with issues?
- line 137 has upLeft diag, it's reported.
- line 138 has upRight diag, it's reported. Weird, that's the one that has the problem below...
(( looking at my notes, I wrote a book ))
- this one is hard damn

- Looks like some are being doubly added too :,( one thing at a time.

But it looks like I'm shifting the values with some substitution.
re.sub(f"{number}", r"...", input_data[line_num_input], count=1) # This line will be the death of me.
Right now it's adding three periods regardless of the length of the value. easy to fix.

Guessed 506142 and that's also not the answer.

Foudn ANOTHER edge case. I wonder how much I should balance "submitting answers" vs. looking for edge cases.

### 
LHS edges are missed. 
Line 37 starts with `999` and has a weird black hole.
Line 46 has `713` that should also be counted, also black hole.

Yup, so if the index is 0, it doesn't return any text for the char_box(). So, need to handle errors.
I wonder if the end of the line gets similar black boxes.

Jesus, I got it! that was rough.
"""


import re

with open("./day03input.txt", "r") as f:
    symbols_then_input = f.read()

PAYLOAD_BOI = 0
input_data = symbols_then_input.splitlines() # In case I need split lines, otherwise need this to get the qual symbols.

# get the relevant symbols to look for >:)
almost_symbols = re.sub("\d", "", symbols_then_input) # remove all digits from file
turn_into_set = re.sub("\.", "", almost_symbols) # remove all periods
qualifying_symbols = set(turn_into_set) # get one occurence
qualifying_symbols.discard("\n") # for some reason there's a \n there.
# print(len(qualifying_symbols))


def get_char_box():
    box_string = ""
    if line_num_input == 139:
        prev_line_string = input_data[(line_num_input-1)][(number_start_index - 1):(number_start_index + number_length + 1)]
        same_line_string = input_data[line_num_input][(number_start_index - 1):(number_start_index + number_length + 1)]
        # next_line_string = input_data[(line_num_input+1)][(number_start_index - 1):(number_start_index + number_length + 1)]
    
        box_string += prev_line_string
        box_string += same_line_string
        # box_string += next_line_string

    elif number_start_index == 0:
        prev_line_string = input_data[(line_num_input-1)][(number_start_index):(number_start_index + number_length + 1)]
        same_line_string = input_data[line_num_input][(number_start_index):(number_start_index + number_length + 1)]
        next_line_string = input_data[(line_num_input+1)][(number_start_index):(number_start_index + number_length + 1)]

        box_string += prev_line_string
        box_string += same_line_string
        box_string += next_line_string
        
    else:
        prev_line_string = input_data[(line_num_input-1)][(number_start_index - 1):(number_start_index + number_length + 1)]
        same_line_string = input_data[line_num_input][(number_start_index - 1):(number_start_index + number_length + 1)]
        next_line_string = input_data[(line_num_input+1)][(number_start_index - 1):(number_start_index + number_length + 1)]

        box_string += prev_line_string
        box_string += same_line_string
        box_string += next_line_string


    # print(input_data[line_num_input])
    # print(same_line_string)
    # print(box_string)
        
    return box_string

for line_num_input in range(len(input_data)):
# for line_num_input in range(104, 105):

    find_all_nums_on_single_line = re.findall('\d+', input_data[line_num_input]) # get list all nums on a line, check if number legit
    print(find_all_nums_on_single_line)
    print("Line number" + str(line_num_input+1))


    for number in find_all_nums_on_single_line:
        number_start_index = input_data[line_num_input].find(number) # returns index of number
        number_length = len(str(number)) # Use length to run the box search len number of times.
        
        # print(f"The number {number} starts on index {number_start_index} and has length {number_length}")
        print("Start Diagnostic Info")
        print(get_char_box())
        
        for char in qualifying_symbols:
            if char in get_char_box():
                print(f"We have a winnder! The number is {number} and the char is {char}")
                PAYLOAD_BOI += int(number)
        
        # print("\n\nanother chunk\n")
        # print(input_data[(line_num_input-1)])
        # print(input_data[(line_num_input)])
        # print(input_data[(line_num_input+1)] + "\n")

        # print(input_data[line_num_input])
        replacement = "."*number_length
        input_data[line_num_input] = re.sub(f"{number}", "."*number_length, input_data[line_num_input], count=1) # here's the culprit.
        # print(input_data[line_num_input])

    print(PAYLOAD_BOI)
    # print(qualifying_symbols)
