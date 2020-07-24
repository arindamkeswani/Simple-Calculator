from tkinter import *

root=Tk()
root.title("Calculator")

e= Entry(root,width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)


def button_click(number):
	#e.delete(0)
	current= e.get()
	e.delete(0,END)
	e.insert(0,str(current) + str(number)) 

def button_clear():
	e.delete(0,END)

def button_ad():
	first= e.get() #first number
	global f_num
	global math
	math ="addition"
	f_num= int(first)
	e.delete(0,END)

def button_sub():
	first= e.get() #first number
	global f_num
	global math
	math ="subtraction"
	f_num= int(first)
	e.delete(0,END)

def button_mul():
	first= e.get() #first number
	global f_num
	global math
	math ="multiplication"
	f_num= int(first)
	e.delete(0,END)

def button_div():
	first= e.get() #first number
	global f_num
	global math
	math ="division"
	f_num= int(first)
	e.delete(0,END)

def button_e():
	second= e.get() #second number
	e.delete(0,END)

	if math=="addition":
		e.insert(0,f_num + int(second))

	if math=="subtraction":
		e.insert(0,f_num - int(second))
	if math=="multiplication":
		e.insert(0,f_num * int(second))
	if math=="division":
		e.insert(0,f_num / int(second))
#Define buttons
button1= Button(root, text="1", padx=30,pady=20, command=lambda: button_click(1))
button2= Button(root, text="2", padx=30,pady=20, command=lambda: button_click(2))
button3= Button(root, text="3", padx=30,pady=20, command=lambda: button_click(3))
button4= Button(root, text="4", padx=30,pady=20, command=lambda: button_click(4))
button5= Button(root, text="5", padx=30,pady=20, command=lambda: button_click(5))
button6= Button(root, text="6", padx=30,pady=20, command=lambda: button_click(6))
button7= Button(root, text="7", padx=30,pady=20, command=lambda: button_click(7))
button8= Button(root, text="8", padx=30,pady=20, command=lambda: button_click(8))
button9= Button(root, text="9", padx=30,pady=20, command=lambda: button_click(9))
button0= Button(root, text="0", padx=30,pady=20, command=lambda: button_click(0))
button_add= Button(root,text="+", padx=30,pady=20,command=button_ad)
button_eq= Button(root,text="=", padx=70,pady=20,command=button_e)
button_cls= Button(root,text="C", padx=70,pady=20,command=button_clear)
button_s= Button(root,text="-", padx=30,pady=20,command=button_sub)
button_m= Button(root,text="x", padx=30,pady=20,command=button_mul)
button_d= Button(root,text="/", padx=30,pady=20,command=button_div)
#Put buttons on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
button_cls.grid(row=4,column=1, columnspan=2)
button_add.grid(row=5,column=0)

button_s.grid(row=6,column=0)
button_m.grid(row=6,column=1)
button_d.grid(row=6,column=2)

button_eq.grid(row=5,column=1,columnspan=2)

root.mainloop()