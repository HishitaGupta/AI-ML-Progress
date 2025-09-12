import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns



df = pd.read_csv('Python\Churn_Modelling.csv')
# print(df.info())

# Target -> #################################
# What are the characteristics of the people    that have churned and why ?
# ###########################################



# Univariate analysis-----------------------------

new_df = pd.DataFrame(df,columns=['Geography','Age','Exited'])
# print(new_df.info())

#plot

# for i , predictor in enumerate (new_df.drop(columns=['Exited']).columns):
#     plt.figure()
#     sns.countplot(data = new_df, x= predictor , hue= 'Exited')
#     plt.show()
#calculate churn ratios for above like males in germany etc. and compare with original churn ratio

#original churn ratio
original_churn_ratio = (df['Exited'].value_counts()/len(df['Exited']))*100 # 20% 
# print(original_churn_ratio)
   
# ----------------------------------------------------


# Bivariate Analysis ----------------------------------

# sns.histplot(x ='Exited',hue='Geography',data = new_df, stat='count',multiple="dodge")
# plt.show()

df_exited1 = new_df.loc[new_df['Exited']==1]
df_exited1.info()

# sns.histplot(x ='Exited',hue='Geography',data = df_exited1, stat='count',multiple="dodge")
# plt.show()

#find ratios and check with original
#female staying in germany are more churners


# Numerical Analysis ----------------------------------

#correlation

new_df2 = pd.DataFrame(df,columns=['EstimatedSalary','Age','Exited'])
print(new_df2.corr() )
#kind of heatmap of correlation with values of correlation
#age and exited have high correlation

# plt.figure(figsize=(20,8))
# new_df2.corr()['Exited'].sort_values(ascending=False).plot(kind='bar') #correlation with respect to exited
# plt.show()


#heatmap
# sns.heatmap(new_df2.corr(),cmap='Paired')
# plt.show()


#line chart of age sorted in ascending
# new_df2['Age'].value_counts().sort_index(ascending=True).plot() #original
# df_exited1['Age'].value_counts().sort_index(ascending=True).plot() #of exited only
# plt.show()

#kdeplot
tot = sns.kdeplot(df.Age[df["Exited"]==0],color="Blue",shade="True")
tot = sns.kdeplot(df.Age[df["Exited"]==1],color="Red",shade="True")
tot.legend(["No Churn","Churn"], loc ='upper right')
tot.set_ylabel('Density')
tot.set_xlabel('Age')
tot.set_title('Age By Churn')

plt.show()