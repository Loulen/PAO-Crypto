import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime
import matplotlib.dates as mdates

def createGraph(path):
    date=[]
    values=[]
    with open(path, newline='') as f:
        reader=csv.reader(f)
        for row in reader:
            date.append(int(row[1]))
            values.append(float(row[2]))
        plt.plot(date, values)
        plt.show()
