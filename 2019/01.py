"""
### 18:47 --  ### 18:51
- neat, even used two new techniques (map, importing files as list of ints) that I wasn't comfortable with.
- this is reading and implementation. This is a great result ❤️ 

- sum of fuel
" Specifically, to find the fuel required for a module, 
take its mass, divide by three, round down, and subtract 2."
- puzzle input is a module

- it was nice that I happened to remember "there was a function that takes a function and an iter
- and applies func to each item." thought it was map and read the docstring, confirmed.


### 18:53 -- ### 19:29
- sum of feul reqs
- new fuel, reqs more fuel
- I can build off first func; just need to keep talley of total weight, ya?
- fuel and its fuel. recursion boiii
    - idk how to do this. let's go with ugly
- I'm having issues with recursion.
    - if the number is no longer needed to be computed, then I return the total
        - in the test's case, should be 2
- having trouble with the reseting 0. when I call recurs, total is reset.
    - this is the thing though, then I've got it.
    - having trouble thinking it thoruhg. let's break it down.
- needing to keep talley of the fuel count while going recursive. how aobut one iter.
    - 

yeah recursion isn't my strong suit. Could use more time with that.
- did really well on the first one, got stuck with recursion on number 2.
- looking at person's solution:
    - I like that they handled the "below zero" by just setting to zero with the max() function. a small help
        - when fuel == 0, they returned 0. makes intuitive sense.
    - the `return fuel + extra_extra(fuel)` makes use of the adding I was hoping for.
        - my else statement was getting close to that.
    - I think the return 0 was something I was missing though
-in general; 
    - get the original amount (`fuel = max(( weight// 3 ) - 2, 0)`)
    - check if it's zero, if so, stop (return) with value 0
    - else, return the first value (`fuel`) and call the recursion function with current value `fuel`.

"""

def fuel_req(mass):
    return (mass // 3) - 2

lines = [int(i) for i in open('01.in').read().splitlines()]
part_1 = sum( map(fuel_req, lines))
print(part_1)
print()

## I like the simplicity here. It's nice: https://www.reddit.com/r/adventofcode/comments/e4axxe/2019_day_1_solutions/f9myhe6/
def extra_extra_extra(weight):
    fuel = max(( weight // 3) - 2, 0) # either above zero or not; handled right here
    if fuel == 0: return 0
    return fuel + extra_extra_extra(fuel)


print(extra_extra_extra(14))
print(extra_extra_extra(1969))

part_2 = sum( map(extra_extra_extra, lines))
print(part_2)



# def recursive_fuel_req(mass):
#     total = 0
#     single = (mass // 3) - 2
#     print(f'{single = }')
#     if single <= 0:
#         return 0
#     else:
#         total += single
#         recursive_fuel_req(single)
#     print(f'{total = }')
#     print()
#     return total + fuel_req(total)

# print('yooooooo')
# print(recursive_fuel_req(1969))


"""
alreday seeing "i should run the tests on this new func
"""