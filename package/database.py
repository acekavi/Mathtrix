import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "gamedb"
)

def genID(mode):
##### Game mode is made global and will be used at many places
    global gameMode
    gameMode = mode
    
    cursor = db.cursor()
    # defining the Query .capitaleze() makes the first letter Uppercase
    query = "SELECT `mode`,`inc` FROM `misc` WHERE `mode` = '"+gameMode[0].capitalize()+"'"
    
    # getting records from the table
    cursor.execute(query)

    # get one single record
    totalInc = cursor.fetchone()
    
    addInc()
    return str(totalInc[0])+str(totalInc[1])

def addInc():
    cursor = db.cursor()

    ## defining the Query
    query1 = "UPDATE `misc` SET `inc` = `inc` + 1 WHERE `mode` = '"+gameMode[0].capitalize()+"'"
    
    ## executing the query
    cursor.execute(query1)

    query2 = "UPDATE `misc` SET `inc` = `inc` + 1 WHERE `mode` = 'T'"
    
    ## executing the query
    cursor.execute(query2)

    ## final step to tell the database that we have changed the table data
    db.commit()

    #db.close()
def saveDB (gameID, name, score, question):
    
    cursor = db.cursor()
    # defining the Query
    query1 = "SELECT `Player`, `Highscore` FROM `"+gameMode+"` WHERE `Player` = '"+name+"'"

    # getting records from the table

    rows_count = cursor.execute(query1)        
    result = cursor.fetchall()
    
    if result != []:
        existName = [lis[0] for lis in result]
        existScore = [lis[1] for lis in result]
        print("\n", existName[0]," with highscore of ", existScore[0],"% already exist!",sep="")
        
        replace = input("Do you wish to replace the record?(Y/N)")
        
        if replace == "Y" or replace == "y":
            query3 = "UPDATE "+gameMode+" SET `gameID` = %s, `Questions` = %s, `Highscore` = %s WHERE `Player` = %s"
            values = (gameID, question, score, name)
            ## executing the query
            cursor.execute(query3,values)

            ## final step to tell the database that we have changed the table data
            db.commit()
            
        else:
            pass
    
    else:
        ## defining the Query
        query2 = "INSERT INTO `"+gameMode+"` (`gameID`, `Player`, `Questions`, `Highscore`) VALUES (%s, %s, %s, %s)"
        ## storing values in a variable
        values = (gameID, name, question, score)

        ## executing the query with values
        cursor.execute(query2, values)

        ## to make final output we have to run the 'commit()' method of the database object
        db.commit()

        
def highscore():
    cursor = db.cursor()

    # To display highscores of Easy------------------------------
    print("Mode -> Easy")
    query1 = "SELECT `gameID`, `Player`, `Highscore`, `Questions` FROM `easy` ORDER BY `Highscore` DESC,`Questions` DESC LIMIT 5"
    
    cursor.execute(query1)
    result = cursor.fetchall()

    print("Game-ID\t\tPlayer Name\t\t\tScore\t\t\tNo. of Questions")
    print("--------------------------------------------------------------------------------------------------------------------")
    for row in result:
        print(row[0] + "\t\t" + str(row[1]) + "\t\t\t\t" + str(row[2])+ "%\t\t\t" + str(row[3]))
    
    # To display highscores of Medium------------------------------
    print("\n\nMode -> Medium")
    query2 = "SELECT `gameID`, `Player`, `Highscore`, `Questions` FROM `medium` ORDER BY `Highscore` DESC,`Questions` DESC LIMIT 5"
    
    cursor.execute(query2)
    result = cursor.fetchall()

    print("Game-ID\t\tPlayer Name\t\t\tScore\t\t\tNo. of Questions")
    print("--------------------------------------------------------------------------------------------------------------------")
    for row in result:
        print(row[0] + "\t\t" + str(row[1]) + "\t\t\t\t" + str(row[2])+ "%\t\t\t" + str(row[3]))

    # To display highscores of easy------------------------------
    print("\n\nMode -> Hard")
    query3 = "SELECT `gameID`, `Player`, `Highscore`, `Questions` FROM `hard` ORDER BY `Highscore` DESC,`Questions` DESC LIMIT 5"
    
    cursor.execute(query3)
    result = cursor.fetchall()

    print("Game-ID\t\tPlayer Name\t\t\tScore\t\t\tNo. of Questions")
    print("--------------------------------------------------------------------------------------------------------------------")
    for row in result:
        print(row[0] + "\t\t" + str(row[1]) + "\t\t\t\t" + str(row[2])+ "%\t\t\t" + str(row[3]))

    query4 = "SELECT `inc` FROM `misc` WHERE `mode` = 'T'"
    
    cursor.execute(query4)
    result = cursor.fetchone()
    print("\nTotal number of games played =",result[0])

