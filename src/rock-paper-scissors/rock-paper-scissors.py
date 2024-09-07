import random
from os import system as sys

option_list: dict[int, str] = {1: "Rock", 2: "Paper", 3: "Scissor"}

def clr():
    '''Clears Screen'''
    sys("cls")

def user_opt_pick() -> int:
    '''
    Ask the user to input a valid option from option list and returns it.
    
    Returns:
        opt (int): Valid input from user
    '''

    while True:
        clr()
        try:
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            opt = int(input())

            if opt not in option_list:
                raise ValueError
            
            return opt

        except ValueError:
            continue

def bot_opt_pick() -> int:
    '''
    Returns:
        int: A random option from option list.

    '''
    return random.randint(1,3)

def result(user_opt: int, bot_opt: int):
    '''
    Prints the result of the match

    Parameters:
        user_opt (int): User selected option
        bot_opt (int): Bot selected option
    '''
    print(f"YOU: {option_list[user_opt]} - {option_list[bot_opt]} :BOT")

    if user_opt == bot_opt:
        print("TIE!")
    elif user_opt == 1:
        if bot_opt == 2:
            print("YOU LOSE!")
        elif bot_opt == 3:
            print("YOU WIN!")
    elif user_opt == 2:
        if bot_opt == 1:
            print("YOU WIN!")
        elif bot_opt == 3:
            print("YOU LOSE!")
    elif user_opt == 3:
        if bot_opt == 1:
            print("YOU LOSE!")
        elif bot_opt == 2:
            print("YOU WIN!")


def start_game():
    user_opt = user_opt_pick()
    bot_opt = bot_opt_pick()

    result(user_opt, bot_opt)



if __name__ == "__main__":
    start_game()