
def getList():
    msglist = []
    file = open('input', 'r')
    for line in file:
        msglist.append(line)
    return msglist

def lettersCounter(msg):
    letterlist = {}
    for letter in msg:
        if letter in letterlist:
            letterlist[letter] += 1
        else:
            letterlist[letter] = 1
    return letterlist

def hasDoubleLetter(letterlist):
    for k in letterlist:
        if letterlist[k] == 2:
            return True
    return False

def hasTripleLetter(letterlist):
    for k in letterlist:
        if letterlist[k] == 3:
            return True
    return False

nbDouble = 0
nbTriple = 0

for msg in getList():
    msgLetters = lettersCounter(msg)
    if hasDoubleLetter(msgLetters):
        nbDouble += 1
    if hasTripleLetter(msgLetters):
        nbTriple += 1

print(nbDouble, nbTriple)
print(nbDouble*nbTriple)

print((lettersCounter('bababc')))