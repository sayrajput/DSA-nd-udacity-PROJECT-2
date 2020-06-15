# LRU Cache    
  
# Explanation    
### Data Structures    
  
 - Doubly Linked List  
 - Dictionary  

### Time Complexity 
  
As dictionary is used lookups will take **O(1)** time  
i.e. **get()** will take O(1) time  
Also **set()** &nbsp; &nbsp; **_remove()** &nbsp; &nbsp; **_add()** &nbsp; &nbsp; **remove_lru_node()** will take  
O(1) time as there is no need to traverse the complete linked list we are just changing pointers  
##### set()  
 - calling _remove() and _add() method 
 - calling _remove_lru_node() method  
 - storing node in dictionary for lookups in O(1) time   
   overall it results in O(1) time  

##### _add()  
- just setting the node before the tail by changing references of the node previous to tail and tail itself
  which takes **O(1)** time  
  
##### _remove()  
- just changing the reference of previous and next node of the node to be removed  
which takes **O(1)** time  
  
##### _remove_lru_node()  
- we have to remove lru node that is next to the dummy head  
so just change the refrence of head to the next element of the node to be removed and change the prev.   reference of that element to the head  
which also takes **O(1)** time 
  
  

### Space Complexity  
Doubly Linked List &nbsp; &nbsp; **O(n)**  
Dictionary(Hashtable) &nbsp; &nbsp; **O(n)**  
  


#### Dummy Head and Tail Nodes  
To reduce code complexity, a dummy head and tail node is used.  
It eliminates checking if there's a head or tail and then setting or resetting either as needed.  This technique is a common   approach.  
  


