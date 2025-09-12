import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import seaborn as sns


#   OUTLIER TREATMENT TECHNIQUES

# 1.--3 SIGMA  TECHNIQUE (STANDARD DEVIATION)-----------

df = pd.read_csv('Python\Churn_Modelling.csv')
# print(df.info())

#function to detect outlier on one dimensional dataset

def find_anomalies(data):
    #define a list to accumulate anomalies
    anomalies =[]

    #set upper and lower limit to 3 standard deviations
    random_data_std = statistics.stdev(data)
    random_data_mean = statistics.mean(data)

    anomaly_cut_off = random_data_std *3

    lower_limit = random_data_mean - anomaly_cut_off
    upper_limit = random_data_mean + anomaly_cut_off

    #Generate ouliers
    for outlier in data :
        if outlier > upper_limit or outlier < lower_limit:
            anomalies.append(outlier)
    return anomalies

# print(len(find_anomalies(df['Age']))) #total 133 = 0.0133%

#find skewness of data
# print(df.Age.skew()) #->positive value ->data is positively skewed

# sns.kdeplot(df['Age']) # -> to check distribution of data
# plt.show()

#transformation to lessen the anomalies

df['Age'] = np.log(df['Age'])
# now check anomalies 
# print(len(find_anomalies(df['Age'])))
#now check skewess and check kdeplot
# print(df.Age.skew()) #->0.1820
# sns.kdeplot(df['Age']) # -> more close to normal distribution
# plt.show()

# 2.--BOXPLOTS------------------------------------------

# sns.boxplot(df['Age']) #still has outliers
# plt.show()
#spot rounded outliers in box plot

# 3.--INTER-QUARTILE RANGE-----------------------------

# Q3-Q1

import numpy as np
import pandas as pd

# Sample data
data = [7, 8, 5, 6, 5, 4, 100, 6, 5, 7, 6, 8, 7, 5, 120]

series = pd.Series(data)

# Step 1: Calculate Q1, Q3
Q1 = series.quantile(0.25)
Q3 = series.quantile(0.75)

# Step 2: Calculate IQR
IQR = Q3 - Q1

# Step 3: Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# the multiplier (1.5, 3, etc.) is a tuning parameter depending on how strict you want to be.

# Step 4: Remove outliers
filtered_data = series[(series >= lower_bound) & (series <= upper_bound)]

print("Original Data:", series.values)
print("Filtered Data (Outliers Removed):", filtered_data.values)

# 4. --OUTLIER ALGORITHMS-----------------------------