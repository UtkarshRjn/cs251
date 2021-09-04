import os
import argparse

parser = argparse.ArgumentParser(description='Rank countries by their olympic medals')
parser.add_argument('-p','--path', required=True, help='Relatve path to the test case folder')
args = parser.parse_args()

def read(path):
	Dict = {}
	for (root,dirs,files) in os.walk(path):
		for file in files:
			myfile = open(os.path.join(path,file),"r")
			for country in myfile.read().split():
				if country.split("-")[0] in Dict.keys():
					temp = [int(country.split("-")[1]),int(country.split("-")[2]),int(country.split("-")[3])]
					Dict[country.split("-")[0]] = [sum(x) for x in zip(Dict[country.split("-")[0]],temp)]
				else:
					Dict[country.split("-")[0]] = [int(country.split("-")[1]),int(country.split("-")[2]),int(country.split("-")[3])]
			myfile.close()
	
	return Dict

def sort(Dict):
	return dict(sorted(Dict.items(), key=lambda e: (-e[1][0],e[0])))

if __name__ == '__main__':
	country = read(args.path)
	sorted_country = sort(country)
	print(sorted_country)
