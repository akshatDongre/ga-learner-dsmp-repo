# --------------
# import packages

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 



# Load Offers
offers = pd.read_excel(path, sheet_name=0)
transactions=pd.read_excel(path, sheet_name=1)
transactions['n']=1
df=pd.merge(offers, transactions)
print(df.head())

# Load Transactions


# Merge dataframes


# Look at the first 5 rows



# --------------
# Code starts here
matrix= pd.pivot_table(df,index='Customer Last Name', columns='Offer #', values='n')

matrix.fillna(0, inplace=True)
matrix.reset_index(inplace=True)
print(matrix.head(5))
# create pivot table


# replace missing values with 0


# reindex pivot table


# display first 5 rows


# Code ends here


# --------------
# import packages
from sklearn.cluster import KMeans

# Code starts here
cluster = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
matrix['cluster']=cluster.fit_predict(matrix[matrix.columns[1:]])
print(matrix.head())
# initialize KMeans object


# create 'cluster' column


# Code ends here


# --------------
# import packages
from sklearn.decomposition import PCA

# Code starts here
pca = PCA(n_components=2, random_state=0)
matrix['x']=pca.fit_transform(matrix[matrix.columns[1:]])[:,0]
matrix['y']=pca.fit_transform(matrix[matrix.columns[1:]])[:,1]
clusters =matrix.iloc[:,[0,33,34,35]]
clusters.plot.scatter(x='x',y='y',c='cluster',colormap='viridis')
# initialize pca object with 2 components


# create 'x' and 'y' columns donoting observation locations in decomposed form


# dataframe to visualize clusters by customer names


# visualize clusters


# Code ends here


# --------------
# Code starts here
data = clusters.merge(transactions)

data = offers.merge(data)
data.head()

champagne = {} 
for i in range(0,5):
    champagne[i]=0
    new_df =data[data['cluster']==i]
    counts = new_df['Varietal'].value_counts(ascending=False)
    # check if 'Champagne' is ordered mostly
    print(i)
    print(counts.index[0])
    if (counts.index[0]=='Champagne'):
        champagne[i]=counts[0]
        # add it to 'champagne'
print(champagne)
cluster_champagne= max(champagne, key=lambda k: champagne[k])
print(cluster_champagne)
# merge 'clusters' and 'transactions'


# merge `data` and `offers`

# initialzie empty dictionary


# iterate over every cluster

    # observation falls in that cluster

    # sort cluster according to type of 'Varietal'

    # check if 'Champagne' is ordered mostly

        # add it to 'champagne'


# get cluster with maximum orders of 'Champagne' 


# print out cluster number




# --------------
# Code starts here
discount={}

# iterate over cluster numbers
for i in range(0,5):
    # dataframe for every cluster
    new_df=data[data['cluster']==i]
    # average discount for cluster
    print(new_df['Discount (%)'].sum()/len(new_df))
    counts=new_df['Discount (%)'].sum()/len(new_df)
    # adding cluster number as key and average discount as value 
    discount[i]=counts



# cluster with maximum average discount
cluster_discount=max(discount, key=lambda k: discount[k])
print(cluster_discount)

# Code ends here


