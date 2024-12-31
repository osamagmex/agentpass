import random



uppercaseLetters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercaseLetters ='abcdefghijklmnopqrstuvwxyz'
specialLetters = '@.$#*'
digits = '0123456789'

    
letterSets = [uppercaseLetters, lowercaseLetters, specialLetters, digits]
max_length=len(uppercaseLetters+lowercaseLetters+specialLetters+digits)
    

def pass_gen(length): 

    password = ""

    usedCharacters = []

    while len(password) < length:
        letterSet = letterSets[random.randint(0, len(letterSets)-1)]

        character = letterSet[random.randint(0, len(letterSet)-1)]

        if character in usedCharacters:
            continue

        password += character
        usedCharacters.append(character)
    has_upper = any(char in uppercaseLetters for char in password)
    has_lower = any(char in lowercaseLetters for char in password)
    has_special = any(char in specialLetters for char in password)
    has_digit = any(char in digits for char in password)
    
    if not(has_upper and has_special and has_digit and has_lower):
        return pass_gen(length)

    return password

input = input("How long is your password: ")

try:
    length = int(input)
    if length>max_length:
        print(f"password must not be longer than {max_length}")
    elif length<8:
        print("password must be atleast 8 character long")

    else:
        password = pass_gen(length)
        print(f"Your password is: {password}")

except:
    print("enter a number")
