import sys
from my_funcs import *
from random import randint
import pickle

def hash(file_in):
	hash_ = []
	with open(file_in, 'rb') as f:
		a = bytearray(f.read())
	if len(a)%2 == 1:
		a.append(1)
	for i in range(0, len(a)-1, 2):
		try:
			s=a[i]^a[i+1]
			s=str(s)
			s=s.encode()
			hash_.append(int.from_bytes(s, 'little'))
		except Exception as e:
			pass
	h=sum(hash_)
	f = h & 0b1111111111111111
	print(f'Ваш хэш: {f}')
	return f


def gen(np, nq):
	ap = 2**(np-1)
	bp = 2**np
	aq = 2**(nq-1)
	bq = 2**nq
	while True:
		p = randint(ap, bp-1)
		if simple_check(p):
				break
	while True:
		q = randint(aq, bq-1)
		if simple_check(q):
				break
	return p, q

def gen_n(p_l, q_l):
	while True:
		p, q = gen(p_l, q_l)	
		Na = p*q
		if len(bin(Na)[2:]) == 16:
				break
	return Na, (p-1)*(q-1)

def gen_n_e_d():
	p_l = 8 
	q_l = 8
	Na, f = gen_n(p_l, q_l)
	print('na =', Na)
	ea = 0
	while True:
		ea = randint(1, f)
		if gcd(ea, f):
			d = inv(f, ea)
			if (d < ea):
				break
	return Na, ea, d

def eds(h, d1, n1, e2, n2):
	m = [i for i in h.to_bytes(3, 'little')]
	c = [power(i, d1, n1) for i in m]
	g = []
	for i in c:
		i = [power(j, e2, n2) for j in i.to_bytes(3, 'little')]
		g.append(i)
	print('Отправляется клиенту g = ', g)
	print('эцп для а: c = ', c)
	return g

# while True:
# 	Na,ea,d=gen_n_e_d()
# 	sw = input('1.Принять открытые ключи\n2.Запись g в файл\n3.Запись открытых ключей в файл')
# 	if (sw == '1'):
# 		with open(sys.argv[1],'r') as f:
# 			re=f.read()
# 			Nb=int(re.split(',')[0].split('[')[-1])
# 			eb=int(re.split(',')[1].split(']')[0])
# 			print(f'n= {Nb}\ne={eb}\n')
# 		h=hash(sys.argv[2])
# 		g=eds(h, d, Na, eb, Nb)
# 		print(g)
# 	if (sw == '2'):
# 		with open(sys.argv[3],'w') as f:
# 			f.write(str(g))
# 	if (sw == '3'):
# 		with open(sys.argv[4],'w') as f:
# 			f.write(str([Na, ea]))
Na,ea,d=gen_n_e_d()
while True:
	#1 - хэш
	#2 - записываем na и ea в файл
	#3 - ссчитываем nb eb из файла
	#4 - файл для g
	sw = input('1.Запись открытых ключей в файл для Боба\n2.Принять ключи Боба и записать g в файл\n')
	if (sw == '1'):
		with open('C:/Users/Юрий/Downloads/wed/Alice_keys.txt','w') as f:
			f.write(f'{Na}, {ea}')
	if (sw == '2'):
		with open('C:/Users/Юрий/Downloads/wed/Bob_keys.txt', 'r') as f:
			Nb, eb = f.read().split(', ')
			Nb, eb = [int(Nb), int(eb)]
		h=hash('C:/Users/Юрий/Downloads/wed/1.txt')
		g=eds(h, d, Na, eb, Nb)
		with open('C:/Users/Юрий/Downloads/wed/g_for_eds.txt','wb') as f:
			pickle.dump(g, f)