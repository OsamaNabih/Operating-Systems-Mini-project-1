import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.pyplot import bar
from tkinter import *
import numpy as np
from tkinter import messagebox
def readInput(file_name):
    nums = []
    try:
        with open(file_name) as f:
             for line in f:
                 arr = line.split()
                 nums.append(arr)
    except FileNotFoundError:
        messagebox.showerror("Error", "File does not exist!")
        return
    f.close()
    process_num = int(nums[0][0])
    mu1 = float(nums[1][0])
    sigma1 = float(nums[1][0])
    mu2 = float(nums[2][0])
    sigma2 = float(nums[2][1])
    my_lambda = float(nums[3][0])
    arrivals = np.random.normal(loc=mu1, scale=sigma1, size=process_num)
    bursts = np.random.normal(loc=mu2, scale=sigma2, size=process_num)
    priorities = np.random.poisson(lam=my_lambda, size=process_num)
    #mapped_priorities = np.arange(1, len(priorities) + 1)
    #sorted_priorities = np.argsort(priorities)
    #for i in range(process_num):
        #priorities[sorted_priorities[i]] = mapped_priorities[i]
    arrivals = np.round(arrivals, 2)
    bursts = np.round(bursts, 2)
    arrivals = np.abs(arrivals)
    bursts = np.abs(bursts)
    f = open("Output.txt", "w")
    f.write(str(process_num) + "\n")
    for i in range(process_num):
        f.write(str(i+1) + " " + str(arrivals[i]) + " " + str(bursts[i]) + " " + str(priorities[i]) + "\n")
    f.close()



def graph(root, data):
    f = Figure(figsize=(5.5, 5.5), dpi=100)
    a = f.add_subplot(111)
    frame = Frame()
    frame.grid(row=15, column=4)
    canvas = FigureCanvasTkAgg(f, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill=BOTH)
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack()
    plt.interactive(False)
    i = 0
    for process in data:
        col = "C" + str(i)
        if len(process.transitions) != 0:   #RR case
            for transition in process.transitions:
                if transition == process.transitions[0]: #Only the first one gets a label, in order not to have duplicates in legend
                    a.bar(x=transition[0], height=process.processNumber, width=transition[1] - transition[0],\
                      align="edge", color=col,  label="Process " + str(process.processNumber))
                else:
                    a.bar(x=transition[0], height=process.processNumber, width=transition[1] - transition[0], \
                          align="edge", color=col)
        else:   #All other non-preemptive algorithms
            a.bar(x=process.startTime, height=process.processNumber, width=process.endTime - process.startTime, align="edge", color=col,\
             label="Process " + str(process.processNumber))
        i += 1
    a.legend(loc='upper right', prop={'size': 6})
    return


def writeGlobalStats(data, outputFile):
    averageTAT = 0
    weightedAverageTAT = 0
    f = open(outputFile, 'w')
    for process in data:
        process.writeStats(f)
        averageTAT += process.TAT()
        weightedAverageTAT += process.weightedTAT()
    averageTAT /= len(data)
    weightedAverageTAT /= len(data)
    f.write("\naverage TAT = " + str(np.round(averageTAT, 2)) + "\nweightedAverageTAT = " \
              + str(np.round(weightedAverageTAT, 2)))
    f.close()