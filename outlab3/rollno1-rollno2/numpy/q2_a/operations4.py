import numpy as np

parser = argparse.ArgumentParser(description='Prints list of unique elements of array')
parser.add_argument('-p','--path', required=True, help='Relatve path to the csv file')
args = parser.parse_args()

csv = np.genfromtxt(args.path,delimiter=',')
mat = np.round(csv).astype(int)
rows, cols = mat.shape
#print(mat)

#Operations4.py
flat = np.sort(mat, axis=None) 
uniq, freq = np.unique(flat, return_counts = True)
print(uniq)
print(freq)
count = np.bincount(flat)[uniq[-2]]
print(count)

