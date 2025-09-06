# matplotlib
# library used for graphical representation of values.pip install matplotlib -> import matplotlib as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# matplotlib.pyplot is a state-based interface to matplotlib. It provides an implicit, MATLAB-like, way of plotting. It also opens figures on your screen, and acts as the figure GUI manager.

# pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation:

Data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Exchange Rate': [65.12, 68.45, 70.23, 74.56, 76.89]
}
# print(type(Data))
# print(Data)

#first convert the data to pandas dataframe

df = pd.DataFrame(Data , columns = ['Year' ,'Exchange Rate'])
#doesnt need to mention column everytime


# print(type(df))
# print(df)


# Plotting-----------------------------------------
# df.plot(x='Year' , y='Exchange Rate', kind ='scatter')
# plt.show()
#pandas method
# kind = bar, barh , pie , line, scatter

# plt.scatter(df['Year'],df['Exchange Rate'])
# plt.show()
# matplotlib method

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([10, 20, 30, 40, 50])
# plt.scatter(x,y);
# plt.show()
# ---------------------------------------------------

# plot a pie chart----------------------------------
# PieData = {'Tasks':[100,500,300]}
# df = pd.DataFrame(PieData , columns =['Tasks'], index =['Pending','Complete','Ongoing'])
# # if indexes not derfined default indexes will be used 0,1,2
# print(df)
# df.plot.pie(y='Tasks',figsize =(5,5))
# plt.show()
# ------------------------------------------------------

# Analysis a data set--------------------------------
newDf = pd.read_csv('Churn_Modelling.csv')
# print(newDf.columns)
#*****Finding how many no. of records for each geography
#sql - select Geograpgy, count(*)
# from tablename
# group by geography
# print(newDf.Geography.value_counts())
#py
# newDf.Geography.value_counts().plot(kind ='barh')
# to find percentage
# (newDf.Geography.value_counts()/(len(newDf)*100)).plot(kind='barh')
# plt.show()
# -----------------------------------------------------

# Mean salary comparison acc to geography--------------
# plt.bar(newDf['Geography'],newDf['EstimatedSalary'].mean(),color ="cyan")
# plt.title('Geography vs Estimated Salary')
# plt.show()
# ----------------------------------------------------- 

# Line Chart -------------------------------------------
x=np.linspace(0,10,100) # returns evenly spaced nums bw a particular range
y=np.sin(x) # returns sin of each value in x
# plt.plot(x, y, label="sin(x)")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Line Chart Example")
# plt.legend()
# plt.show()
# print(y)
# ------------------------------------------------------

#BarChart----------------------------------------------
# categories = ["A", "B", "C", "D"]
# values = [5, 7, 3, 8]

# plt.bar(categories, values, color="skyblue") #use barh for horizontal bar chart
# plt.title("Bar Chart Example")
# plt.ylabel("Value")
# plt.show()
# ------------------------------------------------------

#Histogram---------------------------------------------
#used to show distribution of continuous data
data = np.random.randn(1000)
#generates random numbers from a normal (Gaussian) distribution with mean = 0 and standard deviation = 1.

# plt.hist(data, bins=30, edgecolor="black")
# #less bins less detail more bins more detail
# plt.title("Histogram Example")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
# ------------------------------------------------------

#Scatter Plot ------------------------------------------
# shows relationship bw two variables
# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.scatter(x, y)
# plt.title("Scatter Plot Example")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()
# ------------------------------------------------------

# #PieChart----------------------------------------------
# sizes = [20, 30, 25, 25]
# labels = ["A", "B", "C", "D"]

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# #'%.1f%%' → 12.3% -> visual representation format
# plt.title("Pie Chart Example")
# plt.show()
# ------------------------------------------------------


#Stacked Bar Chart-------------------------------------
# men = [20, 35, 30, 35]
# women = [25, 32, 34, 20]
# categories = ["G1", "G2", "G3", "G4"]

# plt.bar(categories, men, label="Men")
# plt.bar(categories, women, bottom=men, label="Women")
# plt.title("Stacked Bar Chart Example")
# plt.legend()
# plt.show()
# ------------------------------------------------------


#Box Plot (Whisker Plot)--------------------------------
# When to use: Show spread and outliers.
# data = [7, 8, 5, 6, 4, 5, 6, 9, 10, 6, 7, 8]

# plt.boxplot(data)
# plt.title("Box Plot Example")
# plt.show()
#helps to understand five measure 25th, 50th, 75th and so on 
# ---------------------------------------------------

#Bubble Chart---------------------------------------
# Like scatter but size of points varies.
# x = np.random.rand(20)
# y = np.random.rand(20)
# sizes = np.random.randint(50, 500, size=20)

# plt.scatter(x, y, s=sizes, alpha=0.5, color="purple", label="Bubble Data")
# plt.title("Bubble Chart Example")
# plt.show()
# ----------------------------------------------------

#pulled Out slice in pie chart-----------------------
labels_ex = 'JavaScript', 'Java', 'Python', 'R'
sizes = [15, 30, 45, 10]
explode_labels = (0, 0.5, 0, 0)   # Explode only the second slice (Java)
fig1, ax1 = plt.subplots()

ax1.pie(
    sizes, 
    explode=explode_labels, 
    labels=labels_ex, 
    shadow=True, 
    startangle=90
)
ax1.axis('equal')
#Set equal scaling (circle, not ellipse)
plt.show()

# fig1 → the Figure (the whole canvas).
# ax1 → the Axes object (a specific plot area inside the figure).
# Think of:
# Figure = a big sheet of paper.
# Axes = one plot (box) inside that paper.
# You can have multiple axes in one figure (subplots makes this easy).
# So ax1 is the first (and only) axis here.
# -----------------------------------------------------
