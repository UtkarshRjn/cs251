import numpy as np

parser = argparse.ArgumentParser(description='Prints elements belonging to the upper diagonals')
parser.add_argument('-p','--path', required=True, help='Relatve path to the csv file')
args = parser.parse_args()

csv = np.genfromtxt(args.path,delimiter=',')
mat = np.round(csv).astype(int)
rows, cols = mat.shape
#print(mat)

#Operations1.py 
for i in range(0,rows):
    for j in range(0,cols):
        if(j>i): 
            print("\n")
            break
        else: print(mat[j,i], end = " ")
print("\n")


