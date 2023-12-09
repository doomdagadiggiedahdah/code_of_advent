"""

Christmas lights with vengenance, nice
This is starting to turn up in complexity too! Cool.

- There are three actions ("turn off", "turn on", "toggle")
- the range of effected lights
    - calculating that the box that's effected
- storing info about being on or off (0,1) I'll bet ;)

Note on toggle: This only flips the lights in the range given.

I'm also thinking I should create a small scale exp to test this on. 3x3, 4x4.
Also creating objects that store the info... (lol no)

The two coordinates given make the opposite corners of a rectangle
So I need to find how to draw the sides, and then do iterated slice manipulation on all the inside lines

Ok, orienting to this grid nonsense
- numbers are basically read as y,x
- down increases in value (makes sense)
- left to right increases (like usual)
combining those two is odd to me though

## Cornerstones ##
How do I draw the sides of a rectangle in this way?
- for one coordinate, take the diff and go in that direction.
for the coordinates 2,3 and 0,1, what would the corners be? 0,3 and 2,1. So just swapping the coordinates....Let's test again, not with square
with 4,2 and 0,1 the corners are 0,2 and 4,1, they're just swapping. Cool.
Corners are done!

## Slicing Sides ##
How to get a whole side? Since I know the start and end points, I should be able to slice it, just using those same values. 
But how? How do one? Total I'll need four, actually, I should be able to use one and then iterate on another r or c.
So, how do I slice one side?
Prob this: grid[1:3,1] = "6" # changing values of a slice of a column.
Yup! I did [ one[0] ][ one[1]:two[1] ] = 1 and that did the trick. Cool :) Actual code: grid[ int(second[0]) ][ int(second[1]):int(first[1]) ] = 1 
and now to loop that until two[0] (( I worry this may have bugs in it !!! Does it work in both directions? Let's get it working one way first ))


## getting boxes ##
Cool, got boxes now too. 
There is an issue (as I feared) that right now it's only working if the big values are in coor1. 
    - if both x and y coors are the same value it creates a line as expected, but if the values flip? What if I just flip the assignment? (my audio sensibilities are wretching)
    - It does seem like the inputs are all starting from the lower value going up, maybe I just flip that part of the code and see. I'd rather have err handling though. 
- I could also do a quick test to see if that's the case (I think from these coding projects that doesn't seem infeasible.)
    - drop everything but numbers (? and commas? maybe not necessary)
    - check if value 0 < 2 and 1 < 3 always, else print "fail" 


### side adventure: testing the inputs ###
Cool, I'm putting together a test and I've also got a way to grab all numbers. that was easy.
Man this is cool, I just put together a test, found out why the thing wasn't working how I expected 
(the list wasn't integers! So I using a list comprehension to turn all the entries to ints, the logic worked as I expected).
After that, ran through all the entries and it turns out, yes, all the values are increasing; but I was able to verify by
running through the logic check and printing out the lines it was checking, saving that to a file and then running `cat results.txt | wc -l` and getting 300.
And that just kinda flew. I think that I could get really good at this. :) And this is just fun. Learning small things on the way that add up to cool things.
Side note, finding I could do list slices on for loops is great for troubleshooting. This is great.
List comprehension was nice too, easy to imagine like this:
broke:
for i in range(your_list()):
    your_list[i] = int(your_list[i])
    # ew

woke:
your_list = [int(i) for i in your_list] # yummy

Basically, from a normal loop you just take the action and put it in front of the for loop you would write, 
wrap it in square brackets, then equal it to the var you want.


## pulling operation ##
a wonky way of doing this would be
words = line.split(" ")
if words[1] != "off" or "on":
    # Then this is toggle
else:
    if words[1] == "on":
        # turn that shit up
    else:
        # turn that shit off
Let's just try it.
This was wonky and unnecessary. This works just as well
`if "toggle" in line:`


Next then is figuring out what to do for each of those.
- off = 0 (for that grid action in make_box())
- on = 1
- toggle. 
    - Needs to get current value and then flip it. Make a function I think.


### toggle functionality ###
there seems like some weirdness because of the slice, maybe I can work with that though, get a list of the results, list comp and then write that?
(maybe I come back to this after I've written the other code.)

Ugh getting all over the place. How about feeding in a single value from the data to actually change something? That sounds nice.
Got that, now what? getting new variables to work as expected. Got that now as well (with a simple test example! small uncertainty)
Ok, now how about testing just the on/off functionality? htat's easy
I could write a test function that counts how many lights are on at a given time, but so far all the logic has turned out great.
    - In case I need it, I'd just take the difference of the two x and y coors and multiply them by eachother, compare that with the sum of the graph
Instead I'd like to focus on Toggle again.

### Toggle FRFR ###
get current value, if a get b and then assign that as `value`. Iterate. How to fit this into existing structure though?
how can I get current value with this structure?
I don't think I can use `grid[i][ coor1_x : coor2_x + 1 ] = value` because the values aren't the same throughout.
I get current y first then x.
I think I got it, my two main uncertainties are:

1. am I summing correctly, and
2. is the toggle working as it should?
My summing doesn't seem to be the problem, I'm getting consistent results with the diff sum commands.
Let's do some tests to see if it's working as I'd hope. 
Toggle isn't working. (nice, was able to find this out immediately. 😄) I get the sums from each step and the first toggle steps should give me some, but AREN'T.
blast from the past:- In case I need it, I'd just take the difference of the two x and y coors and multiply them by eachother, compare that with the sum of the graph
jeez, mixed up assignment and equal operations. yikes.
But, after that it worked perfectly ❤️


(( random idea, may've already written on this. Something I noticed from watching the dudes go through the
AOC challenges was that they were mostly looking at the code to understand the behavior, not the results.
I interpret this as "I hvae command enough of the language that I can put the results together without needing
to see them". That's a goal. Kinda reminds me of sightreading. ))
    
### Milestones ###
- From a pair of coordinates, draw out sides of a rectangle, or just start with the four corners (done! sides next)
    - ?be able to change the values of the sides?
- Ok, coming back to milestones, what next? I need to 
    - be able to grab the "turn off/on" and "toggle" text from the sentences
        - and then have that switch logic.
    - also deve the logic to operate on them.
        - implement the logic
    - finally, (damn, can't remember.)



### Grid Operations ###
grid = np.zeros((4,4)) # creating a grid f zeros
single_val = grid[2,1] # access a single value
grid[:,1] = "6" # changing values of a column
grid[1,:] = "6" # changing values of a row
grid[1:3,1] = "6" # changing values of a slice of a column.


### Part Two ###

all we're doing is changing the instructions.

lights can't go below zero
turn on += 1
turn off -= 1
    if grid[y][x] == 0:
        continue
toggle += 2

oh, another thing I was happy about, before I started randomly trying out where I should put print statements (no points for guessing)
I thought about the loop structures and put it in the right spot on the first time. Nice :)

YES!!! Got the second answer on the first try! I like understanding exactly what's going on in code, that feels really good!

"""
import re
import numpy as np
input_data = open("./day06input.txt", "r").read().splitlines()

grid = np.zeros((1000,1000))

for line in input_data:

    # "turn off 2,5 through 8,8"
    numbers = re.findall(r'\d+', line)
    numbers = [int(i) for i in numbers]

    coor1_y = numbers[0]
    coor1_x = numbers[1]
    coor2_y = numbers[2]
    coor2_x = numbers[3]

    # Part One
    # def make_box(value):
    #     for y in range(coor1_y, coor2_y + 1):
    #         grid[y][ coor1_x : coor2_x + 1 ] = value
    
    def turn_on():
        for y in range(coor1_y, coor2_y + 1):
            grid[y][ coor1_x : coor2_x + 1 ] += 1

    def turn_off():
        for y in range( coor1_y, coor2_y + 1 ):
            for x in range( coor1_x, coor2_x + 1 ):
                if grid[y][x] == 0:
                    continue
                else:
                    grid[y][x] -= 1

    def toggle():
        print("srarting Toggle")
        for y in range( coor1_y, coor2_y + 1 ):
            grid[y][ coor1_x : coor2_x + 1 ] += 2
            # for x in range( coor1_x, coor2_x + 1 ):
            #     grid[y][x] += 2

                # Part One boi
                # if grid[y][x] == 0:
                #     grid[y][x] = 1 
                # else:
                #     grid[y][x] = 0

    # control flow
    if "turn off" in line:
        turn_off()
    elif "turn on" in line:
        turn_on()
    elif "toggle" in line:
        #??????
        toggle()
    print(f"Line {line} is giving " + str(np.sum(grid)))
    


# print(np.sum(grid))
# print(grid.sum(axis=0))
# print(sum(grid.sum(axis=0)))
# print(sum(grid))