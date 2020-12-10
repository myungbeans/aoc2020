def findAccBeforeLoop(filename):
    file = open(filename, 'r')
    operations = file.read().split('\n')[0:-1]  # last line is \n\n

    def nextCommandIndex(i, inputCommand):
        command = inputCommand.split(' ')
        operation = command[0]
        num = int(command[1])

        i = i + num if operation == 'jmp' else i + 1
        return i

    accum = {
        'current': 0,
        'prev': None
    }

    # Naiive
    # commandsExecuted = {}
    # i = 0

    # while True:
    #     if i in commandsExecuted:
    #         break
    #     commandsExecuted[i] = operations[i]
    #     command = operations[i].split(' ')
    #     if command[0] == 'acc':
    #         accum['prev'] = accum['current']
    #         accum['current'] += int(command[1])

    #     i = nextCommandIndex(i, operations[i])
    # print(commandsExecuted, i)

    # return accum['current']

    # Tortoise & Hare

    slow = 0
    fast = 0

    # Find if loop exists
    while True:
        # jump 1
        slow = nextCommandIndex(slow, operations[slow])
        # break if no loop
        if slow == len(operations) - 1:
            return None

        # jump 2
        fast = nextCommandIndex(fast, operations[fast])
        fast = nextCommandIndex(fast, operations[fast])
        # break if no loop
        if fast == len(operations) - 1:
            return None

        print(slow, fast)

        # break if found loop
        if slow == fast:
            break

    print('met at', slow, fast)

    slow = 0
    singleRun = 0

    # Find start of loop
    while slow != fast:
        print(slow, fast)
        slow = nextCommandIndex(slow, operations[slow])
        fast = nextCommandIndex(fast, operations[fast])
        singleRun += 1

    for i in range(singleRun):
        command = operations[i].split(' ')
        if command[0] == 'acc':
            accum['prev'] = accum['current']
            accum['current'] += int(command[1])
        print (i, accum)
        i = nextCommandIndex(i, operations[i])
    return accum['current']


def main():
    return findAccBeforeLoop('test.txt')


if __name__ == "__main__":
    print(main())
