#Graphing app by Landen and Mason
#Graphing version 1.0
#Imports
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
import csv
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

#Creating the import data function
def import_csv_data():
    global v
    #choosing which file you want
    csv_file_path = askopenfilename()
    v.set(csv_file_path)
#Defining the plot
def plot():
    x = []
    y = []
    
    #Plotting the file that was selected
    with open(askopenfilename(), 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')
        for row in plots:
            x.append(row[1])
            y.append(row[0])

    #Creating and editing the line for the graph
    plt.plot(x, y, color = 'g',linestyle = 'solid',marker= 'o', label= '')
    #X label name
    plt.xlabel('')
    #Y label name
    plt.ylabel('')
    #Title of the Plot
    plt.title('PLOT')
    plt.grid()
    plt.legend()
    #Showing the graph
    plt.show()


root = tk.Tk()
#Title of the window
root.title("Plot")
#Size of the window
root.geometry('150x50')
v = tk.StringVar()
#Background color of the window
root.configure(bg="blue")
#Button to chose the data and plot the data
tk.Button(root, text='Plot a File',command=plot).grid(row=1, column=0)
#Button to close the app
tk.Button(root, text='Close',command=root.destroy).grid(row=1, column=1)
root.mainloop()
