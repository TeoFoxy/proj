import sys
from random import *
def read_file(file_in): 
	try: 
		with open(file_in, "rb") as f: 
			return f.read() 
	except Exception as e: 
		print(e) 
		exit(5)

def write_file(file_out, data): 
	try: 
		with open(file_out, "wb") as f: 
			f.write(data)
	except Exception as e: 
		print(e) 
		exit(6)
		
def power(a,k,m):
	ans=1
	a%=m
	while(k>0):
		if(k%2==1):
			ans=(ans*a)%m
		a=(a*a)%m
		k=k//2
	return ans

while True:
	sw = input('1.Записать y2 в файл\n2.Расшифровать\n')
	if (sw == '1'):
		with open(sys.argv[1], 'r') as f:
			k = f.read()
		p = int(k.split(',')[0].split('[')[-1])
		g = int(k.split(',')[1])
		y1 = int(k.split(',')[2].split(']')[0])
		print(f'p = {p}\ng = {g}\ny1 = {y1}\n')
		x2 = randint(20000, 4000000)
		y2 = power(g, x2, p)
		with open(sys.argv[2], 'w') as f:
			f.write(str(y2))
		z2 = power(y1, x2, p)
		print(z2)	
	else:
		a = bytearray(read_file(sys.argv[3]))
		res = bytearray()
		for i in a:
			res.append(i ^ z2%256)
		write_file(sys.argv[4], res)
		print('3 file: ', res.decode('utf-8'))
		break



