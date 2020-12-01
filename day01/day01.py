entries = []

with open("day01/day01.txt", "r") as f:
    for entry in f:
        entries.append(int(entry))

foundSumOf2 = False
foundSumOf3 = False
for entry in entries:
    for entry2 in entries:
        if entry + entry2 == 2020 and not foundSumOf2:
            print(entry * entry2)
            foundSumOf2 = True
        for entry3 in entries:
            if entry + entry2 + entry3 == 2020 and not foundSumOf3:
                print(entry * entry2 * entry3)
                foundSumOf3 = True
            if foundSumOf3:
                break
        if foundSumOf2:
            break
    if foundSumOf2 and foundSumOf3:
        break