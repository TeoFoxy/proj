from random import randint
from numpy import prod
from funcs import *
import sys

def decode(file_in, file_out, e, n):
	with open(file_in, 'rb') as f:
		a = bytearray(f.read())
	l = ((len(bin(n)[2:]) + 7) >> 3)
	data = (a[i:i+l] for i in range(0, len(a), l))
	decr = b''
	for block in data:
		c = int.from_bytes(block, 'little')
		decr += (power(c, e, n).to_bytes(l+1, 'little')[:l-1])
	with open(file_out, 'wb') as f:
		f.write(decr.rstrip(b'\x00'))

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

p_l = 20
q_l = 8
p, q = gen(p_l, q_l)
n = p*q
f = (p-1)*(q-1)
print(f'p={p}\nq={q}\nn = {n}\nf = {f}\n')
e = 0
while True:
	e = randint(1, f)
	if gcd(e, f):
		d = inv(f, e)
		if (d < e):
			break

while True:
	sw=input('1.Записать N и e в файл\n2.Расшифровать файл\n')
	if (sw == '1'):
		with open(sys.argv[1],'w') as f:
			f.write(str([n, e]))
	if (sw == '2'):
		decode(sys.argv[2], sys.argv[3], d, n)