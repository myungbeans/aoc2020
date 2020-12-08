def countAllAnsweredYes():
    file = open("input.txt", 'r')
    allGroups = file.read().split('\n\n')

    countYeses = 0

    for groupAnswers in allGroups:
        tmp = {}
        for q in list(groupAnswers.replace('\n', '')):
            tmp[q] = tmp[q]+1 if q in tmp else tmp.setdefault(q, 1)

        for key in tmp:
            if tmp[key] == len(filter(None, groupAnswers.split('\n'))):
                countYeses += 1
        tmp = {}

    return countYeses

print(countAllAnsweredYes())
