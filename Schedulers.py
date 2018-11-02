import numpy as np
from Classes import *
from HPF import *
from FCFS import *
from RR import *
from SRTN import *


def scheduler(algo):
    ## Take input from the file in an array of process
    inputFile = open("Output.txt", 'r')
    processArray = []

    for line in inputFile:
        line = line.split(" ")
        if len(line) == 1:
            continue
        temp = Process(int(line[0]), float(line[1]), float(line[2]), int(line[3]))
        processArray.append(temp)

    inputFile.close()
    if algo == 0:
        data = HPFscheduler(processArray)
    elif algo == 1:
        data = FCFSscheduler(processArray)
    elif algo == 2:
        data = RRscheduler(processArray)
    elif algo == 3:
        data = SRTNscheduler(processArray)
    else:
        print("Invalid algorithm")

