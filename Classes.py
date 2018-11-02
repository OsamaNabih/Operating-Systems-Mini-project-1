import numpy as np
precision = 2

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if (self.isEmpty()):
            print("unable to dequeue")
            return None
        node = self.items[0]
        del self.items[0]
        return node

    def size(self):
        return len(self.items)

    def front(self):
        if (self.isEmpty()):
            return None
        return self.items[0]

    def printQueue(self):
        for item in self.items:
            item.printProcess()

    def calculateStats(self, outputFile):
        averageTAT = 0
        weightedAverageTAT = 0
        f = open(outputFile, 'w')
        for item in self.items:
            item.writeStats(f)
            averageTAT += item.TAT()
            weightedAverageTAT += item.weightedTAT()
        averageTAT /= self.size()
        weightedAverageTAT /= self.size()
        f.write("\naverage TAT = " + str(np.round(averageTAT, 2)) + "\nweightedAverageTAT = " \
                + str(np.round(weightedAverageTAT, 2)))
        f.close()

class Process:
    def __init__(self, processNumber, arrivalTime, burstTime, priority):
        self.processNumber = processNumber
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.priority = priority

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.processNumber < other.processNumber
        return self.priority > other.priority


    def endTime(self, endTime):
        self.endTime = endTime
        return

    def startTime(self, startTime):
        self.startTime = startTime
        return

    def waitTime(self):
        return np.round((self.startTime - self.arrivalTime), precision)

    def TAT(self):
        return np.round((self.endTime - self.arrivalTime), precision)

    def weightedTAT(self):
        return np.round((self.endTime - self.arrivalTime) / self.burstTime, precision)

    def printProcess(self):
        print("PNumber: " + str(self.processNumber) + ", Arrival: " + str(self.arrivalTime) + ", Burst: " \
              + str(self.burstTime) + ", Priority: " + str(self.priority))

    def writeStats(self, f):
        f.write("Process #" + str(self.processNumber) + " wait time = " + str(self.waitTime()) + \
                " TAT = " + str(self.TAT()) + " weighted TAT = " + str(self.weightedTAT()) + " arrived at: " + \
                str(self.arrivalTime) + " started at: " + str(np.round(self.startTime, precision)) + " ended at: " \
                + str(np.round(self.endTime, precision)) + '\n')


def printProcessList(processArray):
    for i in processArray:
        print(str(i.processNumber) + " " + str(i.arrivalTime) + " " + str(i.burstTime) + " " + str(i.priority) )