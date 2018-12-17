
curfreq = 0
file = open('input', 'r')
for line in file:
    deltafreq = int(line)
    curfreq += deltafreq

print(curfreq)

