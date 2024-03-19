# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Load the dataset
# Assuming the dataset is already downloaded and saved as 'stock_data.csv'
stock_data = pd.read_csv('stock_data.csv')

# Data preprocessing
# Handling missing values
stock_data.dropna(inplace=True)

stock_data.drop(['Date'], axis=1,inplace=True)


# Calculating mean returns and variances
daily_returns = stock_data.pct_change()
annual_mean_returns = daily_returns.mean()*252
annual_return_variance = daily_returns.var()*252

#Create new dataframe
df = pd.DataFrame(stock_data.columns, columns=['Stock_Symbols'])
df['Variances'] = annual_return_variance.values
df['Returns'] = annual_mean_returns.values


# Applying Elbow Method to determine the number of clusters

#Get and store the annual returns and the annual variances
X = df[['Returns','Variances']].values

# Determining the optimal number of clusters using the elbow method
inertia = []
for k in range(2, 8):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Plotting the elbow graph
plt.plot(range(2, 8), inertia)
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Within-cluster Sum of Squares (Inertia)')
plt.show()

#Applying K-Means Clustering

# Based on the elbow graph, select the optimal number of clusters
#Choose the number of clusters based on the graph and uncomment the below line

#optimal_k = 4  

# Applying K-Means with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_k)
kmeans.fit(X)
cluster_labels = kmeans.labels_
df['Cluster_Labels'] = cluster_labels

# Visualizing clusters
plt.scatter(X[:,0], X[:,1], c=cluster_labels, cmap='rainbow')
plt.title('K-Means Clustering Plot')
plt.xlabel('Returns')
plt.ylabel('Variances')
plt.show()

#Create a function to build a diversed portfolio by heuristic approach

def diversified_portfolio():
    for i in range(0,4):
        symbol = df[df['Cluster_Labels'] == i].head(1)
        print(symbol[['Stock_Symbols','Cluster_Labels']])

# Printing the diversified portfolio
print("Diversified Portfolio:")
print(diversified_portfolio())

#set LOKY_MAX_CPU_COUNT = 3  ---> <number_of_cores> This is to ensure optimal running of the code.
