#import the libraries
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

# DATA EXPLORATION #####################################

#load the dataset
df = pd.read_csv('CustomerChurn.csv')

# print(df.head())
# print(df.info())

#check various attributes like shape (rows and cols), datatyoes

# print(df.shape)
# print(df.dtypes)
# print(df.describe())

# Observations -----------------------------------
    #- TotalCharges -> object (should have been numerical value)
    #- Senior Citizeen -> categorical attribute in 0s and 1s no need of its mean , median , mode.
    #- Tenure - There is not much difference between mean and median therefore there are less outliers. 75% customers have tenure less than 55 months.
    #- Monthly Charges - Avg monthly charges are 64.76 whereas 25% customers pay more than usd 89.95 per month

# ----------------------------------------------------

# print(df['Churn'].value_counts()/len(df)*100)
# df['Churn'].value_counts().plot(kind ='barh', figsize=(8,6))
# plt.xlabel('Count',labelpad=14)
# plt.ylabel('Target Variable',labelpad=14)
# plt.title('Count of TARGET VARIABLE per category', y=1.02)
# plt.show()

# Observations -----------------------------------
    #- 26.5% of people havec hurned.
    #- Data is highly imbalanced.

# ----------------------------------------------------

# Finding %age of missing values
# missing = (df.isnull().sum() * 100 / df.shape[0]).reset_index()
# missing.columns = ['Feature', 'MissingPercent']

# plt.figure(figsize=(16, 5))
# ax = sns.pointplot(x='Feature', y='MissingPercent', data=missing)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # rotate for readability
# plt.show()

# Observations -----------------------------------

    #- We dont have any missing data.
    
    # General Thumb Rules:
        # - for features with less misssing values - can use regression to predict the missing values or fill the mean of the values present , depending on the feature.
        # - for features with very high number of missing values - it is better to drop those columns as they give very less insight on analysis.
        # - No thumb rule, decisions have to be atken wisely

# ----------------------------------------------------

######################################################






# DATA CLEANING ########################################

#-------create a copy of base data for manipulation and processing
new_df = df.copy()

#------Total charges should be numric amount. Lets convert it to numerical data type
new_df.TotalCharges = pd.to_numeric(new_df.TotalCharges,errors='coerce')
# print(new_df.isnull().sum())
#TotalCharges        11 null values

#-----how to handle null values ->
    # impute them with mean,median ,mode
    # del them if %age is very less like null value % in total charges =  0.15%

new_df.dropna(how='any',inplace=True)

#-----feature binning - divide customers into bins based on tenures. for eg. tenure < 12 months
#get max tenure
# print(new_df['tenure'].max()) #72

labels = ["{0} - {1}".format(i,i+11) for i in range(1,72,12)]
# print (labels)
new_df['tenure_group'] = pd.cut(new_df.tenure , range(1,80,12),right=False,labels = labels)
# print(new_df['tenure_group'].value_counts())

#-------remove columns not required for processing
new_df.drop(columns=['customerID','tenure'],axis=1,inplace=True)

#######################################################


# UNIVARIATE ANALYSIS #################################

# for i, predictor in enumerate(new_df.drop(columns=['Churn','TotalCharges','MonthlyCharges'])):
#     plt.figure(i)
#     sns.countplot(data=new_df,x=predictor,hue='Churn')

    # plt.show()

# Observations ---------------------------------------
    # 1. Gender - Male Churn % = Female Churn % = original Churn Rate (26%)
    # 2.  Senior Citizen - 
        # - 22% of not senior citizen are churning.
        # - 40% of senior citizen churn.
    # 3. People who dont have any partner are more likely to churn.
    # 4.Contract - 41% of people in month to month contract churn.
        # - Churn %age in Yearly - 13%
        # - Churn %age in Two Year - 5%




# Insights - Senior Citizens are more likely to churn.
            #  People who dont have any partner are more likely to churn.
            # Monthly contracts are more likely to churn.
            #People who pay via electronic cheque are more likely to churn.(45%)
# ------------------------------------------------------

# BIVARIATE ANALYSIS (NUMERICAL)######################

# 1. dividing the data into people who are active and people who have churned

new_df_target0 = new_df[new_df["Churn"]=="No"]
new_df_target1 = new_df[new_df["Churn"]=="Yes"]

# print(pd.crosstab(new_df.PaymentMethod, new_df.Churn))

# 2. convert target variable into binary numerical variables Yes=1, No=0

new_df['Churn']= np.where(new_df.Churn=='Yes',1,0)
# print(new_df.head())

# 3. convert all categorical variables to dummy variables

new_df_dummies = pd.get_dummies(new_df)
# print(new_df_dummies.head())

# 4. Relationship between monthly charges and total charges

# sns.lmplot(data = new_df_dummies,x ='MonthlyCharges',y='TotalCharges',fit_reg=False)
# plt.show() #positive correlation 0.65

# print(new_df_dummies['MonthlyCharges'].corr(new_df_dummies['TotalCharges']))

# INSIGHT -------------------------------------------
# total charges increase as montlhy charges increase and vice versa
# -----------------------------------------------

# 5, Churn by Montlhy charges and total charges

# mth = sns.kdeplot(new_df_dummies.MonthlyCharges[(new_df_dummies['Churn']==0)], color='Red',shade =True)
# mth = sns.kdeplot(new_df_dummies.MonthlyCharges[(new_df_dummies['Churn']==1)], color='Blue',shade =True)
# mth.legend(['No Churn','Churn'],loc ='upper right')
# mth.set_ylabel('Density')
# mth.set_xlabel('Monthly Charges')
# mth.set_title('Monthly charges By churn')
# plt.show() 

# INSIGHT ----------------------------------------------
# Churn is high when monthly charges are high and no churn is high when monthky charges are low.
# ------------------------------------------------------


# mth = sns.kdeplot(new_df_dummies.TotalCharges[(new_df_dummies['Churn']==0)], color='Red',shade =True)
# mth = sns.kdeplot(new_df_dummies.TotalCharges[(new_df_dummies['Churn']==1)], color='Blue',shade =True)
# mth.legend(['No Churn','Churn'],loc ='upper right')
# mth.set_ylabel('Density')
# mth.set_xlabel('Total Charges')
# mth.set_title('Total charges By churn')
# plt.show() 

# INSIGHT---------------------------------------------
# Astonishing - Churn is high at less total charges
# However , if we combine the insights of 3 parameters ie Tenure, MOnthly Charges & TotalCharges then the picture is bit clear. HIgher monthly charge at lower tenure results in lower total charge. Hence all three factors High Monthly Charge , Lower Tenure , and Lower Total Charge are linked to high Churn.

# 6. Build a correlation graph of all numerical variables with rspect to churn
# plt.figure(figsize=(8,10))
# new_df_dummies.corr()['Churn'].sort_values(ascending=False).plot(kind ='bar')
# plt.show()

# INSIGHTS-----------------------------------------------
# 1. Monthly contractors are more likely to churn.
# 2. People who dont have online security are high churners.
# 3. Tech Supporrt No , first year of subscription - High Chunures
# 4. Tenure (1-12) - high churners (new customers)
# 5. Fiber Optices - more likely to churn
# 6. ELctronic check - more likely to churn

# 7. Long Contrat 2 yrs , Subscription without internt servcie- nO churners
# 8. tenure (61-72) (5+years) - no churners
# 9. Factors like Gender , Avaliability of pHone Service have almost nno impact on churn
# --------------------------------------------------------

# plt.figure(figsize=(12,12))
# sns.heatmap(new_df_dummies.corr(),cmap='Paired')
# plt.show()

#####################################################

###### BIVARIATE ANALYSIS ###########################

# print(len(new_df_target0)) #Non Churners
# print (len(new_df_target1)) #Churners

def uniplot(df,col,title,hue='None'):
    sns.set_style('whitegrid')
    sns.set_context('talk')
    plt.rcParams['axes.labelsize']=20
    plt.rcParams['axes.titlesize']=22
    plt.rcParams['axes.titlepad']=30

    temp = pd.Series(data = hue)
    fig, ax = plt.subplots()
    width = len(df[col].unique()) + 2*len(temp.unique())
    fig.set_size_inches(width,8)
    plt.xticks(rotation =45)
    plt.yscale('log')
    plt.title(title)
    ax = sns.countplot (data =df, x = col , order=df[col].value_counts().index,hue=hue, palette='bright')

    plt.show()

#Partner vs Gender Graph
# uniplot(new_df_target1,col='Partner',title ='Distribution of Gender for Churned Customers',hue='gender')

#INSIHTS------------------------------------------
# Female and no partners are more churners. (more specfic)
# --------------------------------------------------

uniplot(new_df_target1,col='PaymentMethod',title ='Distribution of Payment Method & Gender for Churned Customers',hue='gender')

# INSIGHT-----------------------------------------------
# 4.1 Female who are paying via credit cards are more likely to churn.
# ------------------------------------------------------

# do for contract , tech support etc