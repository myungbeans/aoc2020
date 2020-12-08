import re


def mySeatId():
    file = open("input.txt", 'r')
    allSeats = file.read().split('\n')[0:-1]

    for i, seat in enumerate(allSeats):
        allSeats[i] = re.sub(r'F|L', '0', allSeats[i])
        allSeats[i] = re.sub(r'R|B', '1', allSeats[i])

    allSeats.sort()

    i = 0
    while i < len(allSeats) - 2:
        if getIdVal(allSeats[i+1]) - getIdVal(allSeats[i]) == 2:
            print(getIdVal(allSeats[i]), getIdVal(allSeats[i+1]))
            return getIdVal(allSeats[i]) + 1
        i += 1


def getIdVal(seat):
    print('Getting id val')
    currentRow = 0
    currentCol = 0

    rowMin = 0
    rowMax = 127
    colMin = 0
    colMax = 7

    fbBinary = list(seat)[0:7]
    lrBinary = list(seat)[7:11]

    for i, el in enumerate(fbBinary):
        if el == '0':
            rowMax = rowMax - 128/(2**(i+1))
        else:
            rowMin = rowMin + 128/(2**(i+1))
        if i == 6:
            currentRow = rowMin if el == 'F' else rowMax

    for i, el in enumerate(lrBinary):
        if el == '0':
            colMax = colMax - 8/(2**(i+1))
        else:
            colMin = colMin + 8/(2**(i+1))

        if i == 2:
            currentCol = colMin if el == 'F' else colMax

    return (currentRow * 8) + currentCol

print (mySeatId())
