class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.values = dict()
    
    def append(self,value):
        if not self.is_distinct(value):
            return
        
        new_node = Node(value)
        self.values[str(value)] = new_node

        if self.head is None:
            self.head = new_node
        
        elif self.tail is None:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
    

    def is_distinct(self,value):
        return str(value) not in self.values
    

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        
        return size
    

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        
        return out_string

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next



def union(l1, l2):
    map = dict()
    result = LinkedList()

    for node in l1:
        map[str(node.value)] = node
        result.append(node)
    
    for node in l2:
        value = str(node.value)
        if value not in map:
            map[value] = node
            result.append(node)
    
    return result


def intersection(l1,l2):
    map = dict()

    for node in l1:
        map[str(node.value)] = node

    result = LinkedList()

    for node in l2:
        value = str(node.value)
        if value in map:
            result.append(node)
            del map[value]    #to avoid duplicates
    
    return result



if __name__ == '__main__':

    def result(out):
        if out.size() == 0:
            print("None found")
        else:
            print(out)
    
    def test_case1():
        print("\nRunning Test Case 1 .. ")
        list1 = LinkedList()
        list2 = LinkedList()

        out = union(list1, list2)
        result(out)                     #None found
        
        out = intersection(list1, list2)
        result(out)                     #None found
        
        list1.append(5)
        out = union(list1,list2)
        result(out)           # 5 ->
       
        out = intersection(list1, list2)
        result(out)                          #None found
    

    def test_case2():
        print("\nRunning Test Case 2 ..")
        list1 = LinkedList()
        list2 = LinkedList()

        for value in [4,5,2,3,7,8,9,13]:
            list1.append(value)
        
        for value in [5,6,1,13,10,8,15]:
            list2.append(value)
        
        out = union(list1,list2)
        result(out)          #4 -> 5 -> 2 -> 3 -> 7 -> 8 -> 9 -> 13 -> 6 -> 1 -> 10 -> 15 ->
        out = intersection(list1,list2)
        result(out)   #5 -> 13 -> 8 ->
    

    def test_case3():
        print('\nTest case 3...')
        list1 = LinkedList()
        list2 = LinkedList()

        for value in [15, 2, 4, 5, 6, 9, 2, 4, 1, 12]:
            list1.append(value)

        for value in [10, 7, 8, 14, 11, 21, 16]:
            list2.append(value)

        out = union(list1, list2)
        result(out)            # 15 -> 2 -> 4 -> 5 -> 6 -> 9 -> 1 -> 12 -> 10 -> 7 -> 8 -> 14 -> 11 -> 21 -> 16 ->
        out = intersection(list1, list2)
        result(out)                    #None found




    

    test_case1()
    print("_____________________________________________________________________")
    test_case2()
    print("_____________________________________________________________________")
    test_case3()
    print("_____________________________________________________________________")
