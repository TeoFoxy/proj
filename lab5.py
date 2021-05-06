from random import *
import sys,os
while True:
	sw = input('2.Задание 2\n3.Задание 3\n4.Задание 4\n5.Задание 5\n6.Задание 6\n7.Выход\n')
	if(sw == '2'):
		print('Введите переменную A: ',end='')
		a=int(input())
		print('Введите переменную B: ',end='')
		b=int(input())
		c=a+b
		file=open('C:/Users/Юрий/Downloads/wed/1.txt', "w")
		file.write("Сумма A+B равна ")
		file=open('C:/Users/Юрий/Downloads/wed/1.txt',"a")
		file.write(' '+(str(c)))
		file.close()
		file=open('C:/Users/Юрий/Downloads/wed/1.txt',"r")
		print(file.read())
		print(file.name)
		print(file.mode)
		file.close()
	if(sw == '3'):
	# 	print('Введите переменную A: ',end='')
	# 	a=int(input())
	# 	print('Введите переменную B: ',end='')
	# 	b=int(input())
	# 	with open('C:/Users/Юрий/Downloads/wed/file.txt', 'w') as f:
	# 		f.write(f'a + b = {a+b}\na - b = {a-b}\na * b = {a*b}\na / b = {round(a/b, 2)}')
		print('Введите n: ', end='')
		n=int(input())
		print('Введите фразу: ', end='')
		txt=str(input())
		with open('C:/Users/Юрий/Downloads/wed/file.txt', 'w') as f:
			for i in range(n):
				f.write(txt + '\n')
	if(sw == '4'):
		print('Введите переменную A: ',end='')
		a=int(input())
		print('Введите переменную B: ',end='')
		b=int(input())
		with open('C:/Users/Юрий/Downloads/wed/file1.txt', 'w') as f:
			f.write(f'a + b = {a+b}')
			print('Название файла: ',str(f.name).split('/')[-1])
			print('Файл открыт в режиме для чтения' if f.mode == 'w' else f'Файл открыт в режиме {f.mode}')
		with open('C:/Users/Юрий/Downloads/wed/file2.txt', 'w') as f:
			f.write(f'a - b = {a-b}')
			print('Название файла: ',str(f.name).split('/')[-1])
			print('Файл открыт в режиме для чтения' if f.mode == 'w' else f'Файл открыт в режиме {f.mode}')
		with open('C:/Users/Юрий/Downloads/wed/file3.txt', 'w') as f:
			f.write(f'a * b = {a*b}')
			print('Название файла: ',str(f.name).split('/')[-1])
			print('Файл открыт в режиме для чтения' if f.mode == 'w' else f'Файл открыт в режиме {f.mode}')
		with open('C:/Users/Юрий/Downloads/wed/file4.txt', 'w') as f:
			f.write(f'a / b = {round(a/b, 2)}')
			print('Название файла: ',str(f.name).split('/')[-1])
			print('Файл открыт в режиме для чтения' if f.mode == 'w' else f'Файл открыт в режиме {f.mode}')
	if sw == '5':
		with open('C:/Users/Юрий/Downloads/wed/file1.txt', 'rb') as f:
			a = bytearray(f.read())
		print('============')
		print(a.decode('utf-8'))
		with open('C:/Users/Юрий/Downloads/wed/file2.txt', 'rb') as f:
			a = bytearray(f.read())
		print('============')
		print(a.decode('utf-8'))
		with open('C:/Users/Юрий/Downloads/wed/file3.txt', 'rb') as f:
			a = bytearray(f.read())
		print('============')
		print(a.decode('utf-8'))
		with open('C:/Users/Юрий/Downloads/wed/file4.txt', 'rb') as f:
			a = bytearray(f.read())
		print('============')
		print(a.decode('utf-8'))
		print('============')
	if sw=='6':
		arr = []
		for i in range(randint(3, 10)):
			arr.append(randint(-13, 13))
		with open('C:/Users/Юрий/Downloads/wed/rand.txt', 'w') as f1:
				f1.write(''.join(str(arr).replace("[", "").replace("]","")))
		del arr
		with open('C:/Users/Юрий/Downloads/wed/rand.txt', 'r') as f1:
			b = f1.read()
		arr = []
		for i in b.split(', '):
			arr.append(int(i, 10))
		arr1 = []
		for i in arr:
			if i > 0:
				arr1.append(round(i*i/3, 2))
			if i <= 0:
				arr1.append(3*i*i)
		with open('C:/Users/Юрий/Downloads/wed/f.txt', 'w') as f2:
			f2.write(''.join(str(arr1).replace("[", "").replace("]","")))
		print(arr)
		print(arr1)
	if sw == '7':
		exit()