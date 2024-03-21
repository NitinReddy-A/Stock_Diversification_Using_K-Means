# Portfolio Diversification using K-Means Algorithm:

This project aims to diversify a stock portfolio using the K-Means clustering algorithm. By clustering stocks based on their mean returns and variances, the algorithm identifies groups of stocks with similar risk-return profiles. A diversified portfolio is then constructed by selecting representative stocks from each cluster.


## Introduction:
Stock diversification is a crucial strategy for mitigating risk in investment portfolios. This project leverages the K-Means clustering algorithm to group stocks based on their historical mean returns and variances. By clustering stocks with similar risk-return profiles, investors can construct diversified portfolios that balance risk and return.

## Dependencies:
pandas

numpy

scikit-learn

matplotlib

## Usage
Clone the repository:

    git clone https://github.com/yourusername/stock-diversification.git
Navigate to the project directory:

    cd stock-diversification
Ensure that your dataset is saved as stock_data.csv in the project directory.

Run the stock_diversification.py script:
    
    python stock_diversification.py
Follow the prompts to visualize the optimal number of clusters and view the diversified portfolio.

## Algorithm Overview:
Data Preprocessing: Load the stock dataset, handle missing values, and calculate mean returns and variances.

Elbow Method: Determine the optimal number of clusters using the elbow method, plotting the within-cluster sum of squares against the number of clusters.

K-Means Clustering: Apply K-Means clustering with the optimal number of clusters to group stocks based on their risk-return profiles.

Diversified Portfolio: Construct a diversified portfolio by selecting representative stocks from each cluster using a heuristic approach.

## Results:
After running the script, the user will visualize the elbow plot to determine the optimal number of clusters. Subsequently, the program will display a scatter plot depicting the clusters and output the diversified portfolio, consisting of representative stocks from each cluster.

