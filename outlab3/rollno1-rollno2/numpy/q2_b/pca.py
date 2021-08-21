import numpy as np
import pandas as pd 
from numpy import linalg as LA
import matplotlib.pyplot as plt

data = open(path,'r')
entries = list(map(int, data.read().split()))
X = np.array(entries).reshape(R, C)
X= (X- np.mean(X, axis=0)) / np.std(X, axis=0)
covariance_matrix=np.cov(X)
eigenvalues, eigenvector_matrix = LA.eig(covariance_matrix)
eigenvalue.sort()
print(eigenvalues)
K=2
eigenvector_matrix=np.delete(eigenvector_matrix, [K:], 1)
transformed_matrix=np.dot(X,eigenvector_matrix)
#pd.DataFrame(transformed_matrix).to_csv(‘output/transform.csv’)
plt.scatter(x, y, c ="blue")
plt.plot(range(15))
plt.xlim(-15, 15)
plt.ylim(-15, 15)