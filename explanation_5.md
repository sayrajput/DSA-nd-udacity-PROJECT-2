# Blockchain  
## Explanation  
  
### Data Structures  
Linked List  
Dictionary  
  
### Walkthrough  
Defined a class **Block** initialized with index,timestamp,data,previous_hash, hash,  
next(reference to the next block) where  index, timestamp , data and previous_hash are parameters to the constructor  
  
`calc_hash()` is method under **Block** class, which calculated hash value of a block.  
This function uses index,timestamp,data and previous_hash to generate unique hash for each  
block.  
  

Defined a class **Blockchain** initialized with blocks `dict()` , head and tail. Head and  
tail are initialized with `None`  
  
Methods under **Blockchain** class are :  
  
- **append_block()**  which appends a new block to the blockchain. If no data provided for  
the new block, it returns 'can't append block without data'  .
```python
if data is None or len(data) ==  0:
            print("can't append block without data")
            return
```
A block is created as an instance of **Block** class with data provided.  

If blockchain is empty i.e. if head is None , then new block will become head of the  
blockchain and tail will be equal to head as there is only one block in blockchain.
```python
if self.head is None:
            block = Block(0, datetime.now(), data, "0" )
            self.head = block
            self.tail = self.head
            self.blocks[block.index] = block
            return
```
If head is not None i.e. the blockchain is not empty, then the new block will be added  
next to the tail of the blockchain. And the block added will be made the tail of blockchain.  
This new block will be added to `blocks` dictionary  
```python
self.blocks[block.index] = block
```  
  
- **size()** returns the size of blocks dictionary  
- **get_block()** returns a block with index provided. Looks for index in the `blocks` dict()  
  
### Efficiencies  

`Time Complexity`  O(1) for inserting and looking up a block  

`Space Complexity`  O(1) for inserting and looking up a block  
  


### Design Choice  
Used `blocks` dict() to access blocks with index in **O(1)** time.  
  
Keeping track of the tail of blockchain so that new block can be added in **O(1)**  
i.e. the block is added next to the tail and then the new block is made tail.  
```python
 block = Block(last_block.index+1,datetime.now(), data, last_block.hash )
        self.tail.next = block
        self.tail = block
        self.blocks[block.index] = block
```
  
Used all data i.e. data,index,timestamp and previous_hash to generate unique hash for  
each block.  
```python
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
```  
  


