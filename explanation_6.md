# Union and Intersection of two Linked Lists  
## Explanation  
### Data Structures  
Linked List  
Dictionary  
  

  
### Walktrough  
Defined a class **Node** initialized with value and next(to refer to next node) where value is the  
parameter to the initializer(constructor) and next is initialized to None.  
Under **Node** class defined `__repr__` method to return str of value of instance of node.  

Defined a class **LinkedList** initialized with head , tail and values. Head and tail are  
initialized to None and values is initialized as a dict().  

methods under class **LinkedList**  :

- **append(self,value)**  
appends new node to the linked list if it is distinct.  
It checks if the node is distinct or not.  
If node is distinct then it checks for head. If head is None then sets new_node as head  
If head is not None then checks for tail if tail is None then sets new_node as tail.  
If head and tail both are there then it sets new_node to the next of tail and makes the  
new_node tail of the linked list.  

- **is_distinct(self,value)**  
returns True or False as per the presence of the `value` in the `values` dict()  

- **size(self)**  
returns the size of the linked list  

- **__iter__(self)**  
```python
 def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
```
this method is defined so that we can iterate through the nodes  
eg.  
```python
for node in l1:
        map[str(node.value)] = node
        result.append(node)
```  
  
  
Functions  
  
**union(l1,l2)**  
uses a dict() `map` for mapping nodes of linked list.  
This function returns a LinkedList() object say `results`.  
For each node in 2nd linked list(say l1) it maps node to the dict()  
and appends node to the `results`  
For each node in 2nd linked list(say l2) if the node is not in the `map` dict() it appends  
the node to the results linked list  
At the end it returns the `results` linked list.  
  
**intersection(l1,l2)**  
uses a dict() `map` for mapping nodes of linked list.  
For each node in 1st linked list(say l1) it maps node to the dict()  
`results` linked list object is declared.  
For each node in 2nd linked list(say l2) if it is in the `map` then append to the `result`.  
And delete the node entry from `map` to avoid duplicates.  
At the end return `result`  
  

### Efficiency  
  
**Time Complexity**  
Append takes **O(1)** time as we are keeping track of head and tail.  
Time complexity will be **O(a+b)** where a is size of l1 and b is size of l2.  
  
**Space Complexity**  
It takes **O(a)** space where a is the size of final linked list obtained as a result  
of intersection or union.  
  
  
### Design Choice  
Keeping track of head and tail to perform `append()` in constant time.  
  
Used dict() to map nodes so that they can be accessed in **O(1)** time.  
  
Used `is_distinct()` method to maintain distinct nodes in the linked list.  
  

  
