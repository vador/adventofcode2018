import re

def getList():
    eventList = []
    file = open('input', 'r')
    for line in file:
        eventList.append(line)
    return eventList


def parseEventRecord(event):
    eventre = re.compile(r"^\[(.*)\] (.*)\n$")
    eventgrp = eventre.match(event)
    timepart = eventgrp.group(1)
    msgpart = eventgrp.group(2)
    return [timepart, msgpart]

eventList = getList()

eventList.sort()
print(eventList)

print(parseEventRecord(eventList[0]))
print(parseEventRecord(eventList[1]))
print(parseEventRecord(eventList[2]))

