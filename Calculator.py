from tkinter import *


def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	input.set(operator)

def clearScr():
	global operator
	operator =""
	input.set("")

def btnEqual():
	global operator
	sum = str(eval(operator))
	input.set(sum)
	operator  = ""



cal = Tk()
cal.title("Calculator")
operator = ""
input = StringVar()


txtDisplay = Entry(cal, font=('arial', 20, 'bold'),bd=30, textvariable=input,insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)


btn7 = Button(cal, padx=16, bd=8,pady=16, text="7", command=lambda:btnClick(7), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=1, column=0)

btn8 = Button(cal, padx=16, bd=8,pady=16, text="8", command=lambda:btnClick(8), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=1, column=1)

btn9 = Button(cal, padx=16, bd=8,pady=16, text="9", command=lambda:btnClick(9), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=1, column=2)

Addition = Button(cal, padx=16, bd=8,pady=16, text="+", command=lambda:btnClick("+"), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=1, column=3)

#====================================================================================================================================

btn6 = Button(cal, padx=16, bd=8,pady=16, text="6", command=lambda:btnClick(6), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=2, column=0)

btn5 = Button(cal, padx=16, bd=8,pady=16, text="5", command=lambda:btnClick(5), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=2, column=1)

btn4 = Button(cal, padx=16, bd=8,pady=16, text="4", command=lambda:btnClick(4), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=2, column=2)

Subtraction = Button(cal, padx=16,pady=16, bd=8, text="-", command=lambda:btnClick("-"), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=2, column=3)

#====================================================================================================================================

btn3 = Button(cal, padx=16, bd=8,pady=16, text="3", command=lambda:btnClick(3), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=3, column=0)

btn2 = Button(cal, padx=16, bd=8,pady=16, text="2", command=lambda:btnClick(2), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=3, column=1)

btn1 = Button(cal, padx=16, bd=8,pady=16, text="1", command=lambda:btnClick(1), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=3, column=2)

Multiplication = Button(cal, padx=16,pady=16, bd=8, command=lambda:btnClick("*"), text="*", fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=3, column=3)

#====================================================================================================================================

btn0 = Button(cal, padx=16,pady=16, bd=8, text="0", command=lambda:btnClick(0), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=4, column=0)

btnClear = Button(cal, padx=16,pady=16, bd=8, text="C", command=lambda:clearScr(), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=4, column=1)

btnEquals = Button(cal, padx=16,pady=16, bd=8, text="=", command=lambda:btnEqual(), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=4, column=2)

Division = Button(cal, padx=16, pady=16, bd=8, text="/", command=lambda:btnClick("/"), fg="black",bg="powder blue", font=('arial', 20, 'bold')).grid(row=4, column=3)





cal.mainloop()