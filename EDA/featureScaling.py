# pip install -U scikit-learn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
 

df = pd.read_csv('Python\Churn_Modelling.csv')



# print(df.describe())


new_df = pd.DataFrame(df,columns=['Age','Tenure'])
# print(new_df.head())

#-------First - Normalisation ----------------------


    #imputing null records
new_df['Age']= new_df['Age'].fillna(new_df['Age'].mean())
new_df['Tenure']= new_df['Tenure'].fillna(new_df['Tenure'].mean())

    #using minmaxscaler
scaler = MinMaxScaler() #instantiating the function
normalised_df = scaler.fit_transform(new_df)
# print(normalised_df)

# -------- Second  - Standardisation -------------------

newUpdated_df =  pd.DataFrame(df,columns=['Age','Tenure'])

     #imputing null records
new_df['Age']= new_df['Age'].fillna(new_df['Age'].mean())
new_df['Tenure']= new_df['Tenure'].fillna(new_df['Tenure'].mean())

    # standardisation
scaler = StandardScaler()
standardised_df = scaler.fit_transform(newUpdated_df);
print(standardised_df)

