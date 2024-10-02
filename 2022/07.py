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

commands = sample.split("$ ")
for chunk in commands[:5]:
    # print(f">> {chunk}")
    lines = chunk.splitlines()
    for i in lines:
        print(i)