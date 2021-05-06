import sys
from termcolor import cprint, colored
def hash(file_in):
	with open(file_in, 'rb') as f:
		a=bytearray(f.read())
	res=[]
	for i in range(0, len(a)-1, 2):
		b = a[i:i+2]
		print(list(b))
		# res.append(b[0]^b[1])
		# res.append(a[i]^a[i+1])
		res.append(int.from_bytes(a[i]^a[i+1],'little'))
		# print(f'a[{i}] = {a[i]}\na[{i+1}] = {a[i+1]}')
		print(a[i]^a[i+1])
	# print(res)
	print(bin(int.from_bytes(res,'big')))
	f=sum(res) & 0b1111111111111111
	print(f'hash = {f}')
	# print(int.from_bytes(res, 'big') & 0b1111111111111111)
	# print(int.from_bytes(res, 'little') & 0b11111111111111111)
	# print(bin(int.from_bytes(res, 'little')))
	# print(len(bin(int.from_bytes(res, 'big') & 0b1111111111111111)[2:]))
	print(len(bin(int.from_bytes(res, 'little') & 0b1111111111111111)[2:]))

def hash_gen(file_in):
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
		# hash_.append(a[i]^a[i+1])
	# print(len(a))
	h=sum(hash_)
	f = h & 0b1111111111111111
	print(f'Ваш хэш: {f}')
	return f


def hash_gen1(file_in):
	hash_ = []
	with open(file_in, 'rb') as f:
		a = bytearray(f.read())
	l = len(a)//3
	for i in range(l+2):
		hash_.append(int.from_bytes(a[i*3:i*3+3], 'little'))
	h = sum(hash_)^pow(2, 23)
	f = h & 0b111111111111111111111111
	cprint(f'Ваш хэш: {f}', 'red')
	return f

while True:
	sw = input('1.Запись хэша\n2.Шифрование')
	if (sw == '1'):
		print(hash_gen(sys.argv[1]))
		# with open(sys.argv[1], 'rb') as f:
	else: 
		exit()