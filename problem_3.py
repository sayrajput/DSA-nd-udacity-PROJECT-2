import sys
import heapq

def huffman_encoding(data):
    if not bool(data):
        return '', None
    

    #Step1 Map the frequencies
    frequencies = map_frequency(data)

    #Step2 Build the Huffman Tree
    tree = build_tree(frequencies)

    #Step3 Map the codes from the Huffman Tree
    code_mappings = map_codes(tree, '', dict())

    #Step4 Encode the original data using the code mappings from the Huffman Tree
    encoding = ''
    for char in data:
        encoding += code_mappings[char]

    return encoding,tree


def huffman_decoding(data, tree):
    decoded = ''
    node = tree

    for bit in data:
        #walk to the left child
        if int(bit) == 0:
            if type(node) == HuffmanNode:
                node = node.left_child

        #walk to the right child
        else:
            if type(node) == HuffmanNode:
                node = node.right_child

        #if leaf, capture the char and rewind to the root
        if node.left_child is None and node.right_child is None:
            decoded += node.char
            node = tree
    
    return decoded




class HuffmanNode:
    def __init__(self, freq, char):
        self.freq = freq
        self.char = char
        self.left_child = None
        self.right_child = None



def map_frequency(data):
    frequencies = dict()
    
    if not bool(data):
        return frequencies
    
    total = 0
    for char in data:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
        total += 1
    
    map = list()

    #When there is a single character, set a dummy node to ensure that we can build the tree
    if len(frequencies) == 1:
        map.append((0, None, HuffmanNode(0, None)))
    

    for char,freq in frequencies.items():
        map.append((freq, char, HuffmanNode(freq, char)))
    
    return map


def build_tree(frequencies):
    if len(frequencies) == 0:
        return
    
    heapq.heapify(frequencies)
    p3 = 0
    while len(frequencies)>1:
        lt_freq, lt_char, lt_node = heapq.heappop(frequencies)
        rt_freq, rt_char, rt_node = heapq.heappop(frequencies)

         # Build the parent node
        p_freq = lt_freq + rt_freq
        parent = HuffmanNode(p_freq, None)
        parent.left_child = lt_node
        parent.right_child = rt_node

        #str(p3) is just in case to compare parent to a leaf
        #  when sorting the binary tree

        heapq.heappush(frequencies,(p_freq,str(p3),parent))
        p3 += 1
    
    root = heapq.heappop(frequencies)
    return root[2]



def map_codes(node, code, map):

    if type(node.left_child) is HuffmanNode:
        map_codes(node.left_child, code + '0', map)
    else:
        map[node.char] = code
    
    if type(node.right_child) is HuffmanNode:
        map_codes(node.right_child, code + '1', map)
    else:
        map[node.char] = code
    
    return map



if __name__ == '__main__':

    def run_edge_case_no_data():
        print("running no data given edge case ...")
        test_data = [
            '',
            None,
            False,
            {},
        ]

        for data in test_data:
            print(huffman_encoding(data))          #('',None)
        
    
    def run_edge_case_repeating_char():
        print("\nRunning edge case repeating char ...")
        test_data = [
            'aaaaaa',
            'bbbbbb',
            '1111111',
        ]

        for data in test_data:
            print("\nData: {}".format(data))                                     
            print("Data Size : {}".format(sys.getsizeof(data)))

            encoded_data, tree = huffman_encoding(data)
            print("Encoded : {}".format(encoded_data))
            print("Encoded Size: {}".format(sys.getsizeof(int(encoded_data, base=2))))

            
            decoded_data = huffman_decoding(encoded_data, tree)
            print("Decoded : {}".format(decoded_data))
            print("Decoded size: {}".format(sys.getsizeof(decoded_data)))



    def run_test_case():
        print("\nrunning test case")
        test_data = [
            'sanjay',
            'coding',
            'Huffman',
            'I am Sanjay',
            'Be Positive',
            'sayraj177@gmail.com'  
        ]

        for data in test_data:
            print("\nData : {}".format(data))
            print("Data Size: {}".format(sys.getsizeof(data)))

            encoded_data, tree = huffman_encoding(data)
            print("Encoded : {}".format(encoded_data))
            print("Encoded size : {}".format(sys.getsizeof(int(encoded_data, base = 2))))


            decoded_data = huffman_decoding(encoded_data, tree)
            print("Decoded : {}".format(decoded_data))
            print("Decoded size : {}".format(sys.getsizeof(decoded_data)))
    
    run_edge_case_no_data()
    print("_________________________________________________________")
    run_edge_case_repeating_char()
    print("_________________________________________________________")
    run_test_case()
    print("_________________________________________________________")
    
    
    
 
#output
"""

running no data given edge case ...
('', None)
('', None)
('', None)
('', None)
_________________________________________________________

Running edge case repeating char ...

Data: aaaaaa
Data Size : 55
Encoded : 111111
Encoded Size: 28
Decoded : aaaaaa
Decoded size: 55

Data: bbbbbb
Data Size : 55
Encoded : 111111
Encoded Size: 28
Decoded : bbbbbb
Decoded size: 55

Data: 1111111
Data Size : 56
Encoded : 1111111
Encoded Size: 28
Decoded : 1111111
Decoded size: 56
_________________________________________________________

running test case

Data : sanjay
Data Size: 55
Encoded : 11001011000111
Encoded size : 28
Decoded : sanjay
Decoded size : 55

Data : coding
Data Size: 55
Encoded : 1000110111100110
Encoded size : 28
Decoded : coding
Decoded size : 55

Data : Huffman
Data Size: 56
Encoded : 010001111100011101
Encoded size : 28
Decoded : Huffman
Decoded size : 56

Data : I am Sanjay
Data Size: 60
Encoded : 11101101000111011111001000010011
Encoded size : 32
Decoded : I am Sanjay
Decoded size : 60

Data : Be Positive
Data Size: 60
Encoded : 10110010101100110111100111110110000
Encoded size : 32
Decoded : Be Positive
Decoded size : 60

Data : sayraj177@gmail.com
Data Size: 68
Encoded : 0110110011101011100010111011001001111000001011100001001111100111110100101
Encoded size : 36
Decoded : sayraj177@gmail.com
Decoded size : 68
_________________________________________________________


"""
