class Node:
    name = None
    children = None
    metadata = None
    value = None
    childrens = 0
    metadatas = 0

    def __init__(self, childrens, metadatas, name=None):
        self.name = name
        self.childrens = childrens
        self.metadatas = metadatas
        self.children = []
        self.metadata = []

    def addChild(self,child):
        self.children.append(child)

    def addMetadata(self,metadata):
        self.metadata.append(metadata)

    def getNodeValue(self):
        if self.value is not None:
            return self.value
        else:
            if self.childrens == 0:
                self.value = sum(self.metadata)
                return self.value
            else:
                self.value = self.countChildValues()
                return self.value

    def countChildValues(self):
        tmpVal = 0
        for index in self.metadata:
            if 0 < index <= self.childrens:
                tmpVal += self.children[index-1].getNodeValue()
        return tmpVal

def getElem():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line.rstrip('\n'))
    return elem_list

elem_list = getElem()[0].split(' ')

def readMetadata(node, value_list):
    for i in range(node.metadatas):
        node.addMetadata(int(value_list.pop(0)))

def addNode(curNode, value_list):
    while curNode.childrens > len(curNode.children):
        c = int(value_list.pop(0))
        m = int(value_list.pop(0))
        node = Node(c, m)
        curNode.addChild(node)
        addNode(node, value_list)

    readMetadata(curNode, value_list)

def getMetadataSum(root):
    tmpSum = 0
    for node in root.children:
        tmpSum += getMetadataSum(node)
    if root.metadata is not None:
        tmpSum += sum(root.metadata)
    return tmpSum

def checkTree(node):
    if node.metadatas != len(node.metadata):
        print("metadata err")
        return False
    if node.childrens != len(node.children):
        print("children err")
        return False
    tmpBool = True
    for child in node.children:
        tmpBool = tmpBool and checkTree(child)
    return tmpBool

c = int(elem_list.pop(0))
m = int(elem_list.pop(0))
root = Node(c,m)
addNode(root, elem_list)
print(root)
print(getMetadataSum(root))
print(root.getNodeValue())

print(checkTree(root))