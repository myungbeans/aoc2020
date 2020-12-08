def highestSeatId():
    file = open("input.txt", 'r')
    allSeats = file.read().split('\n')

    maxId = 0

    for seat in allSeats:
        currentRow = 0
        currentCol = 0

        rowMin = 0
        rowMax = 127
        colMin = 0
        colMax = 7

        fbBinary = list(seat)[0:7]
        lrBinary = list(seat)[7:11]

        for i, el in enumerate(fbBinary):
            if el == 'F':
                rowMax = rowMax - 128/(2**(i+1))
            else:
                rowMin = rowMin + 128/(2**(i+1))
            if i == 6:
                currentRow = rowMin if el == 'F' else rowMax

        for i, el in enumerate(lrBinary):
            if el == 'L':
                colMax = colMax - 8/(2**(i+1))
            else:
                colMin = colMin + 8/(2**(i+1))

            if i == 2:
                currentCol = colMin if el == 'F' else colMax

        id = (currentRow * 8) + currentCol
        maxId = id if id > maxId else maxId

    return maxId

print(highestSeatId())
