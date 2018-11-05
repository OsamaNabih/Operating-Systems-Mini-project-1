import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import sys
from Functions import *
import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from Schedulers import *
def readFile():
    file_name = file_field.get()
    file_field.delete(0, END)
    file_field.insert(0, "")
    readInput(file_name)

root = Tk()
root.configure(background='white')
root.geometry("1280x800")

#theLabel = Label(root, text="Input File Name:", bg='yellow', fg='pink')
#theLabel.pack(fill=X)


def simulate():
    algo = options.get()
    switch_time = switch_field.get()
    quantum = quantum_field.get()
    if enum[algo] == 2:
        if quantum == "":
            messagebox.showerror("Error", "You must specify the quantum for Round Robin algorithm!")
            return
        quantum = float(quantum)
    if switch_time != "":
        switch_time = float(switch_time)
    else:
        messagebox.showerror("Error", "You must specify context switching time!")
    data, f = scheduler(enum[algo], switch_time, quantum)
    graph(root, data)
    writeGlobalStats(data, f)
    options.grid(row=15, column=7)

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
file_label = Label(root, text="Input File Name:")
switch_label = Label(root, text="Choose context switching time")
quantum_label = Label(root, text="Specify quantum")
switch_field = Entry(root)
inputFile = Button(text="Submit file name", fg='red', command=readFile)
schedule = Button(text="Start simulation!", fg='green', command=simulate)
quantum_field = Entry(root)
file_field = Entry(root)
file_label.grid(row=4, column=2)
file_field.grid(row=4, column=3)
inputFile.grid(row=5, column=2, columnspan=2)
algo_label = Label(root, text="Choose scheduling algorithm", bg='cyan')
switch_label.grid(row=5, column=7)
switch_field.grid(row=6, column=7)
algo_label.grid(row=4, column=8)
options.grid(row=5, column=8)
schedule.grid(row=6, column=8)
quantum_label.grid(row=4, column=9)
quantum_field.grid(row=5, column=9)
root.mainloop()