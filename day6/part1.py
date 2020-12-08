def countQuestionsAnsweredYes():
    file = open("input.txt", 'r')
    allGroups = file.read().split('\n\n')

    countYeses = 0

    tmp = {}
    print(allGroups)
    for groupAnswers in allGroups:
        answerSet = groupAnswers.replace('\n', '')
        for q in list(answerSet):
            tmp[q] = q
        print(len(tmp))
        countYeses += len(tmp)
        tmp = {}

    return countYeses

print(countQuestionsAnsweredYes())
