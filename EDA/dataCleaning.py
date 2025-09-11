import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Python\Churn_Modelling.csv')


#How to find null values presence ?-------------------

# print(df.info()) #gives info of null values in dataset
# print(df.isnull().sum())


# How to handle null values? --------------------------

#column drop...................
updated_df = df.dropna(axis=1) #drops columns with null values...should only be used if there are too many null values and valuable data is not lost

#row drop...........
# updated_df = df.dropna(axis=0) #deletes rows with null values

#filling missing values-  imputation..........

    #(mean,median if numreical)
    # mode if categorical
    # filling the data with 0 or -999 or some other number that will not occur in data. this is done so as to machine may recognise that data is not real or is diff.
    # filling categorical data with new type for missing value

df['Age'].mean() , df['Age'].median()

updated_df = df

#fill with mean (helpful when less outliers)
updated_df['Age']=updated_df['Age'].fillna(df['Age'].mean())

#fill with median (helpful when more outliers)

#forward and backward fillling
#previous or next value is copied to the nul value
# updated_df = df['Age'].bfill() or ffill()

#no thumb rule which approach is better its hit and trial , try filling null values with diff data and check model accuracy.

#time series forecasting algo  