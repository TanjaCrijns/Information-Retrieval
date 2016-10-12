__author__      = "Tanja Crijns"
import pandas as pd, numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse

if __name__ == "__main__":
    df = pd.read_csv("D:/Users/Tanja/Documents/Master/Information retrieval/Assignment2/Querylog.csv", sep=';')
    queries = df['Query']
    urls = df['Clicked link']
    uniqueQueries = queries.value_counts()
    uniqueURLs = urls.value_counts()

    # Number of unique queries
    print "Unique queries = " + str(len(uniqueQueries))

    # Top 10 most frequent queries
    topTenQueries = uniqueQueries[:10]
    print "Most frequent queries = \n" + str(topTenQueries)

    # Top 10 most clicked URLs
    uniqueURLs = uniqueURLs.drop("\N")
    topTenURLs = uniqueURLs[0:10]
    print "Most frequent URLs = \n" + str(topTenURLs)

    # Vector space representation
    URLsTopQueries = df[df.Query.isin(topTenQueries.index)]['Clicked link']
    URLsTopQueries = URLsTopQueries[URLsTopQueries != '\N']
    vectorSpace = np.zeros(shape=(len(topTenQueries),len(URLsTopQueries)))
    logs = df[df.Query.isin(topTenQueries.index)]
    logs = logs[logs['Clicked link'] != '\N']
    queriestmp = topTenQueries.index.tolist()
    URLstmp = URLsTopQueries.values.tolist()

    # Making the matrix
    for index, log in logs.iterrows():
        vectorSpace[queriestmp.index(log['Query'])][URLstmp.index(log['Clicked link'])] += 1

    # Cosine calculation
    vectorSpace_sparse = sparse.csr_matrix(vectorSpace)
    np.set_printoptions(suppress=True)
    similarities = cosine_similarity(vectorSpace_sparse)
    print similarities.round(decimals=2)








