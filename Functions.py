import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
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
    time, process = data
    time.append(0)
    process.append(0)
    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    a.plot(time, process)
    frame = Frame()
    frame.grid(row=15, column=4)
    canvas = FigureCanvasTkAgg(f, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill=BOTH)
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack()
    plt.interactive(False)
    plt.plot(time, process)
    time = 0.0
    process = 0.0
    plt.interactive(False)
    plt.plot(time, process)