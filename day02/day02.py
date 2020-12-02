passwords = []

with open("day02.txt", "r") as f:
    for password in f:
        passwords.append(password.strip())

validPasswordCounter = 0
validPasswordCounter2 = 0
for password in passwords:
    letterCounter = 0
    minimum = int(password.split('-')[0])
    maximum = int(password.split('-')[1].split()[0])
    
    password = password.split(':')
    letter = password[0][-1]

    password = password[1].strip()

    for char in password:
        if char == letter:
            letterCounter += 1

    if minimum <= letterCounter <= maximum:
        validPasswordCounter += 1

    if (letter == password[minimum-1] and letter != password[maximum-1]) or (letter != password[minimum-1] and letter == password[maximum-1]):
        validPasswordCounter2 += 1

print("Part 1:", validPasswordCounter)
print("Part 2:", validPasswordCounter2)
