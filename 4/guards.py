import re

class Night:

    def __init__(self):
        self.night = [0 for x in range(60)]

    def addSleep(self,fallsAsleep, wakesUp):
        for i in range(fallsAsleep, wakesUp):
            self.night[i] += 1

    def totalSleep(self):
        return sum(self.night)

    def getMaxMinute(self):
        return self.night.index(max(self.night))

    def getMaxSleep(self):
        return max(self.night)

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

def isWakeUp(event):
    if event[1] == "wakes up":
        return True
    else:
        return False

def isFallsAsleep(event):
    return (event[1]=="falls asleep")

def isBeginsShift(event):
    return (event[1][0:5] == "Guard")

def getGuardIdFromBeginEvent(event):
    if isBeginsShift(event):
        return int(event[1].split(" ")[1][1:])
    return

def parseDateTime(event):
    return event[0].split(' ')

def timePartToInt(timePart):
    [hour, min] = timePart.split(':')
    hour = int(hour)
    min = int(min)
    if hour>=1:
        min=0
    return min


def parseEvents(eventList):
    [curDate, curTime] = [0,0]
    nights = {}
    curGuard = 0
    #curGuard = getGuardIdFromBeginEvent(eventList[0])
    for event in [parseEventRecord(event) for event in eventList]:
        if isBeginsShift(event):
            curGuard = getGuardIdFromBeginEvent(event)
            [curDate, curTime] = parseDateTime(event)
            print()
            print(curDate, ' ', curTime, ' ', curGuard,' ', end='')
        [newDate, newTime] = parseDateTime(event)
        if (curDate != newDate):
            curDate = newDate
            curTime = newTime
            print()
            print(curDate, ' ', curTime, ' ', curGuard,' ', end='')
        if (isFallsAsleep(event)):
            curTime = newTime
            print('x', end='')
        if (isWakeUp(event)):
            if curGuard not in nights:
                nights[curGuard] = Night()
            nights[curGuard].addSleep(timePartToInt(curTime), timePartToInt(newTime))
            newTime = curTime
            print('_', end= '')
    print()

    return nights

def printEventList(eventList):
    for event in [parseEventRecord(event) for event in eventList]:
        print(event)
        print(isWakeUp(event), isFallsAsleep(event), isBeginsShift(event), getGuardIdFromBeginEvent(event))

nights = parseEvents(eventList)
guardsSleep = {}

sleeperGuard = max(nights, key=lambda key: nights[key].totalSleep())
print(sleeperGuard)
maxTimeOfSleep = nights[sleeperGuard].getMaxMinute()
print(maxTimeOfSleep)

print(sleeperGuard*maxTimeOfSleep)

maxMin = 0
maxSleep = 0
maxGuard = 0
for guard in nights.keys():
    curNight = nights[guard]
    if  curNight.getMaxSleep() > maxSleep:
        maxSleep = curNight.getMaxSleep()
        maxGuard = guard

print(nights[maxGuard].night)
print(maxGuard, ' ', nights[maxGuard].getMaxMinute(), '', maxSleep)
print(maxGuard*nights[maxGuard].getMaxMinute())