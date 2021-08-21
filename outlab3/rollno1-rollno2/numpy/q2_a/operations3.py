import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Sorts and flattens array')
parser.add_argument('-p','--path', required=True, help='Relatve path to the csv file')
args = parser.parse_args()

csv = np.genfromtxt(args.path,delimiter=',')
mat = np.round(csv).astype(int)
rows, cols = mat.shape
#print(mat)

#Operations3.py
xaxis_sort = np.sort(mat, axis=0)
print(xaxis_sort)
yaxis_sort = np.sort(mat, axis=1)
print(yaxis_sort)
flat = np.sort(mat, axis=None) 
print(flat)
