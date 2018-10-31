import numpy as np
import matplotlib as plt
from tkinter import *
root = Tk()
root.geometry("500x300")
theLabel = Label(root, text="Input File Name:", bg='yellow', fg='pink')
#theLabel.pack(fill=X)


'''
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
'''
def readInput():
    file_name = inputEntry.get()
    nums = []
    with open(file_name) as f:
        for line in f:
            arr = line.split()
            nums.append(arr)
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
    mapped_priorities = np.arange(1, len(priorities) + 1)
    sorted_priorities = np.argsort(priorities)
    for i in range(process_num):
        priorities[sorted_priorities[i]] = mapped_priorities[i]
    arrivals = np.round(arrivals, 2)
    bursts = np.round(bursts, 2)
    arrivals = np.abs(arrivals)
    bursts = np.abs(bursts)
    f = open("Output.txt", "w")
    f.write(str(process_num) + "\n")
    for i in range(process_num):
        f.write(str(i+1) + " " + str(arrivals[i]) + " " + str(bursts[i]) + " " + str(priorities[i]) + "\n")

inputFile = Button(text="Submit file name", fg='red', command= readInput)
schedule = Button(text="Submit scheduling method", fg='green')
inputEntry = Entry(root)
theLabel.grid(row=4, column=2)
inputEntry.grid(row=4, column=3)
inputFile.grid(row=5, column=2, columnspan=2)
#inputFile.pack(side=LEFT)
#schedule.pack(side=RIGHT)



root.mainloop()