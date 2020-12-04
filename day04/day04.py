passports = []
requiredFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
validHairColor = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
eyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

samePassport = ""
f = open("day04.txt", "r")
lines = f.readlines()
for line in lines:
    if line == lines[-1] and len(samePassport) != 0:
        samePassport += " " + line.strip()
        passports.append(samePassport)
    if line == '\n':
        passports.append(samePassport)
        samePassport = ""
    else:
        if len(samePassport) != 0:
            samePassport += " " + line.strip()
        else:
            samePassport += line.strip()
            if line == lines[-1]:
                passports.append(samePassport)


validPassportCounter = 0
validPassportCounter2 = 0
for passport in passports:
    passportFields = []
    fields = [field.split(':')[0] for field in passport.split(' ')]
    fieldValues = [value for value in passport.split(' ')]
    fields.sort()
    requiredFields.sort()

# PART 1--------------------
    for field in fieldValues:
        if field.split(':')[0] == 'cid':
            fieldValues.remove(field)
            break

    if 'cid' in fields:
        fields.remove('cid')
    if fields == requiredFields:
        validPassportCounter += 1

# PART 2--------------------
    invalid = False
    for fieldValue in fieldValues:
        field, value = fieldValue.split(':')[0], fieldValue.split(':')[1]

        if field == 'byr' and not 1920 <= int(value) <= 2002:
            invalid = True
            break

        if field == 'iyr' and not 2010 <= int(value) <= 2020:
            invalid = True
            break

        if field == 'eyr' and not 2020 <= int(value) <= 2030:
            invalid = True
            break

        if field == 'hgt':
            number = ""
            unit = ""
            for char in value:
                if char.isdigit():
                    number += char
                else:
                    unit += char
            if unit == 'cm' and not 150 <= int(number) <= 193:
                invalid = True
                break
            elif unit == 'in' and not 59 <= int(number) <= 76:
                invalid = True
                break
            elif unit != 'cm' and unit != 'in':
                invalid = True
                break

        if field == 'hcl':
            first = True
            invalid = False
            if len(value) != 7:
                invalid = True
                break
            for char in value:
                if char != '#' and first:
                    invalid = True
                    break
                elif char == '#':
                    first = False
                    continue
                else:
                    if char not in validHairColor:
                        invalid = True
                        break
            if invalid:
                break

        if field == 'ecl' and value not in eyeColor:
            invalid = True
            break

        if field == 'pid' and (len(value) != 9 or not value.isdigit()):
            invalid = True
            break

    if not invalid and fields == requiredFields:
        validPassportCounter2 += 1


print("Part 1:", validPassportCounter)
print("Part 2:", validPassportCounter2)
