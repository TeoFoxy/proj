from random import randint
import time
from my_funcs import *
def baby_giant(A,P,y):
	# подбор значений m и k, при условии, что m*k>P
	while True:
		m=randint(1,P)
		k=randint(1,P)
		if ((m*k-P)<=1000000) and (m*k-P>=1):
			break
	# print('m=',m,'k=',k)


	# Заполнение 1 таблицы по формуле: (A**j)*y mod P(заполнение идет до m-1)
	arr=[]
	for j in range(m-1):
		res=(A**j)*y
		res=power(res,1,P)
		arr.append(res)
	# print(arr)


	# Заполнение 2 таблицы по формуле: A**(i*m) mod P(заполнение идет до m*k ) 
	arr_2=[]
	for i in range(m*k):
		st=i*m
		# res=(A**st) % P
		res=power(A,st,P)
		arr_2.append(res)
	# print(arr_2)

	# Поиск совпадений в 2 таблицах и запоминание номера соответствующих элементов
	for j in range(m-1):
		for i in range(m*k):
			if arr[j]==arr_2[i]:
				res_i=i
				res_j=j
			if arr[j]==arr_2[i]:
				break
		if arr[j]==arr_2[i]:
			break
	# print('i=',res_i, 'j=', res_j)


	# Вычисление x
	x=i*m-j
	x=x % P
	print('x=',x)

	
	# Проверка найденного значения x
	prov=power(A,x,P)
	if prov==y:
		print('yeap')
	else:
		print('nope')


while True:
	sw=input('1.Стандартный метод.\n2.Большие простые случайные числа.\n3.Перебор\n')
	if (sw=='1'):
		A=int(input('Введите A:'))
		P=int(input('Введите P:'))
		y=int(input('Введите y:'))
		start=time.time()
		baby_giant(A,P,y)
		res=time.time()-start
		print('time=',res)
	if (sw=='2'):
		while True:
			A=randint(1, 25)
			if simple_check(A):
				break
		print('A=',A)
		while True:
			y=randint(2**20, 2**30)
			if simple_check(y):
				break
		print('y=',y)
		while True:
			P=randint(2**20, 2**30)
			if (simple_check(P)) and (P>y):
				break
		print('P=',P)
		start=time.time()
		
		baby_giant(A,P,y)
		res=time.time()-start
		print('time=',res)
	if (sw=='3'):
		A=int(input('Введите A:'))
		P=int(input('Введите P:'))
		y=int(input('Введите y:'))
		# while True:
		# 	A=randint(2**20, 2**30)
		# 	if simple_check(A):
		# 		break
		# print('A=',A)

		# while True:
		# 	y=randint(2**20, 2**30)
		# 	if simple_check(y):
		# 		break
		# print('y=',y)
		
		# while True:
		# 	P=randint(2**20, 2**30)
		# 	if (simple_check(P)) and (P>y):
		# 		break
		# print('P=',P)
		x=2
		start=time.time()
		while True:
			if power(A,x,P)==y:
				break
			else:
				x+=1
		print('x=',x)
		res=time.time()-start
		print('time=',res)