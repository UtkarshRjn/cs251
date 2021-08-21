import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Padds the matrix')
parser.add_argument('-p','--path', required=True, help='Relatve path to the csv file')
parser.add_argument('-n','--num', required=True, help='Number for input')
args = parser.parse_args()

csv = np.genfromtxt(args.path,delimiter=',')
mat = np.round(csv).astype(int)
rows, cols = mat.shape
#print(mat)

#Operations5.py
x = int(args.num)
pd = np.pad(mat, (x,x), 'constant', constant_values=(0,0))
print(pd)
