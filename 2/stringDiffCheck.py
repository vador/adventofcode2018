def getList():
    msglist = []
    file = open('input', 'r')
    for line in file:
        msglist.append(line)
    return msglist


def stringDiffCalculator(msg1, msg2):
    nbDiff = 0
    for i in range(len(msg1)):
        if msg1[i] != msg2[i]:
            nbDiff += 1
    return nbDiff

def stringCommonLetters(msg1, msg2):
    common = ""
    for i in range(len(msg1)):
        if msg1[i] == msg2[i]:
            common += msg1[i]
    return common

msgList = getList()
nbMsg = len(msgList)

for i in range(nbMsg):
    for j in range(i+1, nbMsg):
        if stringDiffCalculator(msgList[i], msgList[j]) == 1:
            print(i,j)
            print(msgList[i])
            print(msgList[j])
            print(stringCommonLetters(msgList[i], msgList[j]))
