#import packages
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

#import data
df = pd.read_csv('/Users/owenaspen/Documents/School/WGU/D206/d206-churn.dictionary.files/churn_raw_data.csv')

#inspecting data
print(df.info())

#detecting duplicate values (Middleton, n.d. Detecting and Treating Duplicates)
print(df.duplicated().value_counts())

#detecting null values (Middleton, n.d. Detecting and Treating Missing Values)
print(df.isnull().sum())

#detecting outliers (Middleton, n.d. Detecting and Treating Outliers)
#I manually cycled through columns (I.E. replaced 'Population' with 'Children') to generate each plot
boxplot = sb.boxplot(x='Population', data=df)
#I used this code (again cycling through columns) to get an idea of how many outliers are present for each column.
outlier_count = df.query('Population > 31000')
print(outlier_count.info())

#treating detected issues
#missing values (Middleton, n.d. Detecting and Treating Missing Values)
#generating before imputation histograms (cycled through columns to create all graphs)
plt.hist(df['Children'])
plt.show
#imputing missing values with the mean, median, or mode depending on distribution and variable type
df['Children'].fillna(df['Children'].median(), inplace=True)
df['Age'].fillna(round(df['Age'].mean()), inplace=True)
df['Techie'] = df['Techie'].fillna(df['Techie'].mode()[0])
df['Phone'] = df['Phone'].fillna(df['Phone'].mode()[0])
df['TechSupport'] = df['TechSupport'].fillna(df['TechSupport'].mode()[0])
df['Income'].fillna(df['Income'].median(), inplace=True)
df['Tenure'].fillna(df['Tenure'].median(), inplace=True)
df['Bandwidth_GB_Year'].fillna(df['Bandwidth_GB_Year'].median(), inplace=True)
#generating post imputation histogramns for compairison cycled through columns to create all graphs)
plt.hist(df['Children'])
plt.show
#Checking all missing values are filled
print(df.isnull().sum())

#outliers (Middleton, n.d. Detecting and Treating Outliers)
#I removed from the database but retained outliers for the column MonthlyCharge
outliers = df[(df['MonthlyCharge'] > 300)]
print(outliers.info())
df.drop(df[(df['MonthlyCharge'] > 300)].index, inplace=True)
print(df.info())
#Checking the box plot after removing outliers
boxplot = sb.boxplot(x='MonthlyCharge', data=df)

#saving cleaned data and excluded data to a new file
df.to_csv('/Users/owenaspen/Documents/School/WGU/D206/D206_clean_Aspen.csv')
outliers.to_csv('/Users/owenaspen/Documents/School/WGU/D206/D206_outliers_Aspen.csv')
