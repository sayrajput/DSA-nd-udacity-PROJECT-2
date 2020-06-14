# File Recursion
## Explanation
#### Time Complexity
Worst case time complexity    O(n)

os.listdir()  returns a python list of files and directories
for each entry in list check if file
It mostly depends on the number of files and directories(subdirectories included) available under searched directory
let's take no. of dirs      d
and no. of files            f
Time complexity will more affected how many times the functions runs
which is based on no. of files and dirs

so time complexity will be O(d+f)


For the particular directory provided in the problem:
we have directories:
    testdir , subdir1 , subdir2, subdir3, susubdir1, subdir4 , subdir5    total = 7
we have files:
a.c , a.h, .gitkeep, b.c, b.h, .gitkeep,  a.c ,  a.h, t1.c, t1.h          total = 10

So time complexity for this problem with this directory is     O(7 + 10) = O(17)
