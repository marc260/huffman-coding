class HuffmanTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return "%s_%s" % (self.left, self.right)

## Tansverse the NodeTress in every possible way to get codings
def huffmanCodeTree(node, left=True, binString=""):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    tree = dict()
    tree.update(huffmanCodeTree(l, True, binString + "0"))
    tree.update(huffmanCodeTree(r, False, binString + "1"))
    return tree

def huffmanCoding(string):
    frequencyList = {}
    for char in string:
        if char in frequencyList: #count frequency of char in the string
            frequencyList[char] += 1
        else:
            frequencyList[char] = 1

    # Sort the frequency table based on occurrence this will also convert the
    # dict to a list of tuples
    frequencyList = sorted(frequencyList.items(), key=lambda x: x[1], reverse=True)

    nodes = frequencyList

    while len(nodes) > 1:
        keyLeft, freqLeft = nodes[-1]
        keyRight, freqRight = nodes[-2]#
        nodes = nodes[:-2]#removes first 2 nodes from PQ
        parentNode = HuffmanTree(keyLeft, keyRight)
        nodes.append((parentNode, freqLeft + freqRight))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)# Re-sort the list

    huffmanCode = huffmanCodeTree(nodes[0][0])#start running the tree by the root

    #PRINT
    print("\n Character | Frequency  | Huffman code ")
    print("-----------------------------------------")
    for char, frequency in frequencyList:
        print(" %-9r | %10d | %12s" % (char, frequency, huffmanCode[char]))

    count = 0
    print("\nThe encoded string is:")
    for char in string:
        print(huffmanCode[char], end='')
        count += len(huffmanCode[char])

    print("\n\nThe total length of coding is:")
    print(count)

def getString(filename):  # Get graph from file
    file = open(filename, "r", encoding='utf-8')
    lines = file.readlines()
    string = ' '.join(lines)
    return string

string = "mississippi"
print("Input 1: " + string)
huffmanCoding(string)

stringFile = getString('snark.txt')
print('\nInput 2: snark.txt:')
huffmanCoding(stringFile)