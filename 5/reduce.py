def getElem():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line)
    return elem_list

polymer = getElem()[0]
print(polymer)

def isReductible(elem1, elem2):
    if abs(ord(elem1) - ord(elem2)) == 32:
        return True
    else:
        return False

def unitReduce(head, tail):
    next = tail.pop(0)

    if len(head)==0:
        head.append(next)
    else:
        if (isReductible(head[-1], next)):
            head.pop()
        else:
            head.append(next)
    return [head,tail]

def reducePolymer(polym):
    head = []
    tail = polym.copy()
    while len(tail)>0:
        [head, tail] = unitReduce(head, tail)
    return head

def purifyElem(elem,polym):
    result = []
    for val in polym:
        diff = abs(ord(elem) - ord(val))
        if (diff != 0) and (diff != 32):
            result.append(val)
    return result

polymer = list(getElem()[0].rstrip('\n'))

result = reducePolymer(polymer)

print('_',''.join(result),'_')
print(len(''.join(result)))

elemList = set([elem.upper() for elem in polymer])
print(elemList)

minL = len(polymer)
for elem in elemList:
    polymerR = purifyElem(elem, polymer)
    result = reducePolymer(polymerR)
    reducedLen = len(''.join(result))
    if reducedLen < minL:
        minL = reducedLen
        optimalElem = elem
    print('_',''.join(result),'_')

print(minL, optimalElem)