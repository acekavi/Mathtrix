import os

# This clears the cmd prompt
clear = lambda: os.system('cls') #on Windows System only

def errorMsg():
    clear()
    print("Incorrect input. \nRedirecting to main menu...")
    cont = input("\nPress any key to continue...")

def maxOperand(lvl):
    if lvl == 1:
        return 10 
    elif lvl == 2:
        return 50
    else:
        return 100

def gameMode(lvl):
    # This function generated the mode by the difficulty level
    if lvl == 1:
        return "easy"
    elif lvl == 2:
        return "medium"
    else:
        return "hard"
