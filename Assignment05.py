# ---------------------------------------------------------#
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#       When the program starts, load each "row" of data in
#       "ToDoToDoList.txt" into a python Dictionary.
#       Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# VOlaughlin,2.13.2023,Created script
# ---------------------------------------------------------#

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file, object storage file
objFile = None  # file handle
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"task": strData[0].strip(), "priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("======================================") # for looks
        print("Here is the current data in the file: ")
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",")  # Returns a list!
            dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}  # strip gets rid of \n
            print(dicRow)
        print("======================================") # for looks
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("======================================") # for looks
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        dicRow = {"task": strTask, "priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data in table:")
        # for dicRow in lstTable:
        #     print(dicRow)
        # Step 4a - Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["task"] + "(" + row["priority"] + ")")
        print("======================================")
        continue  # to show the menu
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # Step 5a - Allow user to indicate which row to delete
        print("======================================")  # for looks
        strKeyToRemove = str(input("Which TASK would you like removed? - ")).strip()
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
            # end if
        # end for loop
        # Step 5b - Update user on the status
        if (blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        # Step 5c - Show the current items in the table
        print("========= The current items ToDo are: =========")
        for row in lstTable:
            print(row["task"] + "(" + row["priority"] + ")")
        print("===============================================")
        continue  # to show the menu
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # Step 5a - Show the current items in the table
        print("========= The current items ToDo are: =========")
        for row in lstTable:
            print(row["task"] + "(" + row["priority"] + ")")
        print("===============================================")
        # Step 5b - Ask if they want save that data
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open("ToDoList.txt", "w")
            for dicRow in lstTable:
                objFile.write(dicRow["task"] + "," + dicRow["priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the[Enter] key to return to menu.")
        continue  # to show the menu
    # Step 7 - Exit program
    elif (strChoice.strip == '5'):
        break # and exit the program