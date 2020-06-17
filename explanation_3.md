# Huffman Coding  
## Explanation  
  

### Data Structures  
Tree  
Heap  
Dictionary  
List  


### Walkthrough  
  
Defined a class **HuffmanNode** for creating node for huffman tree. This class is initialized  
with freq, char, left_child and right_child where freq and char are provided as parameters  
For initialization left_child and right_child are set to None.  
  

  
#### Defined functions  
-  **map_frequency()** which uses a dict() `frequencies` which stores  
frequency of each char in data.  
  A list named `map` is defined to store freq,char and the HuffmanNode with those freq and char.  
    

- **build_tree()** which takes frequencies and builds a huffman tree from frequencies.  
#Heapify the frequencies list  
while there are more than one frequencies in `frequencies` .
pop() two entries from the heapified list `frequencies`   
`heappop()` pops the entry with minimum freq.  
It pops the tuple (freq, char,node) from list . 
Here, we pop 2 entries and store the values of 2 as:  
```python
    lt_freq, lt_char, lt_node = heapq.heappop(frequencies)
    rt_freq, rt_char, rt_node = heapq.heappop(frequencies)
```  
Now we have to build a new node from these popped entries and push the new entry in heap as:  
```python
         # Build the parent node
        p_freq = lt_freq + rt_freq
        parent = HuffmanNode(p_freq, None)
        parent.left_child = lt_node
        parent.right_child = rt_node

        heapq.heappush(frequencies,(p_freq,str(p3),parent))
```
  
- **map_codes()**  
Maps nodes of tree into codes of '0' and '1' into a dict()  
For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child.   



- **huffman_encoding()** which takes `data` as parameter and returns  
encoded data and tree.  
#step 1 Mapping the frequencies  
calls the **map_frequency()** function for mapping frequencies of `data`  
#step 2 Build the huffman tree  
calls the **build_tree()** function on frequencies. 
  
#Step3 Map the codes from the Huffman Tree  
calls the **map_codes()** function  

#Step4 Encode the original data using the code mappings from the Huffman Tree  
for each char in data add its code mapping to the encoded string.  
  


Defined a function **huffman_decoding()** which decodes the data according to the tree.  
  
For each bit in encoded data, if int(bit) is 0 i.e. if 0 encountered then walk to the left  
child. Otherwise walk to the right child  
Now at the end , if leaf is encountered capture the char and rewind to the root.  
If node's left_child and right_child are None then its a leaf node.  
Add the char of node to the decoded string.  
  

  


### Efficiency  
**Time Complexity**  
Overall time complexity is **O(nlogn)**  
How ?  
Dictionary is used for mapping so it takes O(1) to get values from map  
For adding values to dictionary it will take O(n) time  
**heappush()** method takes O(logn) time, for n elements it will take **O(nlogn)** time  
  
**Space Complexity**  
It requires **O(n)** space  
  
  
### Design Choice  
Used heap(using heapq) to implement priority queue as it is operated simply.  
Dictionary is used to map codes and frequencies so that they can be accessed in O(1) time  
  
