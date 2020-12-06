f = open("day06.txt")
lines = f.readlines()
groupAnswers = []
answers = {}
yesAnswerCounter = 0
everyoneYesCounter = 0
counter = 0
personCounter = 0


def check():
    if line == '\n':
        return
    for char in line:
        if char not in groupAnswers and char != '\n':
            groupAnswers.append(char)
    answers[personCounter] = line.strip()


for line in lines:
    counter += 1
    if line != '\n':
        personCounter += 1
    if counter == len(lines):
        check()
        yesAnswerCounter += len(groupAnswers)
    else:
        check()
    if line == '\n':
        yesAnswerCounter += len(groupAnswers)
        groupAnswers = []

    if line == '\n' or counter == len(lines):
        if len(answers) == 1:
            everyoneYesCounter += len(answers[1])
        else:
            first = False
            sameAnswers = {}
            for key in answers.keys():
                if not first:
                    for char in answers[key]:
                        sameAnswers[char] = 1
                    first = True
                    continue
                for char in answers[key]:
                    if char in sameAnswers.keys():
                        sameAnswers[char] += 1
            for key in sameAnswers.keys():
                if sameAnswers[key] == personCounter:
                    everyoneYesCounter += 1

        answers = {}
        personCounter = 0

print("Part 1:", yesAnswerCounter)
print("Part 2:", everyoneYesCounter)
