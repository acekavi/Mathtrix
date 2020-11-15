import sys
import package.functions as func
import package.utility as utils
import time
            

        
#Creating a menu
while True:
    print ("Welcome to Mathtrix")
    print ("1 -> Quick Game \n\t 5 Simple ADD Questions")
    print ("2 -> Custom Game")
    print ("\t Easy \t\t->\t Addition Only\n\t Medium \t->\t Addition and Substraction\n\t Hard \t\t->\t Addition, Substraction and Multiplication")
    #print ("\t How many questions") Not necessary
    print ("3 -> View Highscores")

    print ("x -> Exit")
    
    option = input("Enter your option : ")
    if option == 'x' or option == 'X':
        sys.exit()
        
    else:
        func.game(option)
        #time.sleep(5) uncomment this to make a 5 sec delay
        utils.clear()
        
