from random import randint
from numpy import prod
from funcs import *
import sys

def code(file_in, file_out, e, n):
	with open(file_in, 'rb') as f:
		a = bytearray(f.read())
	l = ((len(bin(n)[2:]) + 7) >> 3) - 1
	print(l)
	data = (a[i:i+l] for i in range(0, len(a), l))
	en = bytearray()
	for block in data:
		c = int.from_bytes(block, 'little')
		en += (power(c, e, n).to_bytes(l+1, 'little'))
	with open(file_out, 'wb') as f:
		f.write(en)

while True:
	sw=input('1.Принять N и e\n2.Зашифровать файл\n')
	if (sw == '1'):
		with open(sys.argv[1],'r') as f:
			re=f.read()
			n=int(re.split(',')[0].split('[')[-1])
			e=int(re.split(',')[1].split(']')[0])
			print(f'n= {n}\ne={e}\n')
	if (sw == '2'):
		code(sys.argv[2], sys.argv[3], e, n)
		
