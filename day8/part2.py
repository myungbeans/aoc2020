def findAccBeforeLoop(filename):
    file = open(filename, 'r')
    operations = file.read().split('\n')[0:-1]  # last line is \n\n

    def nextCommandIndex(i, inputCommand):
        command = inputCommand.split(' ')
        operation = command[0]
        num = int(command[1])

        if operation == 'jmp':
            i += num
        else:
            i += 1

        return i

    allJumps = [i for i, x in enumerate(operations) if x.split(' ')[0] == 'jmp']
    flippedJumps = {}
    singleRun = {}
    i = 0
    accum = 0
    flippedThisRun = False

    # flip jmp to nop one at a time
    while True:
        # means we found a loop
        if i in singleRun:
            print('hit a loop', i, accum, singleRun)
            # reset
            i = 0
            accum = 0
            singleRun = {}
            flippedThisRun = False

        if len(flippedJumps) == len(allJumps):
            print("tried all jumps")
            break

        if i == len(operations):
            print('reached the end', accum)
            return accum

        command = operations[i].split(' ')
        operation = command[0]

        print(i, command, accum)

        if not flippedThisRun and operation == 'jmp' and i not in flippedJumps:
            flippedJumps[i] = command
            operation = 'nop'
            flippedThisRun = True
            print('flipping', i, operation)

        singleRun[i] = ' '.join([operation, command[1]])

        if operation == 'acc':
            accum += int(command[1])
        i = nextCommandIndex(i, ' '.join([operation, command[1]]))

    allNops = [j for j, x in enumerate(operations) if x.split(' ')[0] == 'nop']
    flippedNops = {}
    singleRun = {}
    j = 0
    accum = 0
    flippedThisRun = False

    # flip nop to jmp one at a time
    while True:
        # means we found a loop
        if j in singleRun:
            print('hit a loop', i, accum, singleRun)
            # reset
            j = 0
            accum = 0
            singleRun = {}
            flippedThisRun = False

        if len(flippedNops) == len(allNops):
            print("tried all nops")
            break

        if j == len(operations):
            print('reached the end', accum)
            return accum

        command = operations[j].split(' ')
        operation = command[0]

        print(j, command, accum)

        if not flippedThisRun and operation == 'jmp' and j not in flippedJumps:
            flippedJumps[j] = command
            operation = 'nop'
            flippedThisRun = True
            print('flipping', j, operation)

        singleRun[j] = ' '.join([operation, command[1]])

        if operation == 'acc':
            accum += int(command[1])
        j = nextCommandIndex(j, ' '.join([operation, command[1]]))


def main():
    return findAccBeforeLoop('input.txt')


if __name__ == "__main__":
    print(main())
