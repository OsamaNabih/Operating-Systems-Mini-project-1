from Classes import *
import numpy as np
from heapq import heappush, heappop

precision = 2

def HPFscheduler(processArray, switch_time):
    ## Sort the Process on the time of arrival
    processArray = sorted(processArray, key=lambda process: float(process.arrivalTime))
    printProcessList(processArray)
    process_num = len(processArray)
    processQ = Queue()
    for process in processArray:
        processQ.enqueue(process)
    heap = []
    time = -0.1
    endTime = 0.0
    busy = False
    exit = False
    terminated = Queue()
    context_switch = switch_time
    data_t = []
    data_p = []
    PN = 0
    while True:
        time = np.round(time + 0.1, precision)
        if (exit or (terminated.size() == process_num)):
            break
        if not processQ.isEmpty():
            if (processQ.front().arrivalTime <= time):
                print("Inserted at: " + str(time))
                heappush(heap, processQ.dequeue())
        data_p.append(PN)
        data_t.append(time)
        if busy:
            if time < endTime:
                continue
            else:
                #print("Finished at: " + str(time))
                terminated.enqueue(curr_process)
                PN = 0
                busy = False
        if len(heap) == 0:
            continue
        elif heap[0].arrivalTime <= time:
            busy = True
            curr_process = heappop(heap)
            curr_process.startTime = time + context_switch
            curr_process.endTime = curr_process.startTime + curr_process.burstTime
            endTime = curr_process.endTime
            PN = curr_process.processNumber
        data_p.append(PN)
        data_t.append(time)
    f = "statsHPFSOsama.txt"
    terminated.calculateStats(f)
    data_t.append(time)
    data_p.append(0)
    return (data_t, data_p)