# File Recursion
## Explanation  
  
### Data Structures  
**List**  
- To store files and dirs under a path  
#`os.listdir()` returns a list of dirs and files under a path.  
- To store `fullpath` for each entry a list is used.  
  
  
   
### Walkthrough  
Defied a function **find_files()** which takes suffix and path as parameters.  
This function returns the call of another function **_find_files()** which is defined
within it.  
_find_files() is called with path and files parameters as 
_find_files(path, files)  
The function find_files() returns _find_files(path,[])  
```python
def find_files(suffix,path):
    def _find_files(path,files):
        #
        #
        return files
    
    return _find_files(path,[])

```  
  
**find_files(path,files)**  
os.listdir(path) is used to list files and dirs under path,  
for each entry(file/dir) in the list a variable `fullpath` stores(as a string) the fullpath  
of the file/dir obtained by joining path to entry(file/dir name).  
Entry is checked if it is a dir or a file by checking its fullpath. If it is a dir, then  
the **_find_files(fullpath,files)** is called recursively on that dir and the result is stored  
in a variable `files`. Otherwise, if the entry is a file and its name ends with `suffix`  
then its `fullpath` is appended to the files list.  
(`fullpath` is the string obt. by joining path to entry)  
At the end of function the `files` list is returned.  

### Time Complexity
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
  

### Space Complexity
Space Complexity will be &nbsp; &nbsp; O(n)  
  

### Design Considerations
**List**  data structures is used  
There are no lookups in function  
The function just need to return a list  
  

**Conditions handled**  
- If no path is given  
```python
if not bool(path):
        return []
```  
  
- If falsey is given for suffix, set it to None to simplify the file suffix conditional  
check  
```python
if not bool(suffix):
        suffix = None
```
