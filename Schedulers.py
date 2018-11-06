import numpy as np
from Classes import *
from HPF import *
from FCFS import *
from RR import *
from SRTN import *
from tkinter import messagebox

def scheduler(algo, switch_time, quantum):
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
    processArray = sorted(processArray, key=lambda process: float(process.arrivalTime))
    if algo == 0:
        data, f = HPFscheduler(processArray, switch_time)
    elif algo == 1:
        data, f = FCFSscheduler(processArray, switch_time)
    elif algo == 2:
        data, f = RRscheduler(processArray, switch_time, quantum)
    elif algo == 3:
        data, f = SRTNscheduler(processArray, switch_time)
    else:
        print("Invalid algorithm")
    return (data, f)
