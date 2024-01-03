import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

#import csv
df = pd.read_csv('/Users/owenaspen/Documents/School/WGU/D206/D206_clean_Aspen.csv')

print(df.info())

df_cont = df[['Income','Outage_sec_perweek','Tenure','MonthlyCharge','Bandwidth_GB_Year']]
#normalize data
df_cont_normalized = (df_cont-df_cont.mean())/df_cont.std()
#find number of principle components
pca = PCA(n_components=df_cont.shape[1])
print(pca)

pca.fit(df_cont_normalized)

df_pca = pd.DataFrame(pca.transform(df_cont_normalized),columns=['PC1','PC2','PC3','PC4','PC5'])

loadings = pd.DataFrame(pca.components_.T,columns=['PC1','PC2','PC3','PC4','PC5'],index=df_cont.columns)
print(loadings)

cov_matrix = np.dot(df_cont_normalized.T, df_cont_normalized)/df_cont.shape[0]

eigenvalues = [np.dot(eigenvector.T, np.dot(cov_matrix, eigenvector)) for eigenvector in pca.components_]

plt.plot(eigenvalues)
plt.xlabel('number of components')
plt.ylabel('eigenvalue')
plt.axhline(y=1, color='red')
plt.show()