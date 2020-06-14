# File Recursion
## Explanation
#### Time Complexity
Worst case time complexity  &nbsp;&nbsp;&nbsp;  O(n)

os.listdir()  returns a python list of files and directories  
It mostly depends on the number of files and directories(subdirectories included) available under searched  directory  
let's take no. of dirs    &nbsp;&nbsp;&nbsp;  d  
and no. of files      &nbsp;&nbsp;&nbsp;&nbsp;  f  
Time complexity will more affected how many times the functions runs  
which is based on no. of files and dirs  
  
so time complexity will be &nbsp; O(d+f)  


For the particular directory provided in the problem:
we have directories:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; testdir , subdir1 , subdir2, subdir3, susubdir1, subdir4 , subdir5  &nbsp;&nbsp;  total = 7  
we have files:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a.c , a.h, .gitkeep, b.c, b.h, .gitkeep,  a.c ,  a.h, t1.c, t1.h    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  total = 10  
  

so time complexity for this problem with this directory is &nbsp;&nbsp;    O(7 + 10) = O(17)

