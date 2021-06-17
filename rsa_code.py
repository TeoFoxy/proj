from random import randint
from numpy import prod
from my_funcs import *
import sys

def code(file_in, file_out, e, n):
	# Побайтовое считывание файла, который нужно будет шифровать
	with open(file_in, 'rb') as f:
		a = bytearray(f.read()) #Запись в переменную a массива байтов

	# Вычисление длины блоков
	l=len(bin(n)[2:])//8
	# Запись блоков (записывается по 3 байта, в соответствии с предыдущим пунктом)
	data = (a[i:i+l] for i in range(0, len(a), l))
	en = bytearray()
	for block in data:
		# Перевод блоков в числа, чтобы потом произвести с ними нужные вычисления
		c = int.from_bytes(block, 'little')
		# Шифрование блоков, а затем перевод их в байты
		en += (power(c, e, n).to_bytes(l+1, 'little'))
	# Запись зашифрованного сообщения в файл
	with open(file_out, 'wb') as f:
		f.write(en)


while True:
	sw=input('1.Принять N и e\n2.Зашифровать файл\n')
	if (sw == '1'):
		# Принятие открытых ключей
		with open('C:/Users/Юрий/Downloads/wed/file_for_N_e_rsa.txt','r') as f:
			re=f.read()
			# Разбиение строки на отдельные элементы с помощью ",", "[" и "]", а затем перевод полученных значений в int
			n=int(re.split(',')[0].split('[')[-1])
			e=int(re.split(',')[1].split(']')[0])
			print(f'n= {n}\ne={e}\n')
	if (sw == '2'):
		code('C:/Users/Юрий/Downloads/wed/1.txt', 'C:/Users/Юрий/Downloads/wed/2.txt', e, n)
		
