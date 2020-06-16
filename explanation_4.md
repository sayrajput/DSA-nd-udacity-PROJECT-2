# Active Directory  
## Explanation  
  
### Data Structures  
List  
Dictionary  
  
### Walkthrough  
Defined a class **Group** initialized with list `groups` and dictionary `users` and `_name` parameter  
that is passed as an arguement when creating instances of the Group class  
Under in the class **Group** some methods are defined which are  
- **add_group()** which appends a group to the list `groups`  
- **add_user()** which add a user in the dictionary `users`  
- **get_groups()** which returns all groups under a group as a list  
- **get_users()** which returns all users under a group as a list  
- **get_name()** returns the name of group  
  
  
A function named **is_user_in_group(user,group,result=None)** is used to check if a user is under a group.  
It takes `user` and `group` as arguement to return if the `user` is under `group`.  
If the user is present in users of current group then it returns True. Otherwise, it checks the group for  
subgroups under it. If any then for each subgroup the function calls itself recursively.  
And if user is found at any call i.e. in any subgroup then function returns True.  
If the user is not found in subgroups also and we have no group or subgroup under then the function just  
returns False.  
  
  
### Time Complexity  
Let g be the no. of groups and u be the no. of users to check in, then the time complexity will be **O(g+u)**  
for accessing these groups and users.  
  

### Space Complexity  
  


### Design Choice  
Dictionary - For faster lookups i.e. in O(1) time, used for storing users and checking for a particular user  
in `users` dictionary in O(1) time  
  
List - For storing groups, lists are fine here. As we have to each element in list(i.e. each group in list)  
for calling function recursively there is no need of data structure like dict() here. List is good for this.  
  
#None is used as value in dictionary to store users, as it requires less memory than anything like 0 or 1  

```python
def add_user(self,user):
    self.users[user] = None
```
