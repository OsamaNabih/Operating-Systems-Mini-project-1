from Classes import *
import numpy as np
from tkinter import messagebox
precision = 2
def RRscheduler(processArray, switchTime, quantum):
	queue = Queue()
	terminated = []
	exit = False
	time = 0.0 
	size = len(processArray)
	currentProcess = None
	quantumTime = quantum
	cpuCycle = 0.1
	switchingTime = switchTime
	while(True):
		if(exit or (len(processArray) == 0 and len(terminated) == size)): ## will be changd 
			break
		while(len(processArray) > 0):
			if(time >= float(processArray[0].arrivalTime)):
				queue.enqueue(processArray[0])
				del processArray[0]
		if(currentProcess != None):
			print("time left " + str(currentProcess.getTimeLeft()))
			print("quantumTime " + str(quantumTime))
			if (currentProcess.getTimeLeft() <= 0):
				print("removing ended process and waiting for arrival of new process / switching process") 
				end = time + currentProcess.getTimeLeft()  ## here we add the currentProcess
														## to get the exact time it ended as if it ended in the middle
														## of the cpu cycle we should have the time it ended 
														## assumption that i can know the time between cpu cycles if not remove 
														## all comments
				currentProcess.setTransitions(start,end)
				terminated.append(currentProcess)
				currentProcess = None  ## not to enter the set transitions twice in here and in the quantum less than 0 
				## here we check if the quantim didnt end and that if it is the last process we will decrement otherwise 
				## we wont decrement and we will switch processes
			if((currentProcess != None and quantumTime > 0) or (currentProcess != None and queue.size() == 0)):
			  
				currentProcess.setTimeLeft(cpuCycle)    
				
		if(not queue.isEmpty()):
			if(currentProcess != None):                  
				if(quantumTime <= 0):
					print("switching Process")
					end = time          ## as if quantum becomes negative it means that the process finished 
													## in the middle of the cpu cycle so i have to put the correct time quantum
													## = 1.5 and cpu time = 1 that will happen 
					currentProcess.setTransitions(start,end)
					queue.enqueue(currentProcess)
					time += switchingTime
					quantumTime = quantum
					currentProcess = queue.dequeue()
					currentProcess.setTimeLeft(cpuCycle)
					start = time
					
					
			elif(currentProcess == None):
				print("putting a new process")
				currentProcess = queue.dequeue()
				time += switchingTime
				start = time
				quantumTime = quantum
				currentProcess.setTimeLeft(cpuCycle)
		time += cpuCycle
		time = np.round(time,5)
		quantumTime -= cpuCycle
		##print("time " + str(time) + " quantum " + str(quantumTime) + " time left " + str(currentProcess.getTimeLeft()) \
		##      + " length of queue " + str(queue.size()) )
	f = "RRstats.txt"
	for process in terminated:
		print("Process #  " + str(process.processNumber) + "\n" )
		process.getTransitions()
	return (terminated, f)