
def getFreqList():
    freqlist = []
    file = open('input', 'r')
    for line in file:
        deltafreq = int(line)
        freqlist.append(deltafreq)
    return freqlist



def createGeneratorFromList(mylist):
    while True:
        head = mylist.pop(0)
        mylist.append(head)
        yield head

freqlist = getFreqList()
freqGen = createGeneratorFromList(freqlist)
freqSeen = {}
curFreq = 0
freqSeen[curFreq] = True
for nextfreq in freqGen:
    curFreq += nextfreq
    if curFreq in freqSeen:
        print(curFreq)
        exit()
    else:
        freqSeen[curFreq] = True



