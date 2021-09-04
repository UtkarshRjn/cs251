import numpy as np
import pandas as pd
import os
from numpy import linalg as LA
import matplotlib.pyplot as plt
import argparse
import matplotlib

matplotlib.use('Agg')

parser = argparse.ArgumentParser(description='pca')
parser.add_argument('-p','--path', required=True, help='Relatve path to the txt file')
parser.add_argument('-o','--output', required=True, help='Relatve path to the output dir')
args = parser.parse_args()

entries = pd.read_csv(args.path, sep=",", header=None)
rows, cols = entries.shape
X = (entries - np.mean(entries))
cov_matrix = np.cov(X.T)
eigenvalues,eigen_matrix = LA.eig(cov_matrix)
eigenvalues[::-1].sort()
print(eigenvalues)
K=2
eigenvector_matrix=np.delete(eigen_matrix, slice(K,cols), 1)

transformed_matrix=np.dot(X,eigenvector_matrix)
# print(transformed_matrix)

np.savetxt(os.path.join(args.output,"transform.csv"),transformed_matrix)
plt.scatter(transformed_matrix[:,0], transformed_matrix[:,1])
plt.xlim([-15, 15])
plt.ylim([-15, 15])

plt.savefig(os.path.join(args.output,'out.png'))
