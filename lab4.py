from random import *
from tkinter import *
import time
while True:
	sw = input('1.Пример 1\n2.Изменение примера 1 в соответствии с вариантом а\n3.Изменение примера 1 в соответствии с вариантом б\n4.Изменение примера 1 в соответствии с вариантом в\n5.Изменение примера 1 в соответствии с вариантом г\n6.Пример с линиями\n7.Пример с треугольниками\n8.Пример с прямоугольниками\n9.Пример с многоугольниками\n10.Пример с текстом\n')
	if(sw == '1'):
		size = 600
		root=Tk()
		canvas = Canvas(root,width=size, height=size)
		canvas.pack()
		diapason = 0
		while diapason<2000:
			colors = choice(['aqua','blue','fuchsia','green','maroon','orange','pink','purple','red','yellow','violet','indigo','chartreuse','lime'])
			x=randint(0,size)
			y=randint(0,size)
			d=randint(0,size/3)
			canvas.create_oval(x,y,x+d, y+d,fill=colors)
			root.update()
			diapason+=1
		while True:
			colors=choicecolors=choice(['aqua','blue','fuchsia','green','maroon','orange','pink','purple','red','yellow','violet','indigo','chartreuse','lime'])
			x0=randint(0,size)
			y0=randint(0,size)
			d=randint(0,size/3)
			canvas.create_oval(x0,y0,x0+d,y0+d,fill=colors)
			root.update()
	elif sw == '2':
		size = 810
		root=Tk()
		canvas = Canvas(root,width=size, height=size)
		canvas.pack()
		diapason = 0
		while diapason<2000:
			colors = choice(['aqua','blue','fuchsia','green','maroon','orange','pink','purple','red','yellow','violet','indigo','chartreuse','lime'])
			x=randint(0,size)
			y=randint(0,size)
			d=randint(0,size/3)
			canvas.create_oval(x,y,x+d, y+d,fill=colors)
			root.update()
			diapason+=1
		while True:
			colors=choicecolors=choice(['aqua','blue','fuchsia','green','maroon','orange','pink','purple','red','yellow','violet','indigo','chartreuse','lime'])
			x0=randint(0,size)
			y0=randint(0,size)
			d=randint(0,size/3)
			canvas.create_oval(x0,y0,x0+d,y0+d,fill=colors)
			root.update()
	elif sw == '3':
		size = 800
		root=Tk()
		canvas = Canvas(root,width=size, height=size)
		canvas.pack()
		diapason = 0
		while diapason<2000:
			colors = choice(['aqua','blue','fuchsia','green','maroon','orange','pink','purple','red','yellow','violet','indigo','chartreuse','lime'])
			x=randint(0,size)
			y=randint(0,size)
			d=randint(0,size/100)
			canvas.create_oval(x,y,x+d, y+d, outline = 'lime', fill=colors)
			root.update()
			diapason+=1
		while True:
			colors=choicecolors=choice(['aqua','blue','fuchsia','green','maroon','orange','pink','purple','red','yellow','violet','indigo','chartreuse','lime'])
			x0=randint(0,size)
			y0=randint(0,size)
			d=randint(0,size/100)
			canvas.create_oval(x0,y0,x0+d,y0+d, outline = 'lime',fill=colors)
			root.update()
	elif sw == '4':
		size = 800
		root=Tk()
		canvas = Canvas(root,width=size, height=size)
		canvas.pack()
		diapason = 0
		while diapason<2000:
			colors = choice(['aqua','blue','fuchsia','green','maroon','orange','pink','purple','red','yellow','violet','indigo','chartreuse','lime'])
			x=randint(0,size)
			y=randint(0,size)
			d=randint(0,size/2)
			canvas.create_oval(x,y,x+d, y+d, outline = 'lime', fill=colors)
			root.update()
			diapason+=1
		while True:
			colors=choicecolors=choice(['aqua','blue','fuchsia','green','maroon','orange','pink','purple','red','yellow','violet','indigo','chartreuse','lime'])
			x0=randint(0,size)
			y0=randint(0,size)
			d=randint(0,size/2)
			canvas.create_oval(x0,y0,x0+d,y0+d, outline = 'lime',fill=colors)
			root.update()
			
	elif sw == '5':
		start=time.time()
		# print(start)
		size = 800
		root=Tk()
		canvas = Canvas(root,width=size, height=size)
		canvas.pack()
		diapason = 0
		while diapason<25000:
			colors = choice(['aqua','blue','fuchsia','green','maroon','orange','pink','purple','red','yellow','violet','indigo','chartreuse','lime'])
			x=randint(0,size)
			y=randint(0,size)
			d=randint(0,size/2)
			canvas.create_oval(x,y,x+d, y+d, outline = 'lime', fill=colors)
			root.update()
			diapason+=1
			fin=time.time()
			res=fin-start
			# print(res)
			if (res>5):
				print(res)
				exit()
	elif sw == '6':
		size = 800
		root = Tk()
		canvas = Canvas(root, width = size, height = size)
		canvas.pack()
		diapazon = 0
		bt = Button(root, text = 'Stop',width = 10, height = 2, command = lambda: root.destroy())
		bt.place(x = size - size//2, y = size - 50)
		while True:
			colors = choice(['aqua', 'blue', 'indigo'])
			x1 = randint(0, size)
			y1 = randint(0, size)
			x2 = randint(0, size)
			y2 = randint(0, size)
			canvas.create_line(x1, y1, x2, y2, fill = colors)
			root.update()
		root.mainloop()
	elif sw == '7':
		size = 800
		root = Tk()
		canvas = Canvas(root, width = size, height = size)
		canvas.pack()
		diapazon = 0
		bt = Button(root, text = 'Stop',width = 10, height = 2, command = lambda: root.destroy())
		bt.place(x = size - size//2, y = size - 50)
		while True:
			colors = choice(['aqua', 'pink', 'indigo'])
			x1 = randint(0, size)
			y1 = randint(0, size)
			x2 = randint(0, size)
			y2 = randint(0, size)
			x3 = randint(0, size)
			y3 = randint(0, size)
			canvas.create_polygon([x1, y1, x2, y2, x3, y3], fill = colors)
			root.update()
		root.mainloop()
	elif sw == '8':
		size = 800
		root = Tk()
		canvas = Canvas(root, width = size, height = size)
		canvas.pack()
		diapazon = 0
		bt = Button(root, text = 'Stop',width = 10, height = 2, command = lambda: root.destroy())
		bt.place(x = size - size//2, y = size - 50)
		while True:
			colors = choice(['aqua', 'pink', 'indigo'])
			x1 = randint(0, size)
			y1 = randint(0, size)
			x2 = randint(0, size)
			y2 = randint(0, size)
			canvas.create_rectangle(x1, y1, x2, y2, fill = colors)
			root.update()
		root.mainloop()

	elif sw == '9':
		size = 800
		root = Tk()
		canvas = Canvas(root, width = size, height = size)
		canvas.pack()
		diapazon = 0
		bt = Button(root, text = 'Stop',width = 10, height = 2, command = lambda: root.destroy())
		bt.place(x = size - size//2, y = size - 50)
		while True:
			points = []
			colors = choice(['aqua', 'pink', 'indigo'])
			for i in range(randint(3, 7)):
				points.append(randint(0, size))
				points.append(randint(0, size))
			canvas.create_polygon(points, fill = colors)
			root.update()
		root.mainloop()
	elif sw == '10':
		size = 800
		root = Tk()
		canvas = Canvas(root, width = size, height = size)
		canvas.pack()
		txt_in = Text(root, width=size//11, height=20, font="20")
		while True:
			letters = choices('abcdefghijklmnopqrstuvwxyzйцукенгшщзхъфывапролджэячсмитьбю1234567890.,!@#$%^&*()_+№;%:?', k=randint(1, 10))
			colors=choice(['aqua','blue','fuchsia','green','maroon','orange',
	       	            'pink','purple','red','yellow','violet','indigo',
	       	            'chartreuse','lime'])
			x = randint(0, size - 50)
			y = randint(0, size - 50)
			canvas.create_text(x, y, text = letters, fill = colors)
			root.update()
		root.mainloop()