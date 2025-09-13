import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from category_encoders import TargetEncoder
from category_encoders import HashingEncoder

df=pd.read_csv('Python\Churn_Modelling.csv')
# print(df.head())

#------ENCODING TECHNIQUES----------------------------



# 1. Label Encoding --------------------------------

# gives nums like 0, 1 ,2 
le = preprocessing.LabelEncoder()
df['Gender_Label'] = le.fit_transform(df.Gender.values)
# print(df['Gender_Label'])



# 2. One Hot Encoding---------------------------------

# sklearn one hot encoders or get dummies function

# one_hot = pd.get_dummies(df['Geography'])
# print(one_hot)

#doing for all at once
df_dummies = pd.get_dummies(df)
#creates gender_female, gender_male, geography_france etc labels in df.
# print(df_dummies.head())



# 3. Dummy Encoding----------------------------------

df_dummies_de = pd.get_dummies(df, drop_first=True)
# drops one redundant column
# print(df_dummies_de.head())



# 4. Target Encoding ---------------------------------

# sklearn target encoder present inside sklearn categiry encder
# pip install category encoders
encoder = TargetEncoder()
df1=pd.read_csv('Python\Churn_Modelling.csv')
# df1['Gender Encoded'] = encoder.fit_transform(df1['Gender'],df1['Exited'])
#creates the numerical values based on some mathematical calculaitions
# print(df1[['Gender','Exited','Gender Encoded']].head())
# TargetEncoder encodes categorical features (X) based on a target column (y, usually numeric like churn/Exited).

# Benefits of TE -
    # simple and quick encoding method that doesnot add to dimensionality of the dataset. Therefore a good first try technique.
    # (new col is created and prev categorical col is deleted  but in one hot encoding way too many new cols are created increasing dimension of the table)

# Limitations of TE -
    # dependent of distribution of the target meaning it requires careful validation as it can be prone to overfitting (overfitting - when model performs good on practice data but not on new or unseen data)



# 5. Hash Encoding -----------------------------------

# categorical encoders hash encoders 
# multivariate hashing implementation with configurable dimensionality / precision.
# 8 cols are created

x = df[['Gender']]
y = df['Exited']

ce_hash = HashingEncoder(cols = ['Gender'],n_components=8)
x_hashed = ce_hash.fit_transform(x,y)

#gives 8 hashed cols achieved from gender cols

print(x_hashed.head())