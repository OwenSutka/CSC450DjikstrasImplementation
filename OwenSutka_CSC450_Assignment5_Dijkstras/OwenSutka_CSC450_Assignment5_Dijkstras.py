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

# Requirements for Dijkstra's code:
############################################################
# 1. First, your program has to read the costs of all links 
# in a given network from “topology.csv” file (provided
# on Moodle). In this file, the first row and the first column 
# refer to the names of the nodes (from u to z). Other cells 
# show the cost of links between the row node and the column 
# node (meaning two nodes are neighbors). The cost value 
# “9999” indicates an infinity cost (meaning two nodes are 
# not neighbors).
# 2. Your program has to take the name of the topology file 
# as a command line argument.
#       python dijkstras_algorithm.py topology.csv
# 3. Next, your program has to take a node’s name as an 
# input from a command line and print the shortest path 
# tree and the cost of least-cost paths for this node..
# 4. The computation of the shortest path tree and the costs 
# of least-cost paths has to be implemented with Dijkstra’s 
# algorithm.
# 5. Please, comment your code thoroughly, explaining the 
# steps of Dijkstra’s algorithm and the overall flow of your 
# program (e.g. parsing of input file, generating shortest 
# path tree output, etc.) In addition, please, properly 
# specify any sources you have used.
# 6. Create a “readme.pdf” in which specify Python version 
# you have used, instructions of how to run your program, 
# and screenshots of some sample program runs.
# 7. Submit zipped folder with your Python source code and 
# the readme.pdf file on Moodle.
############################################################

# Libraries
import sys
import csv

# Constants


# Global Variables
global nodeNames, edgeNamesWeights
nodeNames = []
edgeNamesWeights = {} # format is uu:0,uv:7,ux:3 ......
nodeChoice = ""

# Variables




# Error and Warning cases
############################################################
def errorChoose(errorInt=-1):
    # You can choose whatever error you need and it will produce the relevant result
    errorCase = {
        -1: "Unknown Error",
        1:  "VALUE ERROR: The input provided was in a different format than expected.",
        2:  "NODE NAME ERROR: Node Name specified is not in list of known nodes.",
        3:  "INPUT FILE ERROR: No input file specified. Cannot create node list or edge list.",
        4:  "",
        5:  ""
    }
    # Prints an error statement
    print("\n{}\n".format(errorCase.get(errorInt, "Unknown Error at errorChoose")))
    return

def warningChoose(warningInt=-1):
    # You can choose whatever warning you need and it will produce the relevant result
    warningCase = {
        -1: "Unknown Warning...",
        1:  "Input file unspecified. Will be entering Generic Mode...",
        2:  "No initial node specified on startup. Will need to be specified...",
        3:  ""
    }
    # Prints an warning statement
    print("\nWARNING: {}\n".format(warningCase.get(warningInt, "Unknown Error at warningChoose")))
    return
############################################################


# Functions
############################################################
# This function will take the csv file name as input and will find it and assign some of the global variables some values
def processCSV(inputFile):
    # Initialize the rows from the csv
    dataRows = []
    tempDict = {}
    # make sure to alter the global and not local variables for accessing later
    global nodeNames, edgeNamesWeights
    # Check if there is an input file, if not ask for one
    if(inputFile == -1):
        errorChoose(3)
        while(inputFile == -1):
            try:
                inputFile = str(input("Please, provide the input file's name: "))
                break
            except ValueError:
                inputFile = -1
                errorChoose(1)
    # open and parse data from file so that we have every edge and their weights
    with open(inputFile, 'rt') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            dataRows.append(row)
        # get the node names
        nodeNames = dataRows[0][1:len(dataRows[0])]
        # from each column pull the weight for each other node and itself. Works and is clean
        for i in range(1, len(dataRows[0])):
            for j in range(i,len(dataRows[0])):
                # Including edge cost and name in the dictionary
                edgeName = str(dataRows[0][i] + dataRows[0][j])
                edgeCost = int(dataRows[i][j])
                edgeNamesWeights[edgeName] = edgeCost
                # This had to be used because python ONLY uses pointers to values and it couldn't iterate a dictionary that changes size every iteration
                tempDict[edgeName] = edgeCost
        # now make more robust and easier to use by placing the reverse name for each node
        for i in tempDict:
            if(i[0] != i[1]):
                edgeNamesWeights[str(i[1]+i[0])] = edgeNamesWeights[i]
                

# This function chooses a node and then returns that value
def chooseNode():
    finalNode = -1
    # while loop to force the person to choose a valid combo for a node
    while(1):
        try:
            node = str(input("\nPlease, provide the node's name: "))
        except ValueError:
            node = ""
            errorChoose(1)
        # Check all nodes for the value specified
        for i in range(0, len(nodeNames)):
            if(node == nodeNames[i]):
                finalNode = node
                # return the final node
                return finalNode
            else:
                finalNode = -1
        # runs an error if the value specified is not in the list of nodes
        if(finalNode == -1):
            finalNode = ""
            errorChoose(2)

def dijkstras(startNode):
    nString = []
    weights = {}
    addOnWeight = 0
    global nodeNames, edgeNamesWeights
    tempNodeNames = nodeNames
    visited = {}
    for i in range(0, len(tempNodeNames)):
        weights[tempNodeNames[i]] = 9999
        visited[tempNodeNames[i]] = False
        

    currentNode = startNode
    nextNode = currentNode
    weights[currentNode] = [0, currentNode]
    while(1):
        minPath = 9999      # set min path to be able to reduce it in the future
        visited[currentNode] = True     # set the current nodes visited state to true
        nString.append(currentNode)     # append the current node to the nstring to get order of visiting
        for item in edgeNamesWeights.items():
            oldWeight = 9999
            edgeName = item[0]      # finds that we will determine if it is from the node
            if((edgeName[0] == currentNode) and (visited[edgeName[1]] == False)):       # check if the node the edge is connected to is visited and that the start of the edge is the current node
                tempWeight = int(item[1]) + addOnWeight     # set a temporary weight for the traversal of the specified edge
                otherNodeName = edgeName[1]     # get the end node's name
                nodeInfo = weights[otherNodeName[0]]
                if (nodeInfo == 9999):
                    oldWeight = nodeInfo
                else:
                    oldWeight = nodeInfo[0]
                if(tempWeight < oldWeight):
                    weights[edgeName[1]] = [tempWeight, edgeName[0]]
        print(currentNode)
        print(weights)
        for item in weights.items():
            if(item[1] != 9999):
                print(int(item[1][0]))
                if (int(item[1][0]) < minPath and visited[item[0]] == False):
                    minPath = int(item[1][0])
                    nextNode = item[0]
        if (nextNode == currentNode):
            return nString, weights
        else:
            currentNode = nextNode
            newInfo = weights[currentNode]
            addOnWeight = newInfo[0]
        print(minPath)
        print(nextNode)





def leastCosts(nodeChoice):
    print("least costs paths")
############################################################


# General input and functionality
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
    runningUI = True
    while(runningUI == True):
        programNum = -1
        try:
            programNum = int(input("\n\nWhat Program would you like to run?\n0. Exit\n1. Set CSV file\n2. Set Starting Node\n3. Find Shortest Paths of Set Node\n4. Find Shortest Paths of all Nodes\n5. Find Shortest Parse Tree\n\n"))
        except ValueError:
            programNum = -1
        if(programNum == -1):
            errorChoose(1)
        else:
            runProgram(programNum)
elif(initNode == -1):
    # Normal Function
    processCSV(inputFile)
    nodeChoice = chooseNode()
    tree, paths = dijkstras(nodeChoice)
    #leastCosts(nodeChoice)
else:
    # advanced function
    print("Add this last when all functions are defined")
############################################################
