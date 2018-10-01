#collatz conjecture
import datetime

def sugma(balls):
    level = 1
    if balls == 1:
        return 1
    elif balls % 2 == 0:
        level += sugma(balls/2)
    else:
        level += sugma(balls * 3 + 1)
    return level
maxsteps = 0
max = 0
stepstotal = 0
print(datetime.datetime.now())
for i in range(1000000):
    if sugma(i + 1) > maxsteps:
        max = i + 1
        maxsteps = sugma(i + 1)
    stepstotal += sugma(i + 1)
    #print(i + 1, " requires ", sugma(i + 1), " steps")
print(max, maxsteps)
print(datetime.datetime.now())
print(stepstotal)
