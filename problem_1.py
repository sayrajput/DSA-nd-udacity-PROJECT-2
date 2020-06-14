class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU_Cache:
    def __init__(self,capacity):            
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
    
    
    def set(self, key, value):
        if self.capacity == 0:
            return -1
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return
        
        if len(self.cache) >= self.capacity:
            print("cache full..  removing least recently used node")
            self.remove_lru_node()
        
        node = Node(key,value)
        self._add(node)

        self.cache[key] = node
    

    def _remove(self, node):
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p
    
    def _add(self, node):
        t = self.tail
        tp = t.prev
        tp.next = node
        node.next = t
        node.prev = tp
        t.prev = node
        
    
    def get(self,key):
        if self.capacity == 0:
            return -1
        if key in self.cache:
            node = self.cache[key]
            n = node
            self._remove(node)
            self._add(node)
            return n.key
        return -1
    

    def remove_lru_node(self):
        r = self.head.next
        print(f"{r.key} to be removed")
        rn = r.next
        rp = self.head
        rp.next = rn
        rn.prev = rp
        del self.cache[r.key]
    

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " <-> "
            cur_head = cur_head.next
        out_string = "None <- "+out_string[:-4] + "-> None"
        return out_string





print("\n_______________________________________________________________________________")
print("Test Case 1..\n")
mylru = LRU_Cache(5)
print(mylru)               # None <- 0 <-> 0 -> None     Dummy Nodes only

print(mylru.get(9))        # -1 as 9 in not in mylru


print("\n_______________________________________________________________________________")
print("Test Case 2..")
mylru2 = LRU_Cache(0)
print(mylru2.set(2,2))             # -1
print(mylru2.get(2))               # -1

mylru3 = LRU_Cache(5)
mylru3.set(1,1)
mylru3.set(2,2)
mylru3.set(3,3)
mylru3.set(4,4)
mylru3.set(5,5)

print(mylru3)                         # None <- 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 0 -> None


print(mylru3.get(0))                 # -1
print(mylru3.get(13))                # -1
print(mylru3.get(6))                 # -1
print("\n________________________________________________________________________________________")
print("Test Case 3..")
print(mylru3.get(2))                 # 2
print(mylru3.get(5))                 # 5

mylru3.set(6,6)                      # capacity full, removes lru node .. 
print(mylru3.get(6))                 # 6
print(mylru3.get(1))                 # -1   as it was removed when 6 inserted

mylru3.set(13,13)                   # capacity full, removes lru node
print(mylru3.get(13))               # 13
print(mylru3.get(3))                # -1   as it was removed when 13 inserted

print(mylru3)                       # None <- 0 <-> 4 <-> 2 <-> 5 <-> 6 <-> 13 <-> 0 -> None
