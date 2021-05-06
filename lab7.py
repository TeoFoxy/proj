from tkinter import*
import math
import sys
while True:
	sw = input('1.Задание 1\n2.Задание 2\n')
	if (sw=='1'):
		root=Tk()
		root.title("GUI на Python")
		root.geometry("600x550+300+100")
		def close():
			root.destroy()

		clicks=0
		def click_button():
			global clicks
			clicks+=1
			root.title("Clicks {}".format(clicks))

			root1=Tk()
			root1.title("Новое окно")
			root1.geometry("300x250+50+25")
			btn1=Button(root1,
				text="Закрыть первое окно",
				background="#ff0000",
				foreground="#000000",
				padx="20",
				pady="8",
				font="16",
				command=close)
			btn1.pack()

		btn=Button(root,
			text='Открыть новое окно и изменить Имя первого',
			background="#ffff00",
			foreground="#00ff7f",
			padx="20",
			pady="8",
			font="16",
			command=click_button)
		btn.pack()
		root.mainloop()

	if (sw=='2'):
		root=Tk()
		root.title("GUI на Python")
		root.geometry("600x550+300+100")
		def close():
			root.destroy()

		def click_button():
			label3=Label(text='Ваше имя',justify=CENTER)
			label3.grid(row=7,column=5,sticky="w",pady=10)
			label4=Label(text=name_entry.get(),justify=CENTER)
			label4.grid(row=9,column=5,sticky="w",pady=10)
			label5=Label(text='Ваша фамилия',justify=CENTER)
			label5.grid(row=11,column=5,sticky="w",pady=10)
			label6=Label(text=surname_entry.get(),justify=CENTER)
			label6.grid(row=12,column=5,sticky="w",pady=10)

		def clear():
			name_entry.delete(0,END)
			surname_entry.delete(0,END)

		name_label=Label(text="Введите имя:")
		surname_label=Label(text="Введите фамилию:")
		name_label.grid(row=4,column=4,sticky="w",padx=50, pady=10)
		surname_label.grid(row=5,column=4,sticky="w",padx=50,pady=10)

		name_entry=Entry()
		surname_entry=Entry()
		name_entry.grid(row=4,column=5,padx=50,pady=10)
		surname_entry.grid(row=5,column=5,padx=50,pady=10)

		btn=Button(root,
			text='Вывод текста',
			background="#ffff00",
			foreground="#00ff7f",
			padx="20",
			pady="8",
			font="Arial 14",
			command=click_button)
		btn1=Button(root,
			text='Закрыть окно',
			background="#ff0000",
			foreground="#000000",
			padx="20",
			pady="8",
			font=("Times New Roman",14, "bold"),
			command=close)
		btn2=Button(root,
			text='Очистить поле ввода',
			background="#00ff00",
			foreground="#000000",
			padx="20",
			pady="8",
			font=("Times New Roman",14, "bold"),
			command=clear)
		btn.place(x=50,y=450)
		btn1.place(x=370,y=450)
		btn2.place(x=160,y=350)
		root.mainloop()
	if (sw=='3'):
		def second_window():
			root1=Tk()
			root1.title("Считывание данных из файла")
			root1.geometry("300x130+300+100")
			label1=Label(root1,text=f'Результат вычисления функции: {calc_file()}',justify=CENTER)
			btn1=Button(root1,text="Расчет",
				command=label1.pack)
			label1.place(x=300,y=40)
			btn1.pack()

		def third_window():
			root2=Toplevel()
			root2.title("Считывание данных пользователя")
			root2.geometry("300x130+300+100")

			x_label=Label(root2,text="x= ")
			x_label.place(x=5,y=5)
			x=Entry(root2,width=19)
			x.place(x=30,y=5)
			y_label=Label(root2,text="y= ")
			y_label.place(x=5,y=30)
			y=Entry(root2,width=19)
			y.place(x=30,y=30)
			z_label=Label(root2,text="z= ")
			z_label.place(x=5,y=55)
			z=Entry(root2,width=19)
			z.place(x=30,y=55)
			q1=(math.pow(x,y+1)+math.exp(y-1))/(1+x*math.fabs(y-math.tan(z)))
			q2=(1+math.fabs(x-y))
			q3=math.pow(math.fabs(y-x),2)/2
			q4=math.pow(math.fabs(y-x),3)/3
			h=float(q1*q2+q3-q4)
			h=round(h,3)
			btn1=Button(root2,text="Расчет",
				command=lambda: cout(h))
			
		def cout(h):
			with open(sys.argv[2]) as f:
				f.write('h=',h)
			


		def calc_file():
			with open(sys.argv[1]) as f:
				k=f.read()
			x = float(k.split(';')[0].split('[')[-1])
			y = float(k.split(';')[1])
			z = float(k.split(';')[2].split(']')[0])
			# print(x,y,z)
			q1=(math.pow(x,y+1)+math.exp(y-1))/(1+x*math.fabs(y-math.tan(z)))
			q2=(1+math.fabs(x-y))
			q3=math.pow(math.fabs(y-x),2)/2
			q4=math.pow(math.fabs(y-x),3)/3
			h=float(q1*q2+q3-q4)
			h=round(h,3)
			# print('h= ', h)
			return h
			
			
		
		
		root=Tk()
		root.title("Пример 3")
		canvas=Canvas(root,width=300, height=130)
		canvas.pack()
		lab=Label(text = 'Выберите режим:')
		lab.place(x=5, y=5)
		btn1=Button(root,text="Чтение данных из файла",
			command=second_window)
		btn1.pack()
		btn2=Button(root,text="Ввод данных и запись результата в файл",
			command=third_window)
		btn2.pack()
		root.mainloop()
		