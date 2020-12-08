import re


def findValidPassports():
    passportStrings = []
    file = open("input.txt", 'r')

    passportStrings = file.read().split('\n\n')

    mandatoryKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    validPassports = 0

    # Go through each passport str (list of key:vals) and
    # turn into dict
    # lookup the mandatory keys
    for passport in passportStrings:
        keyVals = passport.split()
        obj = {}
        for pair in keyVals:
            obj[pair.split(':')[0]] = pair.split(':')[1]

        isValid = False
        for key in mandatoryKeys:
            if key in obj:
                print(key)
                print(validators[key](obj[key]))
                isValid = validators[key](obj[key])
            else:
                isValid = False

            if not isValid:
                break

        if isValid:
            validPassports += 1

    return validPassports


def heightValidator(hgt):
    if hgt[-2:] == 'cm' and int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193:
        return True
    if hgt[-2:] == 'in' and int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76:
        return True
    return False


validators = {
    'byr': lambda str: len(str) == 4 and int(str) >= 1920 and int(str) <= 2002,
    'iyr': lambda str: len(str) == 4 and int(str) >= 2010 and int(str) <= 2020,
    'eyr': lambda str: len(str) == 4 and int(str) >= 2020 and int(str) <= 2030,
    'hgt': heightValidator,
    'hcl': lambda str: re.match(r'^#[0-9a-f]{6}$', str) is not None,
    'ecl': lambda str: str in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda str: re.match(r'^[0-9]{9}$', str) is not None,
}

print(findValidPassports())
