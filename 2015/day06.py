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


"""
import numpy as np
input_data = open("./day06input.txt", "r").read().splitlines()

grid = np.zeros((7,7))
# print(grid)

# Test values
coor1 = "1,1"
coor2 = "4,6"

first = coor1.split(",")
second = coor2.split(",")


def make_box():
    for i in range(int(first[0]), int(second[0]) + 1):
        grid[i][ int(first[1]):int(second[1]) + 1 ] = 1
        print(i)
    # grid[ int(second[0]) ][ int(second[1]):int(first[1]) ] = 1 
    print(grid)
    

grid[ int(first[0]) ][ int(first[1]) ] = 1
grid[ int(second[0]) ][ int(second[1]) ] = 1
print(coor1)
print(coor2)
print(grid)
make_box()