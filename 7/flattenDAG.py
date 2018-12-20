import re

class Node:
    orig = None
    dest = None
    parents = None

    def __init__(self, orig):
        self.orig = orig
        self.dest = set()
        self.parents = set()

    def addDest(self,dest):
        self.dest.add(dest)

    def addParent(self, parent):
        self.parents.add(parent)

def getElem():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line)
    return elem_list

def elemListToVectors(elem_list):
    vectre = re.compile(r"^Step (.+) must be finished before step (.+) can begin.")
    vector_list = []
    for elem in elem_list:
        orig = vectre.match(elem).group(1)
        dest = vectre.match(elem).group(2)
        vector_list.append((orig, dest))
    return vector_list


def fill_node_graph(vector_list):
    node_graph = {}
    for vector in vector_list:
        (orig, dest) = vector
        if orig not in node_graph:
            node_graph[orig] = Node(orig)
        if dest not in node_graph:
            node_graph[dest] = Node(dest)
        node_graph[orig].addDest(dest)
        node_graph[dest].addParent(orig)
    return node_graph

def collect_headlessNodes(node_list):
    headless = []
    for node in node_list:
        if len(node_list[node].parents) ==0:
            headless.append(node_list[node].orig)
    return headless

def remove_elem(node_list, elem):
    new_list = node_list.copy()
    for node in new_list:
        nn = new_list[node]
        if elem in nn.parents:
            nn.parents.remove(elem)
    new_list.pop(elem)
    return new_list


vector_list = elemListToVectors(getElem())
print(vector_list)

node_list = fill_node_graph(vector_list)
print(node_list)


while len(node_list):
    headless = collect_headlessNodes(node_list)
    #print(headless)
    headless.sort()
    r = headless.pop(0)
    print(r, end='')
    node_list = remove_elem(node_list, r)
print()
