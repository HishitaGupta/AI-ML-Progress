# SeaBorn - data visualisation
# pip install seaborn

import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------------------------------
df = sb.load_dataset('iris') #predefined dataset
#seaborn internally uses pandas to represent the dataset.
# print(df.head())
# print(df.species.value_counts())
#pandas method - value_counts()
# -------------------------------------------------------

# Various Methods in Seaborne-------------------------

# 1. kde plot - kernel density estimate plot
# sb.kdeplot(df['sepal_length'])
# plt.show()


# 2. distplot - combination of kde with histogram
# sb.displot(df['sepal_length'])

# for col in ['sepal_length', 'sepal_width','petal_length','petal_width']:
#     sb.kdeplot(df[col], shade='True');
# plt.show()

# 3. pairplot - plots the pair wise relationship in dataset (like individually its height vs weight, weight vs age etc but we can combine them using pairplot)

# -------------------------------------------------
Data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Exchange Rate': [65.12, 68.45, 70.23, 74.56, 76.89]
}

#first convert the data to pandas dataframe

df = pd.DataFrame(Data , columns = ['Year' ,'Exchange Rate'])

# print(df)

sb.lineplot(x=df["Year"],y=df["Exchange Rate"])
plt.show()
# --------------------------------------------------


# Other impt data visulaisation libs - plotly(interactive)