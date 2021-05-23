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
		Nb = p*q
		if len(bin(Nb)[2:]) == 16:
				break
	return Nb, (p-1)*(q-1)

def gen_n_e_d():
	p_l = 8 
	q_l = 8
	Nb, f = gen_n(p_l, q_l)
	print('Nb =', Nb)
	eb = 0
	while True:
		eb = randint(1, f)
		if gcd(eb, f):
			d = inv(f, eb)
			if (d < eb):
				break
	return Nb, eb, d

def eds(g, d2, n2, e1, n1):
	try:
		c = []
		err="Err"
		for i in g:
			c.append([power(j, d2, n2) for j in i])
		print('эцп для b: c = ', [(int.from_bytes(i, 'little')) for i in c])
		m = [power(int.from_bytes(i, 'little'), e1, n1) for i in c]
		print('Полученный хэш на клиенте:', [int.from_bytes(m, "little")])
		return int.from_bytes(m, 'little')
	except Exception as e1:
		return err

# while True:
# 	Nb,eb,d=gen_n_e_d()
# 	sw = input('1.Принять открытые ключи\n2.Запись открытых ключей в файл\n3.Проверка ЭЦП\n')
# 	if (sw == '1'):
# 		with open(sys.argv[1],'r') as f:
# 			re=f.read()
# 			Na=int(re.split(',')[0].split('[')[-1])
# 			ea=int(re.split(',')[1].split(']')[0])
# 			print(f'n= {Na}\ne={ea}\n')

# 	if (sw == '2'):
# 		with open(sys.argv[2],'w') as f:
# 			f.write(str([Nb, eb]))
# 	if (sw == '3'):
# 		with open(sys.argv[3],'r') as f:
# 			re=f.read()
# 			g=int(re.split('[')[-1].split(']')[0])
# 		if eds(g,d,Nb,eb,Nb)==hash(sys.argv[4]):
# 			print('ЭЦП подтверждена')
Nb,eb,d=gen_n_e_d()
while True:
	#1 - хэш
	#2 - записываем nb и eb в файл
	#3 - ссчитываем na ea из файла
	#4 - файл для g
	sw = input('1.Запись открытых ключей в файл для Алисы\n2.Принять открытые ключи и g от Алисы\nф')
	if (sw == '1'):
		with open('C:/Users/Юрий/Downloads/wed/Bob_keys.txt','w') as f:
			f.write(f'{Nb}, {eb}')
	if (sw == '2'):
		with open('C:/Users/Юрий/Downloads/wed/Alice_keys.txt', 'r') as f:
			Na, ea = f.read().split(', ')
			Na, ea = [int(Na), int(ea)]
		with open('C:/Users/Юрий/Downloads/wed/g_for_eds.txt', 'rb') as f:
			g = pickle.load(f)
		print(g)
		q=eds(g,d,Nb,ea,Na)
		if q!="Err":
			if q==hash('C:/Users/Юрий/Downloads/wed/1.txt'):
				print('ЭЦП подтверждена')
			else:
				print('ЭЦП не подтверждена')
		else:
			q=eds(g,d,Nb,ea,Na)
			if q==hash('C:/Users/Юрий/Downloads/wed/1.txt'):
				print('ЭЦП подтверждена')
