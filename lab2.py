while True:
	sw = input('1.Пример 1\n2.Пример 2\n3. Пример 3\n4.Ввод цифр(for)\n5.Ввод цифр(while)\n6.Сумма положительных элементов(while)\n7.Сумма отрицательных элементов(while)\n8.Сумма положительных элементов(for)\n9.Сумма отрицательных элементов(for)\n10.Подсчет в заданной последовательности натуральных чисел количества чисел, имеющий делитель равный 2.\n11.Подсчет в заданной последовательности натуральных чисел количества чисел, имеющих делитель равный 3, а также подсчет суммы и произведения таких чисел\n')
	if(sw == '1'):
		print('Введите количество элементов ', end='')
		k=int(input())
		print('Введите начальное значение ', end='')
		n=int(input())
		print('Введите шаг ', end='')
		h=int(input())
		sum1=0
		a=0
		for a in range(k):
			sum1=sum1+n
			n=n+h
		print('Сумма элементов =', sum1)
	elif sw == '2':
		print('Введите количество элементов ', end='')
		k=int(input())
		print('Введите начальное значение ', end='')
		n=int(input())
		print('Введите шаг ', end='')
		h=int(input())
		sum1=0
		a=0
		while a<k:
			sum1=sum1+n
			n=n+h
			a=a+1
		print('Сумма элементов = ',sum1)
	elif sw=='3':
		for v in range(100):
			print('N= ',end='')
			n=int(input())
			print('M= ',end='')
			m=int(input())
			if (n>0) and (m>0) and (n<m):
				break
		k=0
		Sum=0
		P=1
		for i in range(n,m):
			Pr=True
			if i==4:
				Pr=False
			for j in range(2,i//2):
				if (i%j==0):
					Pr==False
					break
			if Pr==True:
				k=k+1
				Sum=Sum+i
				P=P*i
				print(i)
		if k==0:
			print('Простых чисел в диапазоне нет')
		else:
			print('Простых чисел в диапазоне ', k)
			print('Сумма простых чисел в диапазоне', Sum)
			print('Произведение простых чисел в диапазоне', P)
	elif sw=='4':
		for i in range(10):
			a=i
			print(a)
	elif sw=='5':
		a=0
		i=0
		while (i<10):
			a=i
			i+=1
			print(a)
	elif sw=='6':
		a=[]
		i=0
		Sum=0
		print('Введите количество элементов массива: ', end='')
		n=int(input())
		for j in range(n):
			a.append(input())
		while True:
			if (int(a[i])>0):
				Sum=Sum+int(a[i])
			i=i+1
			if (i==n):
				break
		print('Сумма положительных элементов массива =',Sum)
	elif sw=='7':
		a=[]
		i=0
		Sum=0
		print('Введите количество элементов массива: ', end='')
		n=int(input())
		for j in range(n):
			a.append(input())
		while True:
			if (int(a[i])<0):
				Sum=Sum+int(a[i])
			i=i+1
			if (i==n):
				break
		print('Сумма отрицательных элементов массива =',Sum)
	elif sw=='8':
		a=[]
		Sum=0
		print('Введите количество элементов массива: ', end='')
		n=int(input())
		for i in range(n):
			a.append(input())
			if (int(a[i])>0):
				Sum=Sum+int(a[i])
		print('Сумма положительных элементов массива =',Sum)
	elif sw=='9':
		a=[]
		Sum=0
		print('Введите количество элементов массива: ', end='')
		n=int(input())
		for i in range(n):
			a.append(input())
			if (int(a[i])<0):
				Sum=Sum+int(a[i])
		print('Сумма отрицательных элементов массива =',Sum)
	elif sw=='10':
		a=[]
		k=0
		print('Введите количество чисел в последовательности: ', end='')
		n=int(input())
		print('Заполните последовательность натуральными числами: ',end='')
		for i in range(n):
			a.append(input())
			if (int(a[i])%2==0):
				k=k+1
		print('Количество чисел в последовательности с делителем равным 2 = ', k)
	elif sw=='11':
		a=[]
		k=0
		Sum=0
		prod=1
		print('Введите количество чисел в последовательности: ', end='')
		n=int(input())
		print('Заполните последовательность натуральными числами: ',end='')
		for i in range(n):
			a.append(input())
			if (int(a[i])%3==0):
				k=k+1
				Sum=Sum+int(a[i])
				prod=prod*int(a[i])
		print('Количество чисел в последовательности с делителем равным 3 = ', k)
		print('Сумма подходящих чисел = ', Sum)
		print('Произведение подходящих чисел = ', prod)		
	else:
		a=[]
		k=0
		Sum=0
		print('Введите количество чисел в последовательности: ', end='')
		n=int(input())
		print('Заполните последовательность натуральными числами: ',end='')
		for i in range(n):
			a.append(input())
			if (int(a[i])%5==0):
				k=k+1
				Sum=Sum+int(a[i])
		print('Количество чисел в последовательности с делителем равным 3 = ', k)
		print('Сумма подходящих чисел = ', Sum)