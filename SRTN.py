from Classes import *
import numpy as np
from tkinter import messagebox
precision = 2
def SRTNscheduler(processArray, switchTime):
	myHeap = MyHeap(key = getTimeLeft)
	terminated = []
	exit = False
	time = 0.0 
	size = len(processArray)
	currentProcess = None
	cpuCycle = 0.1
	switchingTime = switchTime
	while(True):
		
		if(exit or (len(processArray) == 0 and len(terminated) == size)): ## will be changed 
			break
			
		while(len(processArray) > 0 and time >= float(processArray[0].arrivalTime)):
			myHeap.push(processArray[0])
			del processArray[0]
		if(currentProcess != None):
			if (currentProcess.getTimeLeft() <= 0):
				print("removing ended process and waiting for arrival of new process / switching process") 
				end = time + currentProcess.getTimeLeft() 
				currentProcess.setTransitions(start,end)
				terminated.append(currentProcess)
				currentProcess = None 
				
			if(currentProcess != None):
				currentProcess.setTimeLeft(cpuCycle)  
				
		if(myHeap.size() > 0):
			if(currentProcess != None):
				temp = myHeap.top()
				if(temp.getTimeLeft() < currentProcess.getTimeLeft()):
					end = time
					currentProcess.setTransitions(start,end)
					time += switchingTime
					currentProcess = myHeap.heapPushPop(currentProcess)
					currentProcess.setTimeLeft(cpuCycle)
					start = time
			else:
				
				print("putting a new process")
				currentProcess = myHeap.pop()
				print(currentProcess.printProcess())
				time += switchingTime
				start = time
				currentProcess.setTimeLeft(cpuCycle)

		time += cpuCycle
		time = np.round(time,5)
	f = "SRTNstats.txt"
	return (terminated, f)