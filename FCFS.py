from Classes import *
import numpy as np

precision = 2

def FCFSscheduler(processArray, switch_time):
    ## Sort the Process on the time of arrival
    context_switch = switch_time
    processArray = sorted(processArray, key=lambda process: float(process.arrivalTime))
    q = Queue()
    processQ = Queue()
    for process in processArray:
        processQ.enqueue(process)
    time = -0.1
    endTime = 0.0
    busy = False
    exit = False
    terminated = Queue()
    context_switch = switch_time
    data_t = []
    data_p = []
    PN = 0
    switching = False
    remaining_switch = 0
    while (True):
        time = np.round(time + 0.1, precision)
        if switching == True:
            remaining_switch = np.round(remaining_switch - 0.1, precision)
        if remaining_switch <= 0:
            switching = False
        if (exit or (terminated.size() == len(processArray))):
            break
        if not processQ.isEmpty():
            if (processQ.front().arrivalTime <= time):
                q.enqueue(processQ.dequeue())
        if switching:
            data_p.append(0)
        else:
            data_p.append(PN)
        data_t.append(time)
        if busy:
            if time < endTime:
                continue
            else:
                terminated.enqueue(curr_process)
                PN = 0
                busy = False
        if q.isEmpty():
            continue
        elif q.front().arrivalTime <= time:
            busy = True
            curr_process = q.dequeue()
            curr_process.startTime = time + context_switch
            switching = True
            remaining_switch = context_switch
            curr_process.endTime = curr_process.startTime + curr_process.burstTime
            endTime = curr_process.endTime
            PN = curr_process.processNumber
        if switching:
            data_p.append(0)
        else:
            data_p.append(PN)
        data_t.append(time)
    f = "statsFCFSOsama.txt"
    terminated.calculateStats(f)
    data_t.append(time)
    data_p.append(0)
    return (data_t, data_p)