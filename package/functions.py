import random
import package.database as datab
import package.utility as utils

def quiz(level,count,maxNumber):
    global gameResult,score
    ops = ['+', '-', '*']
    score = 0
    gameResult = []
    for i in range(count):
        num1 = random.randint(1,maxNumber)
        num2 = random.randint(1,maxNumber)
        op = random.choice(ops[:level])
              
        guess = int(input(str(num1)+str(op)+str(num2)+" = "))
        answer = eval(str(num1) + op + str(num2))

        result = ""
        if (guess == answer):
            score += 1
            result = "Correct"
            print(result,'\n')
        else:
            result = "Incorrect"
            print(result,'\n')

            
        gameResult.append([str(num1) + op + str(num2)+"="+str(guess) + "\t\t\t", "(answer "+str(answer)+")" + "\t\t", "["+str(result)+"]"])
    utils.clear()
    gameResults()

def gameResults ():
    print ("Player Name \t- ",playerName)
    print ("Difficulty \t- ",mode.capitalize())

    generatedID = datab.genID(mode)
    print ("Game ID \t- ",generatedID,"\n")
    
    # This loop prints the game results line by line
    for i in gameResult:
        print(*i,"\n")
        
    print ('Your score was {}/{}'.format(score,len(gameResult))+"({0:.0%})".format(score/len(gameResult)))

    highscore = 100 * (score/len(gameResult))

    # Saves data to the database
    datab.saveDB (generatedID, playerName, int(round(highscore)), len(gameResult))
    cont = input("\nPress any key to continue...")

# Main Menu
def game(opt):
    global playerName,mode #Player name and mode is made global so i can use it later on with other functions aswell
    
    utils.clear()
    
    if opt == '1':
        playerName = input("Enter your name : ")
        #Quick match (Easy "1", No. of Questions "5", Maximum operand "10")
        try:
            print("You've chosen a Quick Game\n")
            mode = "easy"
            quiz(1,5,10)
            
        except Exception as e:
            print(e)
            utils.errorMsg()
        
    elif opt == '2':
        playerName = input("Enter your name : ")
        #Custom Match
        try:
            ## mode is set to here but can be used elsewhere too
            mode = ""
            print("You've chosen a Custom Game")
            level = int(input("\t 1 -> Difficulty : Easy \n\t 2 -> Difficulty : Medium \n\t 3 -> Difficulty : Hard \nEnter your option : "))
            
            if level == 1 or level == 2 or level == 3:
                count = int(input("Number of questions you wish to answer: "))
                ## Game mode is set
                mode = utils.gameMode(level)
                
            else:
                utils.errorMsg()
                
            # Inserts the user input values for Difficulty and no. of questions
            quiz(level,count,utils.maxOperand(level))
            
        except Exception as e:
            print(e)
            utils.errorMsg()
           
    elif opt == '3':
        #View Highscores
        utils.clear()
        datab.highscore()
        cont = input("\nPress any key to continue...")
           
    else:
        utils.errorMsg()
