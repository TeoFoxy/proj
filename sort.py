import time
from random import randint 
# Выбор
def selection_sort(arr):
	for i in range(len(arr)):
		minimum= i
		for j in range(i+1, len(arr)):
			if arr[j]<arr[minimum]:
				minimum=j
		arr[minimum],arr[i]=arr[i],arr[minimum]
	return arr
# Вставки
def insertion(arr):
	for i in range(len(arr)):
		cursor=arr[i]
		pos = i
		while pos>0 and arr[pos-1]>cursor:
			arr[pos]=arr[pos-1]
			pos = pos -1
		arr[pos]=cursor
	return arr
# Подсчет
def counting_sort1(arr):
	scope=max(arr)+1
	C=[0]*scope
	for x in arr:
		C[x]+=1
	arr[:]=[]
	for number in range(scope):
		arr+=[number]*C[number]

list_= []
N=int(input('N= '))
for i in range(N):
	list_.append(randint(0,1000))
input('start=')
start=time.time()
# selection_sort(list_)
# insertion(list_)
# list_.sort()
counting_sort1(list_)
res=time.time()-start
print(res)