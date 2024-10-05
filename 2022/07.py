### 11:25
# get file tree
# get total size of all directories
# and then there's some decisions.

# break by $; good
# recognize command. 
    # cd is good for organizing. maybe not needed. 
    # ls tells quanities.
# split first line to get command; awesome, this is working well.
# destructuring.
# now I need to get all the lines of a chunk
### 11:45
# I'm sure I could muscle through this, I've gotta go for now though ❤️ 
### 10:32
# I'm thinking I should be able to parse it to the point of having a cmd and response obj that I can refer to
# result I want: command and results into their own objects
# just not sure how to store this stuff.
# also remember, I'm trying to create and edit at the same time.
# I don't know the "standard way" of creating this type of code right now. I can do it wrong, but have it work, and then upgrade from there.
# also there's a few different goals this thing needs, so I'll need to solve one problem at a time to get to the end.
# I get the sense of too many combinations going in my head. let's take a step back.
    # I've got granular results of ls. that's good, parsing that 
# how about listing nicely the results of a single directory? Done, that's nice.
# some confusion about getting the size of a dir if there's another dir in it.
# let's assume that there's no files being added. I could just create a record of each dir
# make a function that compute_size() and if there's a dir in this record then it fetches that dir
# also, I'm making a parser, this is fun ❤️ 

# In dir: / we see contents: ['dir a', '14848514 b.txt', '8504156 c.dat', 'dir d']
# thinking I store all dirs like ^^, and then run compute_size() on it
# got a bit lost in something. 
# so I've got the commands and contents sep. good. now what?
# don't know what to do for the `..` dirs.

# one thing at a time. I wanted to get the numbers for a directory that had only files. no recursion.
# rna into a bug where I'm getting two folders for cur_dir=='d'. 
# but, the logic for computing a single folder is correct. 
    # getting there appropriately needs work.
    # and then recursion, and it's done.
# actually so that feels way closer than before.
# (( meta-note: taking a second to ID what my goal was that got me lost put me back on track nicely. ))
### 11:40
# let's troubleshoot the cur_dir


# NEEDS:
# associate contents with a directory
    # taking ls and associating it with a directory.
# variable for current directory

sample = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

command_and_result = sample.split("$ ")
cur_dir = ''

# I want to check the string dir is in any entry of a list.
# let's start with the non recursize example


# def compute_size(ls_contents):
#     # if 'dir sub' in ls_contents, compute_size(dir_sub)
#     dir_size = 0
#     for item in ls_contents:
#         dir_size += int(item.split(' ')[0])
#     print(dir_size)


# for chunk in command_and_result[1:]:

#     # destruct to commands and results
#     lines = chunk.splitlines()
#     command = lines[0]
#     if command.startswith('cd'):
#         cur_dir = command.split(' ')[1] # this won't work for the `..` command......
#     if len(lines) > 1:
#         ls_contents = lines[1:] # I feel good till here. there's either cd or ls_contents
#         # print(f"In dir: {cur_dir} we see contents: {ls_contents}")


#     # # compute size
#     # print(f'we have this: {cur_dir}')
#     if cur_dir == 'd':
#         # print(lines)
#         compute_size(ls_contents)

# ok, the dir can change but not have ls_contents be run, that's why it happens twice
# only get the contents size after changing to a directory
# don't know how to think about it.
# something about associating sequential ughhhhhh



#### sigh

# seems like there's some tools that I'm not familiar wit hthat would make this easier.
# and maybe that's something to take note of, when I'm not feeling much progress in something
# and specifically that I feel I'm butting up against a wall
# where I could muscle through, but it's not going ot be pretty. 
# someone else has probably run into this and has figured something out.
# in those times, I think me figuring out on my own won't be as helpful as seeing how others approach it
# in this time, people are using defaultdict; idk what that is and I'm about to find out.
# oh also, the way that someone else talked about destructuring, I wouldn't have encountered that
# as a "community accepted concept" (or some such term). 

# I've heard of defaultdict before, "It provides a default value for the key that does not exist." -[source](https://www.geeksforgeeks.org/defaultdict-in-python/)
# interesting, you can ask for whatever key you want, and it'll respond with a default value.
# so why useful here? Ah, each directory is key, 




# https://topaz.github.io/paste/#XQAAAQApAgAAAAAAAAAzHIoib6pXbueH4X9F244lVRDcOZab5q1+VXY/ex42qR7D+RJIsrl/Sxb6tPAL+4hwfHLYDcxAkOQUPDzJHt5E6HtsTuD7sQmi8zUjU23yXHSz2Ybz1Wg76Dml+yk2nSfpuHeVfYbBzOSzCq56Pqa2xKaoiZFw198LfErdujq9KpE+VyQQcqTb+3lhE6lB+md3/24UDyF9kQ7hNPzS3MMiOqXfViov9xImHF/cBQtDixb1urf0ihR2KbZi4sIlWsKr0bb1xtUxAP3NlxXAiq/OMZ0yHqyOrimJgFLHSn1lR9Gs1jLjZCGuSE5JTAqg6l18+0PmcudpJXsn21dPkc7Zqcm9JT6oQ9kl5C/HsOnhg0zfNdUV06YFakTcAq3/yygRiA==
# I hate how long these links are
# I like the way they setup a list to keep track of the directories. '..' == curr.pop(); perfect
# this one got 66 points, neat.
# the accumulate for loop is cool too.

# from collections import defaultdict
# from itertools import accumulate

# dirs = defaultdict(int)

# for line in open('07.txt'):
#     match line.split():
#         case '$', 'cd', '/': curr = ['/']
#         case '$', 'cd', '..': curr.pop()
#         case '$', 'cd', x: curr.append(x+'/')
#         case '$', 'ls': pass
#         case 'dir', _: pass
#         case size, _:
#             for p in accumulate(curr):
#                 print('this one mat')
#                 print(curr, p)
#                 dirs[p] += int(size)

# print(sum(s for s in dirs.values() if s <= 100_000))


# yeah, it works but I'm not sure how.
# if ls was used on a dir twice wouldn't that be double counted?
# yeah, I was right. I guess this is only listed once though. you could fix it with this

# processed_dirs = set()

# for line in file():
#     match line.split():
#         case '$', 'ls':
#             dir_path = ''.join(curr)
#             if dir_path in processed_dirs:
#                 continue
#             processed_dirs.add(dir_path)




from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)
processed_dir = set()

for line in open('07.txt'):
    match line.split():
        case '$', 'cd', '/': curr = ['/']
        case '$', 'cd', '..': curr.pop()
        case '$', 'cd', x: curr.append(x+'/')
        case '$', 'ls': 
            dir_path = ''.join(curr)
            if dir_path in processed_dir:
                continue
            processed_dir.add(dir_path)
        case 'dir', _: pass
        case size, _:
            for p in accumulate(curr):
                dirs[p] += int(size)

print(sum(s for s in dirs.values() if s <= 100_000))
print(min(s for s in dirs.values() if s >= dirs['/'] - 40000000))
# just need to get all above 30000000 and then pick the smallest?

# https://github.com/silentw0lf/advent_of_code_2022/blob/main/07/solve.py
# also uses stack.pop() for `..`