from Classes import *
import numpy as np
from heapq import heappush, heappop

precision = 2

def HPFscheduler(processArray, switch_time):
    ## Sort the Process on the time of arrival
    process_num = len(processArray)
    processQ = Queue()
    for process in processArray:
        processQ.enqueue(process)
    heap = []
    time = -0.1
    endTime = 0.0
    busy = False
    exit = False
    terminated = []
    context_switch = switch_time
    while True:
        time = np.round(time + 0.1, precision)
        if (exit or (len(terminated) == process_num)):
            break
        while (not processQ.isEmpty() and processQ.front().arrivalTime <= time):
                heappush(heap, processQ.dequeue())
        if busy:
            if time < endTime:
                continue
            else:
                terminated.append(curr_process)
                busy = False
        if len(heap) == 0:
            continue
        elif heap[0].arrivalTime <= time:
            busy = True
            curr_process = heappop(heap)
            curr_process.startTime = time + context_switch
            curr_process.endTime = curr_process.startTime + curr_process.burstTime
            endTime = curr_process.endTime
    f = "HPFstats.txt"
    return (terminated, f)