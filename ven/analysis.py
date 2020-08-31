import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import the visitors.csv data of visitors during 2008-2017
visitors = pd.read_csv('visitors.csv')

#prints out the data
print(visitors)

print(visitors.columns)

print(visitors.index) #prints original index

#visitors= visitors.assign(visitor_month=visitor[0])
#visitors= visitors.assign(visitor_peryear=visitor[1])
#visitors[visitors['visitor_month'] == 'Jan']

#visitors.index = visitors['Month/Year']
#del visitors['Month/Year']
#print(visitors.index)

#visitors.iloc[:,:6].describe()

print(visitors.mean)

print(visitors.sum())


visitors.plot(kind='bar')
plt.show()