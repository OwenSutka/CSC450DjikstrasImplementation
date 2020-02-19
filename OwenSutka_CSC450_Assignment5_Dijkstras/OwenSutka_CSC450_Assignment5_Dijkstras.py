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
global nodeNames, edgeNamesWeights, nodeChoice
nodeNames = []
edgeNamesWeights = {} # format is uu:0,uv:7,vu:7 ......
nodeChoice = ""

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


# Functions
############################################################
# This function will take the csv file name as input and will find it and assign some of the global variables some values
def processCSV():
    print("processing the CSV")

# This function chooses a node and then returns that value
def chooseNode():
    finalNode = -1
    # while loop to force the person to choose a valid combo for a node
    while(1):
        try:
            node = str(input("\nPlease, provide the node's name: "))
            break
        except ValueError:
            errorChoose(1)
    # Check all nodes for the value specified
    for i in range(0, len(nodeNames)):
        if(node == nodeNames[i]):
            finalNode = node
            break
        else:
            finalNode = -1
    # runs an error if the value specified is not in the list of nodes
    if(finalNode == -1):
        finalNode = ""
        errorChoose(2)
    # return the final node
    return finalNode
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
            programNum = int(input("\n\nWhat Program would you like to run?\n0. Exit\n1. Set CSV file\n2. Set Starting Node\n3. Find Shortest Paths of Set Node\n4. Find Shortest Paths of all Nodes/n/n"))
        except ValueError:
            errorChoose(4)
            programNum = -1
        if(programNum == -1):
            errorChoose(1)
        else:
            runProgram(programNum)
elif(initNode == -1):
    # Normal Function
    processCSV(inputFile)
    nodeChoice = chooseNode()
    shortestPathTree(nodeChoice)
    leastCosts(nodeChoice)
else:
    # advanced function
    print("Add this last when all functions are defined")
############################################################
