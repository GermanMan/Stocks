import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader as data
import os

style.use("ggplot")
print('Hello! Welcome to my stock finder!')
#While loop allows the user to search as many stocks as they wish and stop when ever they want 
use = True
while use == True:
    
    #stock gets the stock and info gets what about the stock the user wants to see
    stock = str(input("What stock would you like to see: "))
    info = str(input('What information on this stock would you like to see? ie: High, Low, Open, Close: '))

    #lets user input specific dates
    inYear= int(input('What year: '))
    inMonth= int(input('What month: '))
    inDay= int(input('What day: '))
    endYear= int(input('What year: '))
    endMonth= int(input('What month: '))
    endDay= int(input('What day: '))    
    start = dt.datetime(inYear, inMonth, inDay)
    end = dt.datetime(endYear, endMonth, endDay)

    #df creates a data frame for the stock
    df = data.DataReader(stock, 'yahoo', start, end)

    #csv makes a new file with all the stock info so it doesn't crash  
    df.to_csv(stock+'.csv')

    #makes a graph for the stock
    df[[info]].plot()
    plt.show()
    again = str(input('Would you like to view another stock? y/n'))
    if again == 'y':
        os.remove(stock+'.csv')
        use = True
    else:
        os.remove(stock+'.csv')
        use = False
    
    
