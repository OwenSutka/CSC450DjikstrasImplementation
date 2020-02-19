############################################################
# Name: Owen Sutka
# Date Last Altered: 01/15/2020
# Class: CSC 450
# Teacher: Dr. Timofeyev
# Assignment: Assignment #3 - Ping over UDP
# Assignment Due Date: 01/17/20
# Purpose: To illustrate how two computers communicate over
#           UDP and how packets can be dropped
############################################################
# Requirements for client side code:
############################################################
# 1. Sets socket timeout as 1 second. settimeout() socket
#    function is your friend.
# 2. Sends multiple (n) UDP segments with ping message to
#    server with specified IP address and port number. 
# 3. Receives message back from server and calculates
#    message round trip time in milliseconds.
# 4. Displays server response if segment was received.
# 5. Displays Request time out string if segment was lost.
#    Segment is considered lost if the timeout is up.
# 6. Displays ping statistics information (number of sent,
#    received, lost segments, and loss percentage).
# 7. Displays approximate round trip times in milliseconds
#    (minimum, maximum, and average RTT).
# 8. Gets server IP address, server port number and number
#    (n) of ping packets to send as a command line arguments.

############################################################

# Libraries
import sys

# Constants


# Variables



# Error and Warning cases
############################################################
def errorChoose(errorInt=-1):
    # You can choose whatever error you need and it will produce the relevant result
    errorCase = {
        -1: "Unknown Error",
        1:  "",
        2:  "",
        3:  "",
        4:  "",
        5:  ""
    }
    # Prints an error statement
    print("\nERROR: {}\n".format(errorCase.get(errorInt, "Unknown Error at errorChoose")))
    return


def warningChoose(warningInt=-1):
    # You can choose whatever warning you need and it will produce the relevant result
    warningCase = {
        -1: "Unknown Warning",
        1:  "Input file unspecified. Will be entering Generic Mode.\n",
        2:  "No initial node specified on startup. Will need to be specified...\n",
        3:  ""
    }
    # Prints an warning statement
    print("\nWARNING: {}\n".format(warningCase.get(warningInt, "Unknown Error at warningChoose")))
    return

############################################################

# Take in csv file
if(len(sys.argv) >= 2):
    inputFile = str(sys.argv[1])
else:
    warningChoose(1)
    inputFile = "topology.csv"                                  ############## CHANGE VERY IMPORTANT

# Take in initial node
if(len(sys.argv) >= 3):
    initNode = int(sys.argv[2])
else:
    warningChoose(2)
    initNode = -1

if(inputFile == -1):
    # Add-on function
    while(runningUI == True):
        programNum = -1
        try:
            programNum = int(input("\n\nWhat Program would you like to run?\n0. Exit\n1. Set Server IP\n2. Set Server Port\n3. Set Number of Pings\n4. Set Probability of Success\n5. Set Socket Timeout\n6. Run Single Ping Program\n7. Run Full Ping Program\n8. Print most Recent Statistics\n9. Send Statistics to Text File\n\n"))
        except ValueError:
            errorChoose(4)
            programNum = -1
        if(programNum == -1):
            errorChoose(1)
        else:
            runProgram(programNum)
elif(initNode == -1):
    # Normal Function
    print("Pull this print from the pdf")
else:
    # advanced function
    print("Add this last when all functions are defined")

