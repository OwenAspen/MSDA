#import packages
import pandas as pd
from scipy import stats

#import data with index_col set to CaseOrder so that a column isn't added to the data
df = pd.read_csv('/Users/owenaspen/Documents/School/WGU/D207/d9rkejv84kd9rk30fi2l/churn_clean.csv', index_col='CaseOrder')

#Separating the types of payment methods into their own lists containing the tenure for each customer
credit_card = df[df.PaymentMethod == 'Credit Card (automatic)'].Tenure
bank_transfer = df[df.PaymentMethod == 'Bank Transfer(automatic)'].Tenure
mailed_check = df[df.PaymentMethod == 'Mailed Check'].Tenure
electronic_check = df[df.PaymentMethod == 'Electronic Check'].Tenure

#Performing an ANOVA test on our 4 different sets of payment types tenures
anova = stats.f_oneway(credit_card, bank_transfer, mailed_check, electronic_check)
#Displaying the result
print(anova)

