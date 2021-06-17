from random import randint
from numpy import prod
from my_funcs import *
import sys

def decode(file_in, file_out, d, n):
	# Побайтовое считывание защифрованного файла
	with open(file_in, 'rb') as f:
		a = bytearray(f.read())

	# Вычисление длины блока
	l=len(bin(n)[2:])//8+1

	# запись данных файла в блоки заданной длины
	data = (a[i:i+l] for i in range(0, len(a), l))
	decr=bytearray()
	for block in data:
		# Перевод блоков в числа, чтобы потом произвести с ними нужные вычисления
		c = int.from_bytes(block, 'little')

		# Расшифровка блоков,а затем перевод их в байты
		decr += (power(c, d, n).to_bytes(l+1, 'little')[:l-1])
	with open(file_out, 'wb') as f:
		# Запись полученных расшифрованных блоков в файл, предварительно убрав из конца ненужные биты
		f.write(decr.rstrip(b'\x00'))

p_l = 20
q_l = 8
# Генерация чисел заданной длины
p, q = gen(p_l, q_l)
n = p*q
f = (p-1)*(q-1)
print(f'p={p}\nq={q}\nn = {n}\nf = {f}\n')

# Генерация случайного e в диапазоне от 1 до f, а затем вычисление d с помощью инверснии
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
		# Объявление открытых ключей
		with open('C:/Users/Юрий/Downloads/wed/file_for_N_e_rsa.txt','w') as f:
			f.write(str([n, e]))
	if (sw == '2'):
		decode('C:/Users/Юрий/Downloads/wed/2.txt', 'C:/Users/Юрий/Downloads/wed/3.txt', d, n)
