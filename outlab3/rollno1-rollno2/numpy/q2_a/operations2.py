import numpy as np

parser = argparse.ArgumentParser(description='Prints mean, median, std deviation, determinant and inverse')
parser.add_argument('-p','--path', required=True, help='Relatve path to the csv file')
args = parser.parse_args()

csv = np.genfromtxt(args.path,delimiter=',')
mat = np.round(csv).astype(int)
rows, cols = mat.shape
#print(mat)

#Operations2.py
mean = np.mean(mat, axis=0)
print(mean)
median = np.median(mat, axis=0)
print(median)
deviat = np.std(mat, axis=0)
deviat_2 = np.around(deviat, decimals=2)
print(deviat_2)
determinant = np.linalg.det(mat)
print(determinant)
if(determinant!=0):
    inv = np.linalg.inv(mat)
    inverse_2 = np.around(inv, decimals=2)
    print(inverse_2)
else:
    pseudo = np.linalg.pinv(mat)
    pseudo_inv_2 = np.around(pseudo, decimals=2)
    print(pseudo_inv_2)


