from random import randint
import sys, os
def power(a,k,m):
	ans=1
	a%=m
	while(k>0):
		if(k%2==1):
			ans=(ans*a)%m
		a=(a*a)%m
		k=k//2
	return ans
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
# def gen(n):
# 	while True:
# 		while True:
# 			q=randint(2**(n-2), 2**(n-1)-1)
# 			if prost(q):
# 				break
# 		p=2*q+1
# 		if prost(p):
# 			break
# 	g=3
# 	while True:
# 		g=randint(1,p-1)
# 		if (power(g,q,p)!=1):
# 			break
# 	x1=randint(5000,50000000)
# 	y1=power(g,x1,p)
# 	return p, g, y1

def gen_n(nn):
	ap=2**(nn-1)
	ab=2**nn
	while True:
		p=randint(ap,ab-1)
		if prost(p):
			break
	return p

def gen_e(n):
	while True:
		e=randint(n,100)
		break

# def gen_d:
# 	while True:
# 		d=inv()

def gen2(n):
	while True:
		while True:
			Nb=randint(2**(n-2), 2**(n-1)-1)
			if prost(Nb):
				break
		db=2*Nb+1
		if prost(db):
			break
	eb=randint(1000,10000000)
	return Nb, db, eb

def prost(n):
	for i in range(2,n//2+2):
		if n%i==0:
			return False
	return True

# Na, da, ea=gen1(16)

# Nb,db, eb=gen2(16)

m=13
Na=gen_n(16)
da=gen_n(16)
ea=gen_e(16)
print('m= ', m)
print('Na= ', Na)
print('da= ', da)
print('ea= ', ea)
Nb=gen_n(16)
db=gen_n(16)
eb=gen_e(16)
print('Nb= ', Na)
print('db= ', da)
print('eb= ', ea)

ca=power(m,ea,Na)
print('c= ', ca)
g=power(ca,db,Nb)
print('g= ', g)


cb=power(g,eb,Nb)
print('c=', cb)
m=power(cb,da,Na)
print('m= ', m)

