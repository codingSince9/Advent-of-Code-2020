import math

boardingPasses = []
seats = []

for boardingPass in open("day05.txt"):
    boardingPasses.append(boardingPass.strip())

highestID = 0
for boardingPass in boardingPasses:
    upperRowBoundary = 127
    lowerRowBoundary = 0
    upperColumnBoundary = 7
    lowerColumnBoundary = 0
    for char in boardingPass:
        if char == 'B':
            lowerRowBoundary = math.ceil((lowerRowBoundary + upperRowBoundary)/2)
        elif char == 'F':
            upperRowBoundary = int((lowerRowBoundary + upperRowBoundary)/2)
        elif char == 'R':
            lowerColumnBoundary = math.ceil((lowerColumnBoundary + upperColumnBoundary)/2)
        else:
            upperColumnBoundary = int((lowerColumnBoundary + upperColumnBoundary)/2)

    seatID = upperRowBoundary * 8 + upperColumnBoundary
    seats.append(seatID)
    if seatID > highestID:
        highestID = seatID

print("Part 1:", highestID)

seats.sort()
counter = 0
for x in seats:
    if x - seats[counter+1] == -2 and x+1 not in seats:
        print("Part 2:", x+1)
        break
    counter += 1
