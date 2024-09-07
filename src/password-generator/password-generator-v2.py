import random

letterList: str = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
numList: str = "1234567890"
symbolList: str = ".,/!?#@%&();:><*+-_"

def isValid(myPwd: str) -> bool:
    '''
    Checks if password contains at least one letter, one number and one special character
    '''
    pwdSet = set(myPwd)
    letterSet = set(letterList)
    numSet = set(numList)
    symbolSet = set (symbolList)
    return not (pwdSet.isdisjoint(numSet) or pwdSet.isdisjoint(symbolSet) or pwdSet.isdisjoint(letterList))

def get_random_char(pwdString: str) -> str:
    '''
    Returns a random character that can be a letter, number or special character,
    that is not previously on password while it is generating
    '''
    randomChar = ""
    while randomChar in pwdString:
        randomList = random.choice([numList, letterList, symbolList])
        randomChar = random.choice(randomList)

    return randomChar

def password_generator(passLength: int) -> str:
    '''
    Generates a random password which length is given.
    '''
    while True:
        myPwd = ""
        while len(myPwd) < passLength:
            myPwd += get_random_char(myPwd)

        if isValid(myPwd):
            return myPwd

def main():
    passLength = 16
    print(password_generator(passLength))

if __name__ == "__main__":
    main()