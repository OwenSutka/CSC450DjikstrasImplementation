############################################################
# Name: Owen Sutka
# Date Last Altered: 02/20/2020
# Class: CSC 450
# Teacher: Dr. Timofeyev
# Assignment: Assignment #5 - Dijkstra's
# Assignment Due Date: 02/21/20
# Purpose: To illustrate the least cost paths formation that
#    A network will calculate
############################################################

# Requirements for Dijkstra's code:
############################################################
# 1. First, your program has to read the costs of all links 
# in a given network from given file (provided
# on Moodle). In this file, the first row and the first column 
# refer to the names of the nodes (from u to z). Other cells 
# show the cost of links between the row node and the column 
# node (meaning two nodes are neighbors). The cost value 
# 9999 indicates an infinity cost (meaning two nodes are 
# not neighbors).
# 2. Your program has to take the name of the topology file 
# as a command line argument.
# 3. Next, your program has to take a nodes name as an 
# input from a command line and print the shortest path 
# tree and the cost of least-cost paths for this node..
# 4. The computation of the shortest path tree and the costs 
# of least-cost paths has to be implemented with Dijkstras 
# algorithm.
# 5. Please, comment your code thoroughly, explaining the 
# steps of Dijkstras algorithm and the overall flow of your 
# program (e.g. parsing of input file, generating shortest 
# path tree output, etc.) In addition, please, properly 
# specify any sources you have used.
# 6. Create a readme.pdf in which specify Python version 
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
global nodeNames, edgeNamesWeights # set as global cuz its like cheating
nodeNames = []  # initialize (unnecessary in python but we wildin)
edgeNamesWeights = {} # format is uu:[0,u],uv:[7,u],ux:[3,u] ......

# Variables
nodeChoice = "" # why did I do this? oh yeah cuz 90% of my programs are microcontrollers



# Error and Warning cases           ---- Not really used
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


# Functions         -- Very much used
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

# this is the big boi program that actually does things
# FYI: I kinda went the cheeky route and used dictionaries cuz I know this algo by heart at this point
#       so it was quicker for me to do it that way. Hard to understand though.
def dijkstras(startNode):
    # initialization of variables has a special space in my heart, even if python couldn't care less...
    nString = []
    weights = {}
    visited = {}
    addOnWeight = 0
    # pulling in those cheeky boi globals from before for use in this algo
    global nodeNames, edgeNamesWeights

    # this for loop initializes the weights dictionary adn the visited dictionary. This allows me to check if a node has been vistied before and to check if
    #       the new weight is less than the old one. Weights will also be the variable returned that defines what this algo does. 
    for i in range(0, len(nodeNames)):
        weights[nodeNames[i]] = 9999
        visited[nodeNames[i]] = False

    # set the currentNode to the specified starting node and then also setting the next node to current node for use later in the algo to check if no new
    #       nodes are available to take a path down
    currentNode = startNode
    nextNode = currentNode
    # This shows how the final weights dictionary will be returned. We have the node as the key, then we have the total cost to get to that node and the previous
    #       node as the object the key returns. We can completely define the shortest path tree from this information
    weights[currentNode] = [0, currentNode]

    # this is a cheeky while loop that allows us to not think too much about what break-out cases may exist and just break if we think the algo is done
    while(1):
        # set min path to be able to reduce it in the future
        minPath = 9999      
        # set the current node visited state to true, remember this will iterate and eventually all nodes should be true
        visited[currentNode] = True     

        # now time for the thicc part of the algo. This will check each item in the edge list we have created and then check each one against the current node (iterating)
        #           and then if it is connected to the current node it will the ncheck to see if the weight is more than what is already on that path and then replace
        #           the current weights dictionary field if necessary
        for item in edgeNamesWeights.items():
            # make the old weight the max possible so that life is gud
            oldWeight = 9999
            edgeName = item[0]
            # check if the node the edge is connected to is visited and that the start of the edge is the current node
            if((edgeName[0] == currentNode) and (visited[edgeName[1]] == False)):    
                # set a temporary weight for the traversal of the specified current node plus the edge
                tempWeight = int(item[1]) + addOnWeight     
                # get the end nodes name
                otherNodeName = edgeName[1]    
                # get the end nodes info so that we dont have conflicts
                nodeInfo = weights[otherNodeName[0]]
                # grab the info and assign a value to oldWeight
                if (nodeInfo == 9999):
                    oldWeight = nodeInfo
                else:
                    oldWeight = nodeInfo[0]
                    # compare and change if needed, basic weight training
                if(tempWeight < oldWeight):
                    weights[edgeName[1]] = [tempWeight, edgeName[0]]
        # this is the part that determines the next node to traverse. Basically finds the cheapest path and jumps on it, there is a possibility nextNode is still currentNode...
        for item in weights.items():
            # checks for untouched nodes...
            if(item[1] != 9999):
                # checks if unvisited and if it min path in case of multiple unvisited nodes
                if (int(item[1][0]) < minPath and visited[item[0]] == False):
                    # set them vals boi
                    minPath = int(item[1][0])
                    nextNode = item[0]
        # ...if nextNode is equal to currentNode, then there are no more possible nodes to visit and therefore we are done. Return the weights dictionary
        if (nextNode == currentNode):
            return weights
        # ...if nextNode is a new boi then we need to set current Node to that and get the addOnWeight to change to that new nodes value
        else:
            currentNode = nextNode
            newInfo = weights[currentNode]
            addOnWeight = newInfo[0]


def leastCosts(nodeChoice):
    print("least costs paths")
############################################################


# General input and functionality       --- I have this on github at https://github.com/OwenSutka/CSC450DjikstrasImplementation , I have much more I wnat to implement.
#       For now it is quite incomplete so ignore the mess of structure and focus on just the one bit of code that actually runs
############################################################
# Take in csv file fro mcommand line
if(len(sys.argv) >= 2):
    inputFile = str(sys.argv[1])
else:
    #warningChoose(1)
    inputFile = -1

# Take in initial node, works but doesnt run Dijkstras so oops
if(len(sys.argv) >= 3):
    initNode = str(sys.argv[2])
else:
    #warningChoose(2)
    initNode = -1

# checks if no input file specified. Enters a UI mode that is un-implemented
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
# Runs if csv is specified but initial node is not (ACTUAL PROGRAM)
elif(initNode == -1):
    # Normal Function
    # pulls in CSV data
    processCSV(inputFile)
    # Pulls in the node you want
    nodeChoice = chooseNode()
    # gets the dictionary of paths from dijkstras
    paths = dijkstras(nodeChoice)

    # the rest below is basically me parsing the dijkstras output to get it in the format in the pdf. It is quite boring but in order to now lose
    #           points I shall walk through the stupidity of parsing
    # This is the created dictionary, for each node it indicates if the tree part for it is created through a boolean
    created = {}
    for item in paths.items():
        created[item[0]] = False
    # this is paths in the format we want them in to print. We initialize here
    pathsOrderedTree = {}
    # we run this for the square of the len of the paths because if the order is reversed, we have to run this part 6+5+4+3+2+1 times, so it
    #           was easier to just multiply than to find the sum of all possible combinations, this algorithm isnt graded on efficiency
    for i in range(0, len(paths)*len(paths)):
        # now we parse through all parts of the paths that came from djikstras
        for item in paths.items():
            # if we have the initial node, we treat it special, just cuz we need an initial place to start (why it is 6+5+4+3+2+1)
            if(item[0] == nodeChoice):
                # we add the initial node to the dictionary to have something to access
                pathsOrderedTree[nodeChoice] = nodeChoice
                created[nodeChoice] = True
            else:
                # now all other nodes go through here. We first find the previous node from the paths data, then see if it has been created
                #           if it has been created then we use its path and append out nodes name to get this ones current path
                prevNode = item[1][1]
                if(created[prevNode] and not(created[item[0]])):
                    created[item[0]] = True
                    pathsOrderedTree[item[0]] = pathsOrderedTree[prevNode] + item[0]
    # print the shortest path tree basically
    outputPrintTrees = "Shortest path tree for node {}:\n".format(nodeChoice)
    for item in pathsOrderedTree.items():
        if(item[0] != nodeChoice):
            outputPrintTrees = outputPrintTrees + item[1] + ", "
    print(outputPrintTrees)
    # print the least costs paths for the nodes
    outputPrintPaths = "Costs of least-cost paths for node {}:\n".format(nodeChoice)
    for item in paths.items():
        outputPrintPaths = outputPrintPaths + item[0] + ":" + str(item[1][0]) + ", "
    print(outputPrintPaths)
# no worky, do not play
else:
    # advanced function
    print("Add this last when all functions are defined")
############################################################
