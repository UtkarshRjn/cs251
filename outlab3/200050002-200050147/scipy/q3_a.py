import argparse
from scipy import integrate

parser = argparse.ArgumentParser(description='Limits of an intergal')
parser.add_argument('x1', type=float , help='Lower limit of x')
parser.add_argument('x2', type=float , help='Upper limit of x')
parser.add_argument('y1', type=float , help='Lower limit of y')
parser.add_argument('y2', type=float , help='Upper limit of y')
parser.add_argument('z1', type=float , help='Lower limit of z')
parser.add_argument('z2', type=float , help='Upper limit of z')
args = parser.parse_args()

f = lambda x,y,z : (x**2)*(y**2)*(z**2)
print(integrate.tplquad(f, args.x1, args.x2, lambda x: args.y1, lambda x:\
						args.y2, lambda x,y: args.z1, lambda x,y: args.z2)[0])
