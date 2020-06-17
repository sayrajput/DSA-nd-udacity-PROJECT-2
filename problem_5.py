import hashlib
from datetime import datetime


class Block(object):
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
    



class Blockchain:
    def __init__(self):
        self.blocks = dict()
        self.head = None
        self.tail = None
    
    def append_block(self,data):
        if data is None or len(data) ==  0:
            print("can't append block without data")
            return
        if self.head is None:
            block = Block(0, datetime.now(), data, "0" )
            self.head = block
            self.tail = self.head
            self.blocks[block.index] = block
            return
        
        last_block = self.tail

        block = Block(last_block.index+1,datetime.now(), data, last_block.hash )
        self.tail.next = block
        self.tail = block
        self.blocks[block.index] = block

    def size(self):
        return len(self.blocks)

    def get_block(self,index):
        if index in self.blocks:
            return self.blocks[index]
        return None
    



my_blockchain = Blockchain()

#Test1
my_blockchain.append_block(None)
#prints     can't append block without data


#Test 2
my_blockchain.append_block("")
#prints    can't append block without data

#Test 3
my_blockchain.append_block("Block 0")
my_blockchain.append_block("Block 1")
my_blockchain.append_block("Block 2")
my_blockchain.append_block("Block 3")

print(my_blockchain.head.data)
#prints   Block 0
print(my_blockchain.head.hash)
#prints hash of head i.e. hash of Block 0
print(my_blockchain.head.previous_hash)
# prints  0


print(my_blockchain.tail.data)
#prints   Block 3

print(my_blockchain.tail.previous_hash)
#prints hash of previous block i.e. hash of Block 2
print(my_blockchain.head.next.next.hash)
#prints hash of Block 2
print(my_blockchain.head.next.next.data)
#prints   Block 2

print(my_blockchain.head.next.data)
#prints   Block 1



#Test 4

print(my_blockchain.get_block(1))
#prints Block 1

print(my_blockchain.get_block(5))
#prints None
