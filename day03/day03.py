area = []

for x in open("day03.txt", "r"):
    area.append(x.strip())


def checkSlope(right, down):
    downCounter = 0
    location = 0
    treeCounter = 0
    wait = False
    for line in area:
        if line[location] == '#' and not wait:
            treeCounter += 1

        if not wait:
            locationSet = False
            for i in range(right):
                if location + right == len(line) + i:
                    location = i
                    locationSet = True

            if not locationSet:
                location += right

        if downCounter < down:
            downCounter += 1
            if downCounter != down:
                wait = True
            else:
                downCounter = 0
                wait = False
            continue

    return treeCounter


allTrees = checkSlope(3, 1)
print("Part 1:", allTrees)
allTrees *= checkSlope(1, 1)
allTrees *= checkSlope(5, 1)
allTrees *= checkSlope(7, 1)
allTrees *= checkSlope(1, 2)
print("Part 2:", allTrees)
