import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import sys
from Functions import *
import time
from tkinter import *
from tkinter.ttk import Combobox
from Schedulers import *
def readFile():
    file_name = inputEntry.get()
    inputEntry.delete(0, END)
    inputEntry.insert(0, "")
    readInput(file_name)

root = Tk()
root.configure(background='white')
root.geometry("1000x800")

#theLabel = Label(root, text="Input File Name:", bg='yellow', fg='pink')
#theLabel.pack(fill=X)

def simulate():
    print(options.get())
    algo = options.get()
    options.grid_forget()
    data = scheduler(enum[algo])
    graph(root, data)
    options.grid(row=5, column=7)
'''
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
'''

enum = {'HPF': 0, 'FCFS': 1, 'RR': 2, 'SRTN': 3}
schedule_algos = ['HPF', 'FCFS', 'RR', 'SRTN']
options = Combobox(root, values=schedule_algos)
options.set("HPF")
theLabel = Label(root, text="Input File Name:")
inputFile = Button(text="Submit file name", fg='red', command=readFile)
schedule = Button(text="Start simulation!", fg='green', command=simulate)
inputEntry = Entry(root)
theLabel.grid(row=4, column=2)
inputEntry.grid(row=4, column=3)
inputFile.grid(row=5, column=2, columnspan=2)
theLabel2 = Label(root, text="Choose scheduling algorithm", bg='cyan')
theLabel2.grid(row=4, column=7)
options.grid(row=5, column=7)
schedule.grid(row=6, column=7)
root.mainloop()

