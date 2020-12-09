numbers = [int(number) for number in open("day09.txt")]


def findBadNumber():
    preamble = []
    for nextNumber in numbers:
        if len(preamble) < 25:
            preamble.append(nextNumber)
            continue
        else:
            foundBadNumber = True
            for x in preamble:
                if nextNumber - x in preamble:
                    foundBadNumber = False
                if not foundBadNumber:
                    preamble.pop(0)
                    preamble.append(nextNumber)
                    break
            if foundBadNumber:
                return nextNumber


def findEncryptionWeakness(badNumber):
    contiguousSet = []
    for nextNumber in numbers:
        if sum(contiguousSet) < badNumber:
            contiguousSet.append(nextNumber)
            continue
        else:
            while True:
                if sum(contiguousSet) > badNumber:
                    contiguousSet.pop(0)
                else:
                    break
            if sum(contiguousSet) == badNumber and len(contiguousSet) >= 2:
                contiguousSet.sort()
                return contiguousSet[0] + contiguousSet[-1]
            contiguousSet.append(nextNumber)


badNumber = findBadNumber()
print("Part 1:", badNumber)
print("Part 2:", findEncryptionWeakness(badNumber))
