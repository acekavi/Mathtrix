def readCSVData():
    global records
    
    lines = []
    with open("Data.csv") as file:
        for line in file: 
            line = line.strip() #Striping the file line by line
            lines.append(line)  #storing everything in a list

#Getting the striped lines and spliting them again and adding line by line toa new list 
    records = []
    for i in lines: 
        records.append(i.split(",")[:5])

def showAllData():
    print("Reading all the records\n")

    for i in records:   #Displaying line by line 
        print(*i,sep="\t")

    print("\n")
    
def showMaths():
    print("Reading the records of First Name and Maths\n")

    for i in records:   #Displaying corresponding columns using indexes
        print(i[0],i[3],sep="\t")

    print("\n")

def above70():
    print("Reading the records of Maths and Programming marks above 70\n")

    print("Fname\tMaths\tProgramming")  #This line is excluded in the loop
    for i in records[1:]:   #Only the lines with numbers are taken to loop
        if int(i[3]) > 70 and int(i[4]) > 70:   #Marks are checked before displaying
            print(i[0],i[3],i[4],sep="\t")

    print("\n")
    
def failedAllSubjects():
    print("Reading the records of who failed in all the subjects\n")

    print("Fname\tScience\tMaths\tProgramming")
    for i in records[1:]:
        if int(i[2]) < 40 and int(i[3]) < 40 and int(i[4]) < 40: #Same as the above70()
            print(i[0],i[2],i[3],i[4],sep="\t")

    print("\n")

def scienceTotal():
    total = 0   #A variable is set and the total will be set here
    
    for i in records[1:]:   #Total variable is changed by this loop
        total += int(i[2])  #Values in this column is added to total
    
    print("Total of Science Marks : ",total)
    print("\n")

def highestMaths():
    highest = 0

    for i in records[1:]: #All records read and assigned to i line by line
        if int(i[3]) > highest: #If the the mark is greater than highest variable
            highest = int(i[3]) # it is set as the new highest
    
    print("Highest maths marks : ",highest)
    print("\n")
