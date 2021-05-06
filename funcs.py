from random import randint
from numpy import prod
import sys
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
			f.flush()
			f.seek(0)
			f.write(data)
	except Exception as e: 
		print(e)    
		exit(6)
def gcd(a, b):
	while (a != 0) and (b != 0):
	    if a > b:
	        a %= b
	    else:
	        b %= a
	gcd = a + b
	return True if gcd == 1 else False

def power(a, k, m):
	r = 1
	a = a % m 
	while(k > 0):
		if(k % 2 == 1):
			r = (r * a) % m
		a = a * a % m
		k = k // 2
	return r

def inv(a, b):
	U = (a, 1, 0)
	V = (b, 0, 1)
	q = U[0]//V[0]
	T = (U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2])
	while (V[0]!=0):
		q = U[0]//V[0]
		T = (U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2])
		U = V
		V = T
	if(U[2]<0):
		return U[2]+a
	else:
		return U[2]

def simple_check(a):
	for i in range(2, a//2 + 2):
		if a%i == 0:
			return False
	return True