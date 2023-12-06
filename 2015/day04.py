"""
(2023.12.06__02.35.26) -- (2023.12.06__02.38.54) 

(( I recorded this late because I thought I was going to sleep, but then
the answer started coming pretty quickly.))

I gotta go to sleep, but this is going to be a brute forcing attempt.
I increase the number that's added onto the puzzle input

Out of curiousity I timed it, result was 
real    0m0.096s
user    0m0.091s
sys     0m0.005s

For part two:
real    0m2.498s
user    0m2.485s
sys     0m0.013s

lol
"""

import hashlib

puzzle_input = "ckczppom"
generated_number = 0

while True:
    hash_result = hashlib.md5(f"{puzzle_input}{generated_number}".encode('utf-8')).hexdigest()
    if hash_result[:6] != "000000":
        generated_number += 1
        continue
    else:
        print(generated_number)
        break