# This is a public class so that i am able to Format
# any text throughout the Electoral System by typing
# FormatText.Something - The Something being BOLD, BLUE etc
class FormatText:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   BLACK = "\033[30m"
   WHITEBACK = "\033[47m"
   WHITE = "\033[37m"
   END = '\033[0m'


def main():             # creating main function
    menuOption = 0            # creating a variable for the while statement
    fileObj = None          # creating a variable for opening the file

    print()                 # Here so that when program first runs it is down one line and not at the very top of screen
    while menuOption != 5:        # while statement to allow the menu to function whilst 5 is not selected
        menuOption = menu()       # calling the menu function

        # using an if elif else statement for the menu options
        if menuOption == 1:        # This is Menu Option 1
            print(FormatText.PURPLE + "\n"+"*"* 60 +"\n" + FormatText.END) # Take a new line and Output ********** in purple 60 times then take another new line
            print(FormatText.BOLD + FormatText.UNDERLINE + FormatText.BLUE + "*" * 26+ " Setup " + "*" * 27 + FormatText.END) # Print *** Setup *** in Bold, Underline and Blue
            print(FormatText.GREEN+"\tSetting up polling station - voting file...."+ FormatText.END ) # Print message in Green Text

            # Creating Variable fileName
            fileName = input(FormatText.WHITEBACK+FormatText.BLACK+FormatText.BOLD+"Enter your file name: "+FormatText.END) # print input with Background colour White, Text = Black and Bold

            fileObj = open(r"storage/" + fileName + ".txt", "w") # Opening the variable fileName in Storage Dictionary and making file Text File (.txt). Also writing to file (w)

            # write data into text file
            # \n taking new line each time
            fileObj.writelines("Black Party: 0\n")
            fileObj.writelines("Blue Party: 0\n")
            fileObj.writelines("Green Party: 0\n")
            fileObj.writelines("Red Party: 0\n")
            fileObj.writelines("Yellow Party: 0\n")
            fileObj.writelines("Male: 0\n")
            fileObj.writelines("Female: 0\n")

            fileObj.close() # Close the file
            print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
            print("The file:",fileName,".txt has been created") # Message to let you know the file u created




        elif menuOption == 2: # This is Menu Option 2

            if fileObj != None: # If the variable for open file not equal to none continue
                # The Variable another has got to equal something (can be any Text)
                another = ""
                # When another doesn't equal password in continues rest of code
                while another != "Password": # When Password is entered kicks you out of while loop taking you back to menu

                    print(FormatText.PURPLE + "\n"+"*"* 60 +"\n"+ FormatText.END) # Take a new line and Output ********** in purple 60 times then take another new line
                    print(FormatText.BOLD + FormatText.UNDERLINE + FormatText.BLUE + "*" * 22+ " Polling Booth " + "*" * 23 + FormatText.END) # Print *** Polling Booth *** in Bold, Underline and Blue
                    print("\tYou are writing to " + fileName + " file") # print a message to let you know what file your writing points too

                    file = open(r"storage/" + fileName + ".txt", "r") # Read data from file (File Created in Menu option 1)

                    tallyLst = [0,0,0,0,0,0,0] # Creating the list tallyLst

                    # Striping all text away in order to get the point per party.
                    # Then adding the points to their place on the tallyLst
                    blackPoints = float(file.readline().lstrip("Black Party: ").rstrip("\n"))
                    tallyLst[0] = blackPoints
                    bluePoints = float(file.readline().lstrip("Blue Party: ").rstrip("\n"))
                    tallyLst[1] = bluePoints
                    greenPoints = float(file.readline().lstrip("Green Party: ").rstrip("\n"))
                    tallyLst[2] = greenPoints
                    redPoints = float(file.readline().lstrip("Red Party: ").rstrip("\n"))
                    tallyLst[3] = redPoints
                    yellowPoints = float(file.readline().lstrip("Yellow Party: ").rstrip("\n"))
                    tallyLst[4] = yellowPoints
                    malePoints = float(file.readline().lstrip("Male: ").rstrip("\n"))
                    tallyLst[5] = malePoints
                    femalePoints = float(file.readline().lstrip("Female: ").rstrip("\n"))
                    tallyLst[6] = femalePoints

                    # Created pollingCard list
                    # pollingCard is where the users vote goes per candidate
                    pollingCard = [0,0,0,0,0,0,0]
                    # Saying that pollingCard can be found in the function pollingBooth
                    pollingCard = pollingBooth(pollingCard, tallyLst)

                    # Messages outputed after pollingBooth Function has returned the pollingCard
                    print("First Five Numbers are Candidates and Last Two Numbers are Male and Female\n")
                    print("User's Vote:",pollingCard)

                    # Converting the pollingCard (User's Votes) into points
                    pollingCard = TranslatePollingCardtoVotes(pollingCard)

                    # Adding the pollingCard to the tallyLst through the for loop
                    for index in range(7):
                        tallyLst[index] += pollingCard[index]

                    print("Points after converting vote:",pollingCard)
                    print("The total Points per candidate:",tallyLst)
                    print(FormatText.PURPLE + "*" * 60 + "\n" + FormatText.END) # Output ********** in purple 60 times and take a new line

                    # Write the updated tallyLst back to the file
                    fileObj = open(r"storage/" + fileName + ".txt", "w") # open the file created in menu option 1
                    fileObj.writelines("Black Party: " + str(tallyLst[0])+ "\n")
                    fileObj.writelines("Blue Party: "+ str(tallyLst[1]) + "\n")
                    fileObj.writelines("Green Party: "+ str(tallyLst[2]) + "\n")
                    fileObj.writelines("Red Party: " + str(tallyLst[3]) + "\n")
                    fileObj.writelines("Yellow Party: " + str(tallyLst[4]) + "\n")
                    fileObj.writelines("Male: " + str(tallyLst[5]) + "\n")
                    fileObj.writelines("Female: " + str(tallyLst[6]) + "\n")
                    fileObj.close() # Close the text file

                    print("\tTo "+FormatText.YELLOW+ "Leave " + FormatText.END+ "Polling Booth Enter: " + FormatText.RED+"Password"+FormatText.END) # Print message with "Leave" in yellow and "Password" in red
                    # If Password is entered kicks you out of while loop else any other input while loop starts over again
                    another = input(FormatText.WHITEBACK+FormatText.BLACK+FormatText.BOLD+"Another voter (Press Enter)?"+FormatText.END) # print input with Background colour White, Text = Black and Bold
                print() # When While loop is Exited will print emprty line. Reason is so ******* on start of Menu function isn't tight agains "Another voter..." line

            else: # If the variable for open file equals none continue
                print(FormatText.PURPLE + "\n" + "*" * 60 +  FormatText.END) # Take a new line and Output ********** in purple 60 times
                print("Complete Menu Option 1") # Print Message

        elif menuOption == 3: # This is Menu Option 3
            # Try and Except for validating user input
            try:
                if fileObj != None: # If the variable for open file not equal to none continue
                    collatingData(tallyLst) # Calling a function. Reason for tallyLst is if there isn't a tallyLst created (From Menu option 2) option 3 can't run
                else:
                    print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
                    print("Complete Menu Option 1 - First") # if no file (Menu option 1) this message is printed
            except:
                print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END)# Take a new line and Output ********** in purple 60 times
                print("Complete Menu Option 2 - Before you can Continue") # if no tallyLst (Menu option 2) this message is printed

        elif menuOption == 4: # This is Menu Option 4
            # Try and Except for validating user input
            try:
                if fileObj != None: # If the variable for open file not equal to none continue
                    reviewStats(tallyLst) # Calling a function. Reason for tallyLst is if there isn't a tallyLst created (From Menu option 2) option 3 can't run
                else:
                    print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
                    print("Complete Menu Option 1 first") # if no file (Menu option 1) this message is printed
            except:
                print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
                print("Complete Menu Option 2 - Before you can Continue") # if no tallyLst (Menu option 2) this message is printed
        elif menuOption == 5:
            print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
            print("Exiting Electoral System") # Print message for user
            break
        else: # if any other number other than 1 to 5 is entered this code will run
            print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
            print("Invalid Menu option - Try Again") # print message for user

    # Once while loop is broken out of (Menu Option 5)
    print("End of program") # Print Message
    print(FormatText.PURPLE +  "*" * 60 + FormatText.END) # Output ********** in purple 60 times

def pollingBooth(pollingCard, tallyLst): # Creating a function called pollingBooth

    print(FormatText.GREEN+FormatText.BOLD+"\n\tVoting Choices"+FormatText.END) # Output new line tab text and print "Voting Choices" in green text and bold
    print("\t0/1/2/3/4/5\n") # Tab in print message and take a new line
    print(FormatText.GREEN+FormatText.BOLD+"\tDescription"+FormatText.END) # Tab in print "Description" in green and bold
    print("\tYou can only use 1-5 once and zero as many times as you like ") # Tab and print message
    print("\tOnly one number per candidate") # Tab and print message

    mfAns = genderQuestion() # Creating a variable which is found from the function genderQuestion
    if mfAns == 1: # if one is returned - Male
        pollingCard[5] = 1
        pollingCard[6] = 0
    else: # if zero is returned = Female
        pollingCard[5] = 0
        pollingCard[6] = 1

    # Call CandidatesInfo function
    # Will output a description of all Candidates in the running
    CandidatesInfo()


    invalid = True # Setting Variable invalid to True
    while invalid: # While invalid is true
        for index in range(0,5): # So it will run str(index+1) over 5 times
            duplicate = True # duplicate variable equals True. It is for the duplicates function
            # keep looping as long as there is a duplicate
            while duplicate: # While duplicate is True
                print(FormatText.YELLOW +"\tCandidate " + str(index+1) + ":"+ FormatText.END) # Will print "Candidate 1" then "Candidate 2" and so till 5 due to for loop
                vote = recordVote(index) # Setting vote variable to equal recordVote
                pollingCard[index] = vote # Making the pollingCard list the users inputs from the recordVote function

                duplicate = Duplicates(pollingCard, index) # duplicate variable is equal to function Duplicates, in order to check users input (index)
                print("Is there a duplicate:", duplicate) # Will print "Is there a duplicate:" True or else False depending on user input
                print("Voting Numbers used:",pollingCard[0:5]) # Will output the pollingCard e.g. [1,0,0,3,2] to show the numbers u have used
                print(FormatText.PURPLE + "*" * 60 + "\n" + FormatText.END) # Output ********** in purple 60 times and take a new line

        # If invalid is False then following code will run
        # Should never run cause invalid is hard coded as True previously not False
        invalid = False

    print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
    print("Your votes have been cast") # Output message

    return pollingCard # Returning the new updated pollingCard

def recordVote(index): # Creating a function
    # The Variable another has got to equal something (can be any Text) so that you are able to return / print messages
    message = ""

    # When the candidate goes up by (index+1) in polling booth it will output the messages below.
    if index == 0:
        message = "\t\tBlack Party - Joan Jet - Joan wants to build a statue of himself"
    elif index == 1:
        message = "\t\tBlue Party - Bert Navy - Bert wants to cut all politicians salary"
    elif index == 2:
        message = "\t\tGreen Party - Luke Lime -  Luke wants the poor to stay poop"
    elif index == 3:
        message = "\t\tRed Party - Rose Burgundy - Rose wants the Benefits Scheme to be re-looked at"
    elif index == 4:
        message = "\t\tYellow Party - Egbert Yoke - Egbert wants school to teach children about Tax and Mortgages"

    print(message) # Will print the message

    # Next few lines of code is for voting for the candidate presented whether that be Candidate 1,2,3 etc
    votingNum = -1 # Creating a votingNum variable that is carrying a value.

    # The variable votingNum means i can have a while loop
    while votingNum < 0 or votingNum > 5: # when number is less than zero and greater than 5 code doesn't runs
        # Try and Except for error handling so that used can't enter letters or can't enter number outside range 0-5
        try:
            # Storing the user vote in a variable
            userVote = input(FormatText.WHITEBACK+FormatText.BLACK+FormatText.BOLD+"Enter Vote: "+FormatText.END) # Text has background colour white, Text colour Black and Bold.

            # Creating an if statement so that if user input zero
            # it can be used as many times as you like with no  limit
            if len(userVote) == 0:
                userVote = "0" #user input is "0"
            votingNum = int(userVote)
        except:
            votingNum = -1

    return votingNum # Return the user input

# This Function is used to Change the users inputed votes
# e.g. 1,2,3,5,4 into poinnts so that vote position 3 is
# worth 0.33 points
def TranslatePollingCardtoVotes(pollingCard):
    # Index is user input in pollingCard [0,0,0,0,0,0,0] - 0 is the Index
    for index in range(5): # For loop to loop over index 5 times
        if(pollingCard[index] == 2): # Users input is 2
            pollingCard[index] = 0.5 # Change to 0.5
        elif (pollingCard[index] == 3): # Users input is 3
            pollingCard[index] = 0.33 # Change to 0.33
        elif (pollingCard[index] == 4): # Users input is 4
            pollingCard[index] = 0.25 # Change to 0.25
        elif (pollingCard[index] == 5): # Users input is 5
            pollingCard[index] = 0.2 # Change to 0.2
        else:
            # value one stays unchanged
            x = 1
    return pollingCard # The new polling card is returned e.g. Instead of [1,3,2,4,5]
                        # it will not be [1,0.33,0.5,0.25,0.2]


def CandidatesInfo(): # Creating a CandidatesInfo Function
    print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
    print(FormatText.GREEN + FormatText.BOLD+"\tCandidates"+FormatText.END) # Will Tab outputed text and make text bold and in green colour
    print("\tThere are Five Candidates\n") # Tab text and then take a new line

    # Will print "Candidate 1", "Candidate 2" etc in yellow text and then the party and description following it
    print(FormatText.YELLOW + "\tCandidate 1" + FormatText.END + " = " + "Black Party - Joan Jet - Joan wants to build a statue of himself")
    print(FormatText.YELLOW + "\tCandidate 2" + FormatText.END + " = " + "Blue Party - Bert Navy - Bert wants to cut all politicians salary")
    print(FormatText.YELLOW + "\tCandidate 3" + FormatText.END + " = " + "Green Party - Luke Lime - Luke wants the poor to stay poop")
    print(FormatText.YELLOW + "\tCandidate 4" + FormatText.END + " = " + "Red Party - Rose Burgundy - Rose wants the Benefits Scheme to be re-looked at")
    print(FormatText.YELLOW + "\tCandidate 5" + FormatText.END + " = " + "Yellow Party - Egbert Yoke - Egbert wants school to teach children about Tax and Mortgages")
    print(FormatText.PURPLE +  "*" * 60 +"\n" + FormatText.END) # Output ********** in purple 60 times and take a new line


def Duplicates(pollingCard, index): # Creating a Duplicates Function to test you can't have 1,2,3,4,5 twice in user input.
                                    # e.g. out of 5 candidates u can't have 1,2,3,4,5 for two candidates

    # Creating an if elif else statement so that it takes your input in the polling card which is what index is for.
    # it looks at the position of pollingCard and checks that it doesn't match any other value in the index
    # Apart from zero because the polling card is set at zero so that zero is allowed.
    # if it matches "Already used - Vote Again" will be printed else "Vote valid" will be printed
    if pollingCard[index] == pollingCard[0] and pollingCard[index] != 0 and index != 0:
        print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
        print("Already used - Vote Again") # Print message
        # return true so the loop continues
        return True

    elif pollingCard[index] == pollingCard[1] and pollingCard[index] != 0 and index != 1:
        print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
        print("Already used - Vote Again") # Print message
        # return true so the loop continues
        return True

    elif pollingCard[index] == pollingCard[2] and pollingCard[index] != 0 and index != 2:
        print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
        print("Already used - Vote Again") # Print message
        # return true so the loop continues
        return True

    elif pollingCard[index] == pollingCard[3] and pollingCard[index] != 0 and index != 3:
        print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
        print("Already used - Vote Again") # Print message
        # return true so the loop continues
        return True

    elif pollingCard[index] == pollingCard[4] and pollingCard[index] != 0 and index != 4:
        print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
        print("Already used - Vote Again") # Print message
        # return true so the loop continues
        return True

    else:
        print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
        print("Vote valid") # Print message
        # return false to end loop
        return False

def genderQuestion(): # Create a function called genderQuestion
    print(FormatText.BOLD+FormatText.GREEN+"\n\tSelect Your Gender"+FormatText.END) # Will take a new line and tab text that is green and bold.

    # Used for while loop
    gender = -1 # creating a variable that is storing a value for gender

    # creating a while loop so that if gender doesn't equal 1 and doesn't equal 0 code will run
    # The while loop will run as gender is set to -1 so i am able to enter while loop
    while gender != 1 and gender != 0: #
        # try and except for error handling so that user can't enter any letters in the gender input
        try:
            print("\tFor "+ FormatText.YELLOW+FormatText.BOLD+"Male"+FormatText.END+" Enter "+FormatText.RED+FormatText.BOLD+"(1)"+FormatText.END) # print message - "Male" is bold and in yellow - (1) is in red.
            print("\tFor "+ FormatText.YELLOW+FormatText.BOLD+"Female"+FormatText.END+" Enter "+FormatText.RED+FormatText.BOLD+"(0)"+FormatText.END) # print message - "Female" is bold and in yellow - (0) is in red.
            gender = int(input(FormatText.WHITEBACK+FormatText.BLACK+FormatText.BOLD+"Are you Male (1) or Female (0): "+FormatText.END)) # User input saved to variable gender - text has a white background - text is bold
        except:
            print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
            print("Invaild Gender Type") # print message
            print(FormatText.PURPLE + "*" * 60 + "\n" + FormatText.END) # Output ********** in purple 60 times and take a new line
            gender = -1 # sets gender to -1 so that the while loop runs again
    return gender # Return gender which is users input either 1 or 0.

# This function is going to produce the Menu for Electoral System
def menu():     # Created menu functon
    print(FormatText.PURPLE +"*"* 60 +"\n"+ FormatText.END)  # is going to print ********** in purple 60 times and them take a new line
    print(FormatText.BOLD + FormatText.UNDERLINE + FormatText.BLUE+"*************** Electoral System Menu ******************"+ FormatText.END) # Will Print *** Electoral System Menu *** Blue and Underlined
    print(FormatText.GREEN+"\t 1. Setup polling station votes file"+FormatText.END) # Is printing what option 1 is
    print(FormatText.CYAN+"\t 2. Enter polling booth"+FormatText.END) # Is printing what option 2 is
    print(FormatText.YELLOW+"\t 3. Collate data from other polling stations"+FormatText.END) # Is printing what option 3 is
    print(FormatText.DARKCYAN+"\t 4. Review statistics"+FormatText.END) # Is printing what option 4 is
    print(FormatText.RED+"\t 5. Exit"+FormatText.END) # Is printing what option 5 is

    # While True Statement is here so that when i get Option input i can return value entered
    while True:
        try: # For Error Handling so that you can't have any number other than 1,2,3,4,5 as specified in Main Function.
            option = int(input(FormatText.WHITEBACK+FormatText.BLACK+FormatText.BOLD+"Enter your option: "+FormatText.END)) # User inputs option
            break # If option is between 1-5 while loop breaks
        except ValueError: # Here so that if user enters fsjfself. System will not crash
            print(FormatText.PURPLE + "\n"+"*"* 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
            print("Please enter a number between 1 and 5: ") # Print message to guide user in what to do
            print(FormatText.PURPLE + "*"* 60 + "\n"+FormatText.END) # Output ********** in purple 60 times and take a new line
    return option # Users input is returned


def reviewStats(tallyLst): # Creating a variable reviewStats
    listfile = [] # Creating a variable that stores a list
    print()
    while True: # Created a while loop so that if user inputs doesn't match the while loop will run again
        # Try and except for error handling so that if user enters file that doesn't exist they get a output message
        try:
            print(FormatText.PURPLE + "*" * 60 +"\n"+ FormatText.END) # Take a new line and Output ********** in purple 60 times then take another new line
            print(FormatText.BOLD + FormatText.UNDERLINE + FormatText.BLUE + "*" * 24 + " Statistics " + "*" * 24 + FormatText.END) # Print *** Statistics *** in Bold, Underline and Blue
            print(FormatText.GREEN + "\tFile Names" + FormatText.END) # tab text and print it out in green text
            print("\t\tYou" + FormatText.RED + " DO NOT " + FormatText.END + "need to include" + FormatText.YELLOW + " .txt" + FormatText.END + " in File Name")
            fileName = input(FormatText.WHITEBACK+FormatText.BLACK+FormatText.BOLD+"Enter name: "+FormatText.END) # storing the file in variable fileName
            print(FormatText.PURPLE +  "*" * 60 + "\n" +FormatText.END) # Output ********** in purple 60 times and take a new line

            # Open the file you just entered to read the data
            file = open(r"storage/" + fileName + ".txt", "r")

            # Striping all text away in order to get the point per party.
            # Then adding the points to their place on the tallyLst
            blackPoints = float(file.readline().lstrip("Black Party: ").rstrip("\n"))
            tallyLst[0] = round(blackPoints,2)
            bluePoints = float(file.readline().lstrip("Blue Party: ").rstrip("\n"))
            tallyLst[1] = round(bluePoints,2)
            greenPoints = float(file.readline().lstrip("Green Party: ").rstrip("\n"))
            tallyLst[2] = round(greenPoints,2)
            redPoints = float(file.readline().lstrip("Red Party: ").rstrip("\n"))
            tallyLst[3] = round(redPoints,2)
            yellowPoints = float(file.readline().lstrip("Yellow Party: ").rstrip("\n"))
            tallyLst[4] = round(yellowPoints,2)
            malePoints = float(file.readline().lstrip("Male: ").rstrip("\n"))
            tallyLst[5] = round(malePoints,2)
            femalePoints = float(file.readline().lstrip("Female: ").rstrip("\n"))
            tallyLst[6] = round(femalePoints,2)

            file.close()    # Close the file you have opened to save the new changes

            file = open(r"storage/" + fileName + ".txt", "r") # Re-Open the file

            # Create a for loop to iterate over every line in file in order to save it to list (listfile)
            for line in file:
                listfile.append(line.strip()) # Add data to the list (listfile)

            # Getting max and min of candidate
            # Had to split text from value in order to get digit.
            # Read over every value in listfile in order to determine max and min
            largest = max(str(line.split(":")[1]) for line in listfile[0:5])
            smallest = min(str(line.split(":")[1]) for line in listfile[0:5])


            print(FormatText.GREEN + "\tWinning / Losing Candidate(s)" + FormatText.END) # tab text and output message in green text
            print("\tBelow is all Candidate Winners and Losers\n") # tab text and output message then take new line

            print(FormatText.YELLOW + "\tCandidate Winner(s)" + FormatText.END) # tab text and output message in yellow text
            # For loop to iterate over the first five pieces of data in listfile
            for item in listfile[0:5]:
                # Finding item largest in order to get not just the number but the text associated with it
                if (item.find(largest)) != -1:
                    # prints the winning candidate with name and number of votes
                    print("\tThe winning candidate(s) are", item, "vote(s)\n")

            print(FormatText.YELLOW + "\tCandidate Loser(s)" + FormatText.END) # tab text and output message in yellow text
            # For loop to iterate over the first five pieces of data in listfile
            for item in listfile[0:5]:
                # Finding item smallest in order to get not just the number but the text associated with it
                if (item.find(smallest)) != -1:
                    # prints the losing candidate with name and number of votes
                    print("\tThe losing candidate(s) are", item, "vote(s)")

            # Getting max and min of candidate
            # Had to split text from value in order to get digit.
            # Read over every value in listfile in order to determine max and min
            popular_gender = max(str(line.split(":")[1]) for line in listfile[5:])
            nonPopular_gender = min(str(line.split(":")[1]) for line in listfile[5:])

            print(FormatText.GREEN + "\n\n\tTop Gender to Vote" + FormatText.END) # take two new lines, tab text and output message in green text
            print("\tBelow is the Gender to vote the most") # tab text and print message
            print("\tAs well as the Gender to vote the least\n") # tab text and print message. Then take new line
            print(FormatText.YELLOW + "\tMost Popular Gender to Vote" + FormatText.END) # tab text and output message in yellow text

            # For loop to iterate over the everything after five which is 6 & 7 (Gender Male and Female) for data in listfile
            for item in listfile[5:]:
                # Finding item popular_gender in order to get not just the number but the text associated with it
                if (item.find(popular_gender)) != -1:
                    # prints the most popular gender either male or female and number of votes
                    print("\tThe most popular gender to vote is:", item, "vote(s)\n")
            print(FormatText.YELLOW + "\tLeast Popular Gender to Vote" + FormatText.END) # tab text and output message in yellow text
            # For loop to iterate over the everything after five which is 6 & 7 (Gender Male and Female) for data in listfile
            for item in listfile[5:]:
                # Finding item nonPopular_gender in order to get not just the number but the text associated with it
                if (item.find(nonPopular_gender)) != -1:
                    # prints the least popular gender either male or female and number of votes
                    print("\tThe least popular gender to vote is:", item, "vote(s)")

            file.close() # Close the open file

            # Getting the total number of candidate/party votes
            # Store the total tally in totalTally_Parties
            # The tallyLst being added together is the candidates
            totalTally_Parties = tallyLst[0] + tallyLst[1] + tallyLst[2] + tallyLst[3] + tallyLst[4]

            # Getting the total number of male and female votes
            # Store the total tally in totalTally_Gender
            # The tallyLst being added together is the Male (tallyLst[5]) and Female (tallyLst[6])
            totalTally_Gender = tallyLst[5] + tallyLst[6]

            # Calculating each party by taking its position in tallyLst dividing it by totalTally_Parties or totalTally_Gender then times it by 100
            # storing each candidate in there parties
            # I am also rounding the percent to one decimal places
            black_Percent = round((tallyLst[0] / totalTally_Parties) * 100, 1)
            blue_Percent = round((tallyLst[1] / totalTally_Parties) * 100, 1)
            green_Percent = round((tallyLst[2] / totalTally_Parties) * 100, 1)
            red_Percent = round((tallyLst[3] / totalTally_Parties) * 100, 1)
            yellow_Percent = round((tallyLst[4] / totalTally_Parties) * 100, 1)
            male_Percent = round((tallyLst[5] / totalTally_Gender) * 100, 1)
            female_Percent = round((tallyLst[6] / totalTally_Gender) * 100, 1)

            # printing candidate statistics so that it is displaying parties total points and there percent of votes.
            print(FormatText.GREEN + "\n\n\tCandidates Statistics"+ FormatText.END)
            print("\tBelow is all Five Candidates Total Points")
            print("\tAs well as the percentage of people that voted for them\n")
            print(FormatText.YELLOW + "\tCandidate 1: " + FormatText.END + "Black Party has got:", tallyLst[0], "Point(s)" + "\n\t\t\t\t" + " Which is:", black_Percent, "% of votes")
            print(FormatText.YELLOW + "\tCandidate 2: " + FormatText.END + "Blue party has got:",tallyLst[1], "Point(s)" + "\n\t\t\t\t" + " Which is:", blue_Percent, "% of Votes")
            print(FormatText.YELLOW + "\tCandidate 3: " + FormatText.END + "Green party has got:",tallyLst[2], "Point(s)" + "\n\t\t\t\t" + " Which is:", green_Percent, "% of Votes")
            print(FormatText.YELLOW + "\tCandidate 4: " + FormatText.END + "Red party has got:",tallyLst[3], "Point(s)" + "\n\t\t\t\t" + " Which is:", red_Percent, "% of Votes")
            print(FormatText.YELLOW + "\tCandidate 5: " + FormatText.END + "Yellow party has got:",tallyLst[4], "Point(s)" + "\n\t\t\t\t" + " Which is:",  yellow_Percent, "% Votes")

            # printing male and female statistics so that it is displaying male and female total points and there percent of votes.
            print(FormatText.GREEN + "\n\n\tMale / Female Statistics" + FormatText.END)
            print("\tBelow is the total number of Males and Females who voted")
            print("\tAs well as the percentage of Males and Females that voted\n")
            print(FormatText.YELLOW + "\tMale: " + FormatText.END + "There was",tallyLst[5],"Male(s) that voted" + "\n\t\t\t\t" + " Which is:", male_Percent, "% of Votes")
            print(FormatText.YELLOW + "\tFemale: " + FormatText.END + "There was",tallyLst[6],"Female(s) that voted" + "\n\t\t\t\t" + " Which is:", female_Percent, "% of Votes\n")
            break # breaking out of while so that is goes back to Menu
        except:
            # printing validatation so that if file doesn't exist it will output following code
            print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
            print("File doesn't exist")



def collatingData(tallyLst): # Creating a function called collatingData

    allFiles = [] # Creaing a variable that is going to store a list

    # Tryed to create a while loop to iterate over question if the wrong
    # but after the wrong file name was entered once in cycle if i then
    # put two files that do exist it wouldn't open them.

    # Try and Except error so that if any wrong inputs are entered it will ouput a message "Make sure and answer queston correctly?"
    try:

        print(FormatText.PURPLE + "\n" + "*" * 60 +"\n"+ FormatText.END) # Take a new line and Output ********** in purple 60 times then take another new line
        print(FormatText.BOLD + FormatText.UNDERLINE + FormatText.BLUE + "*" * 22 + " Collating Data " + "*" * 22 + FormatText.END) # Print *** Collating Data *** in Bold, Underline and Blue
        print(FormatText.GREEN+"\tNumber of Files"+FormatText.END)
        print("\t\tHow many files do you want to combine? E.g. 1,2,3,4 etc")
        num_files = int(input(FormatText.WHITEBACK+FormatText.BLACK+FormatText.BOLD+"Enter Number of Files: "+ FormatText.END)) # User enters the number of files they want to combine and saves it to variable num_files

        # if statement so that for number of files you don't go 3463434 files u want to combine because there isn't that many files
        if num_files <1 or num_files >20: # if num_files - user input is less than 1 and greater than 20 code will run
            print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times then take another new line
            print("Please enter a number between 1 and 20")
        else: # num_files is between 1 and 20 code will run
            print(FormatText.GREEN+"\n\tFile Names"+FormatText.END)
            print("\t\tYou" + FormatText.RED+ " DO NOT "+ FormatText.END+ "need to include" + FormatText.YELLOW+ " .txt" + FormatText.END + " in File Name")

            # for loop to get all the names of number of files you want to combine
            for i in range(num_files):
                filename = input(FormatText.WHITEBACK+FormatText.BLACK+FormatText.BOLD+"Enter the File Name: "+FormatText.END)
                allFiles.append(filename) # appending the file name to a list

            line_sums = {} # Creating a dictionary called line_sums
            # looping over every file in list allFiles
            for filename in allFiles:
                with open("storage\\" + filename + ".txt", "r") as f: # reading data in each filename
                    # for loop for each line in files
                    for line in f:
                        # spliting the text and the digit into key and value
                        key, value = line.split(":")
                        key = key.strip()
                        value = value.strip()
                        # Changing the text str to a float value
                        value = float(value)
                        # if key isn't in line_sums at it to line_sums
                        if key not in line_sums:
                            line_sums[key] = 0
                        line_sums[key] += value

            # Open the totalVotes.txt file to save all data to by writing it to file
            TotalvotesFile = open(r"storage/" + "totalVotes.txt", "w")
            for k, v in line_sums.items():
                TotalvotesFile.write("{}: {}\n".format(k,v))
            TotalvotesFile.close()

            # output a message to let user know that all data has been added to totalVotes file
            print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
            print("All votes have been added to the Total Votes File (totalVotes)")
            print("To Review Statistics go to Menu Option 4 'Review Statistics'")

    except: # will output following code if you enter number of files wrong or enter a file that doesn't exist
        print(FormatText.PURPLE + "\n" + "*" * 60 + FormatText.END) # Take a new line and Output ********** in purple 60 times
        print("Make sure and answer question correctly?")


main() # Calling the function to start program