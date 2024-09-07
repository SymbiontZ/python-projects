import random

letterList: str = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
numList: str = "1234567890"
symbolList: str = ".,/!?#@%&();:><*+-_"

def isValid(myPwd: str) -> bool:
    pwdSet = set(myPwd)
    numSet = set(numList)
    symbolSet = set (symbolList)
    return not (pwdSet.isdisjoint(numSet) or pwdSet.isdisjoint(symbolSet))


def get_random_letter(pwdString: str) -> str:
    
    randomLetter: str = ""
    while randomLetter in pwdString:
        randomLetter = random.choice(letterList)
    
    return randomLetter

def get_random_num(pwdString: str) -> str:
    randomNum = ""
    while randomNum in pwdString:
        randomNum = random.choice(numList)
    
    return randomNum

def get_random_symbol(pwdString: str) -> str:
    randomSymbol = ""
    while randomSymbol in pwdString:
        randomSymbol = random.choice(symbolList)
    
    return randomSymbol

def password_generator(passLength: int) -> str:
    while True:
        myPwd = ""

        while len(myPwd) < passLength:
            random_func = random.choice([get_random_letter,get_random_num,get_random_symbol])
            myPwd += random_func(myPwd)

        if isValid(myPwd):
            return myPwd


def main():
    passLength = 8
    random_pass = password_generator(passLength)
    print(random_pass)

if __name__ == "__main__":
    main()