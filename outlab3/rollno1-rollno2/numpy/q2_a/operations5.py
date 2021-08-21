import numpy as np

parser = argparse.ArgumentParser(description='Padds the matrix')
parser.add_argument('-p','--path', required=True, help='Relatve path to the csv file')
args = parser.parse_args()

csv = np.genfromtxt(args.path,delimiter=',')
mat = np.round(csv).astype(int)
rows, cols = mat.shape
#print(mat)

#Operations5.py
x = int(input())
pd = np.pad(mat, (x,x), 'constant', constant_values=(0,0))
print(pd)
