import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns



df = pd.read_csv('Python\Churn_Modelling.csv')
# print(df.info())

# print(df.Age.min()) #18
# print(df.Age.max()) #92

labels = ['0-20','21-40','41-60','Above 61']
bins = [0,20,40,60,100]

df['Age_bins'] = pd.cut(df.Age,bins,labels = labels ,include_lowest =True)  (IMPT)  

# df[['Age_bins','Age']].to_csv('test.csv') 

# print(df.Age_bins.value_counts()) 
#value_counts like group function sql

def add_labels(x,y):
    for i in range (len(x)):
        plt.text(i,y[i],y[i])

plt.bar(labels,df['Age_bins'].value_counts())

add_labels(labels,df['Age_bins'].value_counts())
plt.xlabel('Age Ranges')
plt.ylabel('count')
plt.title('Age Distribution')
plt.show()