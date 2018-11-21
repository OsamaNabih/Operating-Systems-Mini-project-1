from Classes import *
import numpy as np

precision = 2

def FCFSscheduler(processArray, switch_time):
    ## Sort the Process on the time of arrival
    q = Queue()
    processQ = Queue()
    for process in processArray:
        processQ.enqueue(process)
    time = -0.1
    endTime = 0.0
    busy = False
    exit = False
    terminated = []
    context_switch = switch_time
    while (True):
        time = np.round(time + 0.1, precision)
        if (exit or (len(terminated) == len(processArray))):
            break
        while not processQ.isEmpty():
            if (processQ.front().arrivalTime <= time):
                q.enqueue(processQ.dequeue())
        if busy:
            if time < endTime:
                continue
            else:
                terminated.append(curr_process)
                busy = False
        if q.isEmpty():
            continue
        elif q.front().arrivalTime <= time:
            busy = True
            curr_process = q.dequeue()
            curr_process.startTime = time + context_switch
            curr_process.endTime = curr_process.startTime + curr_process.burstTime
            endTime = curr_process.endTime
    f = "FCFSstats.txt"
    return (terminated, f)