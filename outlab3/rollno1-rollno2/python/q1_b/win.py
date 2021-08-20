import os
import argparse

parser = argparse.ArgumentParser(description='Find winners')
parser.add_argument('-p1','--path1', required=True, help='Relatve path to web_list.txt')
parser.add_argument('-p2','--path2', required=True, help='Relatve path to uid_list.txt')
parser.add_argument('-o','--output', required=True, help='Relatve path to the outputdir')
args = parser.parse_args()

def print_webList(path1):
	for e in open(path1).read().split():
		print(e.split('/')[2])

def complete(url):
	if url.split('.')[0] == 'www':
		url = 'https://' + url
	elif url.split('.')[0] == 'http://www':
		url.replace('http','https')
	elif url.split('.')[0] != 'https://www':
		url = 'https://www.' + url 
	return url

def print_winners(path1,path2,output):
	count = 0
	with open(os.path.join(output,'winner.txt'),"w") as f:
		for e in open(path2).read().split("\n")[:-1]:
			user_name,_,ip_address,url = e.split('||')[:4]
			url_complete = complete(url)
			if url_complete in open(path1).read().split():
				print(f"user_name - {user_name} : Winner - Lucky draw!!! - {url_complete}")
				f.write(f"{user_name}||{ip_address}||{url_complete}\n")
				count +=1
	f.close()
	print(count)

if __name__ == '__main__':
	print_webList(args.path1)
	print_winners(args.path1,args.path2,args.output)