from random import randint
import sys, os
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

def gen(n):
	while True:
		while True:
			q=randint(2**(n-2), 2**(n-1)-1)
			if prost(q):
				break
		p=2*q+1
		if prost(p):
			break
	g=3
	while True:
		g=randint(1,p-1)
		if (power(g,q,p)!=1):
			break
	x1=randint(5000,50000000)
	y1=power(g,x1,p)
	return p,g,y1, x1

def power(a,k,m):
	ans=1
	a%=m
	while(k>0):
		if(k%2==1):
			ans=(ans*a)%m
		a=(a*a)%m
		k=k//2
	return ans

def prost(n):
	for i in range(2,n//2+2):
		if n%i==0:
			return False
	return True

p, g, y1, x1 = gen(17)
print("g = ",g)
print("p = ",p,"\nlen p = ", len(bin(p)[2:]))
print("y1 = ",y1)
gamma = 0
while True:
	sw = input('1.Записать p, g, y1 в файл\n2.Принять y2\n3. Зашифровать\n')
	if(sw == '1'):
		with open(sys.argv[1], 'w') as f:
			f.write(str([p, g, y1]))
	elif sw == '2':
		with open(sys.argv[2], 'r') as f:
			y2 = int(f.read())
		z1 = power(y2, x1, p)
		gamma = z1
		print(z1)
	else:
		a = bytearray(read_file(sys.argv[3]))
		res = bytearray()
		print('1 file:\n', a.decode('utf-8'))
		for i in a:
			res.append(i ^ z1%256)
		write_file(sys.argv[4], res)
		print('2 file:\n', res.decode('ISO-8859-1'))
		break

