# Pandas is a fast, powerful and flexible to use open source, data analysis and manipulation tool. used to analyse data.

import pandas as pd
import numpy as np

#dataframe

df = pd.read_csv('Churn_Modelling.csv')

# print(df)

# print(df.head(5)) #view top 5 records
# print(df.tail(5)) #view top 5 records

# print(df.info()) #info about cols and data types and total memory size

# print(df.describe()) # describes the statisticla info of the numerical columns

# print(df.columns) #prints all cols

# print(df.T) #shows a transpose - rows become cols and cols become rows

# print(df.sort_values('Age')) #sort your data based on age

# print(df['Balance']) #print a particular column

# df['New Balance'] = df['Balance'] +1000

# print(df['New Balance'])

#Accessing rows and cols

# print(df[10:13])

# print(df[10:13])

#where clause

# print (df[df.Age >50]) #select * from df where age >50

# print (df['Age'].fillna(10)) #fills null values in age as 15

newdf = df

# print (newdf.pop('Age')) #remove a certain col
# # print(newdf.columns)

# newdf.drop('RowNumber',axis=1) #del a row
# print(newdf.head())
# print(newdf['Balance'])
# newdf['New Balance'] = newdf['Balance'].apply(np.sqrt)
# print(newdf['New Balance'])


#drop null value

newdf.dropna()

######################################################

#   CONCAT AND MERGING

#####################################################

# table 1
# cust_id, cuts_name
# 1, satyajit
# 2, hillary
# 3, raj
# 4,shankar

# table 2
# cust_id, salary
# 2, 1000
# 3,25000
# 5, 20000

# inner join output :
# custid, custname, salary
# 2, hillary,10000
# 3,raj,25000

# left join output:
# 1, satyajit
# 2, hillary , 10000
# 3, raj , 25000
# 4,shankar

# right join output:
# 2, hillary,10000
# 3,raj,25000
# 5,-,20000


# Sample DataFrame 1
df1 = pd.DataFrame({
    'cust_id': [1, 2, 3, 4],
    'cust_name': ['satyajit', 'hillary', 'raj', 'shankar']
})

# Sample DataFrame 2
df2 = pd.DataFrame({
    'cust_id': [2, 3, 5],
    'salary': [10000, 25000, 20000]
})

# print("DataFrame 1:")
# print(df1)
# print("\nDataFrame 2:")
# print(df2)


# merge_df = pd.merge (df1, df2,on='cust_id', how ="inner")
# select df1.* , df2.* from df1 inner join df2
# on df1.cust_id = df2.cust_id
# print(merge_df)

##########################################################
# LOC VS ILOC

#####################################################

# loc gets rows (and/or cols) with particular labels.
# iloc gets rows (and/or cols) at integer locations.

s = pd.Series(list("abcdef"), index =[49,48,47,0,1,2])
# print(s.loc[0]) # at col with label 0
# print(s.iloc[0]) #0th row of table

# print(s.loc[0:2]) # at col with label 0
# print(s.iloc[0:2]) #0th row of table

######### sort a series
s= s.sort_index() #sorted by nums
print(s)


s= s.sort_values() #sorted by values
print(s)


