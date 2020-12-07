bags = {}
bagsWithNumbers = {}
shinyBags = []
SHINY_GOLD = 'shiny gold'


def checkIfShiny(bag, key):
    if bag in shinyBags:
        bags[key] = SHINY_GOLD
        shinyBags.append(key)


def countBags(key):
    if len(bagsWithNumbers.get(key)) == 1:
        if bagsWithNumbers.get(key)[0] == 'no other bags':
            return 0
        number = int(bagsWithNumbers.get(key)[0].split()[0])
        bag = ' '.join(bagsWithNumbers.get(key)[0].split()[1:3]).strip()
        return number + number * countBags(bag)
    else:
        total = 0
        for value in bagsWithNumbers.get(key):
            number = int(value.split()[0])
            bag = ' '.join(value.split()[1:3]).strip()
            total += number + number * countBags(bag)
        return total


for bag in open("day07.txt"):
    bag = bag.strip('.\n')
    mainBag = ' '.join(bag.split()[:2])
    containsBags = bag.split('contain')[1].split(',')
    containsBags = [x[2:-4].strip() if 'bag' in x else x[2:-5].strip() for x in containsBags]
    bags[mainBag] = containsBags

    containWithNumbers = bag.split('contain')[1].split(',')
    containWithNumbers = [x[1:] for x in containWithNumbers]
    bagsWithNumbers[mainBag] = containWithNumbers

    for x in containsBags:
        if x == SHINY_GOLD:
            shinyBags.append(mainBag)
            break


def part1():
    change = True
    goldBagsCounter = 0
    while change:
        size = len(shinyBags)
        for key, value in bags.items():
            if len(value) > 1:
                for v in value:
                    checkIfShiny(v, key)
            else:
                checkIfShiny(value[0], key)

        if size == len(shinyBags):
            change = False

    for value in bags.values():
        if SHINY_GOLD in value:
            goldBagsCounter += 1

    return goldBagsCounter


def part2():
    number = int(bagsWithNumbers.get(SHINY_GOLD)[0].split()[0])
    bag = ' '.join(bagsWithNumbers.get(SHINY_GOLD)[0].split()[1:3]).strip()
    return number + number * countBags(bag)


print("Part 1:", part1())
print("Part 2:", part2())
