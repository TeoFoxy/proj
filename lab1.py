while True:
	sw = input('1.Пример 1\n2.Пример 2\n3. Пример 3\n')
	if(sw == '1'):
		print('Введите букву ', end='')
		a=input()
		for s in 'Hello world':
			if s==a:
				break
			else:
				print(s, 'Это не ', a)
	elif sw == '2':
		s='spam'
		print(s[3])
		a=len('spam')
		print(a)
	else:
		s='spam'
		print(s[-4])
		a=len('spam')
		print(a)
		break