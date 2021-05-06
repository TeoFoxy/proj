while True:
	sw = input('1.Пример 1\n2.Пример 2\n3. Пример 3\n4.Для примера 1 изменение а\n5.Для примера 1 изменение б\n6.Для примера 1 изменение в\n7.Для примера 2 изменение а\n8.Для примера 2 изменение б\n9.Для примера 2 изменение в\n10.Для примера 3 изменение а\n11.Для примера 3 изменение б\n12.Для примера 3 изменение в\n13.Для примера 3 изменение г\n14.Формирование элементов матрицы путем сложения индексов и произвольные замены элементов\n')
	if(sw == '1'):
		m=6
		n=5
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif sw == '2':
		m=6
		n=5
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for i in range(n):
			for j in range(m):
				if a[i][j]>5:
					a[i][j]=44
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif sw=='3':
		m=6
		n=5
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for i in range(n):
			for j in range(m):
				if i==j:
					a[i][j]=1
				if i>j:
					a[i][j]=0
				if i<j:
					a[i][j]=2
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif(sw == '4'):
		m=8
		n=8
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif(sw == '5'):
		m=8
		n=8
		a=[[(i+1)*(j+1) for j in range(m-1)] for i in range(n-1)]
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif(sw == '6'):
		m=8
		n=8
		a=[[(i+2)*(j+2) for j in range(m-2)] for i in range(n-2)]
		for row in a:
			print(' '.join([str(elem) for elem in row]))			
	elif(sw == '7'):
		m=8
		n=8
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for i in range(n):
			for j in range(m):
				if a[i][j]>5:
					a[i][j]=44
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif(sw=='8'):
		m=6
		n=5
		print('Введите элемент, на который хотите заменить 0: ', end='')
		b=int(input())
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for i in range(n):
			for j in range(m):
				if a[i][j]==0:
					a[i][j]=b
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif(sw == '9'):
		m=6
		n=5
		print('Введите b: ', end='')
		b=int(input())
		print('Введите элемент, на который хотите заменить элементы меньшие b: ', end='')
		q=int(input())
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for i in range(n):
			for j in range(m):
				if a[i][j]<b:
					a[i][j]=q
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif(sw=='10'):
		m=8
		n=8
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for i in range(n):
			for j in range(m):
				if i==j:
					a[i][j]=1
				if i>j:
					a[i][j]=0
				if i<j:
					a[i][j]=2
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif(sw=='11'):
		m=6
		n=5
		print('Введите элемент, на который хотите заменить элементы во 2 строке: ', end='')
		b=int(input())
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for i in range(n):
			for j in range(m):
				if i==j:
					a[i][j]=1
				if i>j:
					a[i][j]=0
				if i<j:
					a[i][j]=2
				if i==1:
					a[i][j]=b
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif(sw=='12'):
		m=5
		n=5
		print('Введите элемент, на который хотите заменить элементы на побочной диагонали: ', end='')
		b=int(input())
		a=[[i*j for j in range(n)] for i in range(n)]
		for row in a:
			print(' '.join([str(elem) for elem in row]))
		print()
		for i in range(n):
			for j in range(m):
				if i+j==n-1: 
					a[i][j]=b
		for row in a:
			print(' '.join([str(elem) for elem in row]))


	elif(sw=='13'):
		m=6
		n=5
		print('Введите элемент, на которых хотите заменить элементы в 3 столбце: ', end='')
		b=int(input())
		a=[[(i)*(j) for j in range(m)] for i in range(n)]
		for i in range(n):
			for j in range(m):
				if i==j:
					a[i][j]=1
				if i>j:
					a[i][j]=0
				if i<j:
					a[i][j]=2
				if j==2:
					a[i][j]=b
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	elif(sw=='14'):
		m=6
		n=5
		print('Введите элемент, на которых хотите заменить элементы во 2 строке: ', end='')
		b=int(input())
		a=[[(i)+(j) for j in range(m)] for i in range(n)]
		for i in range(n):
			for j in range(m):
				if i==1:
					a[i][j]=b
		for row in a:
			print(' '.join([str(elem) for elem in row]))
	else:
		print('Введите размерность матрицы: ', end='')
		while True:
			n=int(input())
			if (n%2==0):
				print('Введено четное число, введите другое: ',end='')
			if(n%2==1):
				break	
		a=[[i*j for j in range(n)] for i in range(n)]
		for row in a:
			print(' '.join([str(elem) for elem in row]))
		for i in range(n):
			for j in range(n):
				if (i==j) and (i+j==n-1): 
					print(a[i][j])