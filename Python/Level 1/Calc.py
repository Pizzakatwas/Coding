from tkinter import *

def Delete():
    Input.config(text=Input.cget('text')[:-1])

def Evaluate():
    Input.configure(text=str(eval(Input.cget('text'))))

def Clear():
    Input.config(text='')

def input1():
    Input.config(text=Input.cget('text')+'1')

def input2():
    Input.config(text=Input.cget('text')+'2')

def input3():
    Input.config(text=Input.cget('text')+'3')

def input4():
    Input.config(text=Input.cget('text')+'4')

def input5():
    Input.config(text=Input.cget('text')+'5')

def input6():
    Input.config(text=Input.cget('text')+'6')

def input7():
    Input.config(text=Input.cget('text')+'7')

def input8():
    Input.config(text=Input.cget('text')+'8')

def input9():
    Input.config(text=Input.cget('text')+'9')

def input0():
    Input.config(text=Input.cget('text')+'0')

def inputDot():
    Input.config(text=Input.cget('text')+'.')

def Plus():
    Input.config(text=Input.cget('text')+'+')

def Subtract():
    Input.config(text=Input.cget('text')+'-')

def Mtp():
    Input.config(text=Input.cget('text')+'*')

def Dvd():
    Input.config(text=Input.cget('text')+'/')

window = Tk()
window.title("Rabii's calculator program :)")

Input = Label(window,
              fg='green',
              bg='black',
              font=('Futura',30),
              width=14,
              height=2,
              relief=RAISED,
              bd=10)
Input.grid(row=0,column=0,columnspan=4)

Button1 = Button(window,
                 text='1',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input1,
                 relief=RAISED,
                 bd=5)
Button1.grid(row=1,column=0)

Button2 = Button(window,
                 text='2',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input2,
                 relief=RAISED,
                 bd=5)
Button2.grid(row=1,column=1)

Button3 = Button(window,
                 text='3',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input3,
                 relief=RAISED,
                 bd=5)
Button3.grid(row=1,column=2)

Button4 = Button(window,
                 text='4',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input4,
                 relief=RAISED,
                 bd=5)
Button4.grid(row=2,column=0)

Button5 = Button(window,
                 text='5',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input5,
                 relief=RAISED,
                 bd=5)
Button5.grid(row=2,column=1)

Button6 = Button(window,
                 text='6',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input6,
                 relief=RAISED,
                 bd=5)
Button6.grid(row=2,column=2)

Button7 = Button(window,
                 text='7',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input7,
                 relief=RAISED,
                 bd=5)
Button7.grid(row=3,column=0)

Button8 = Button(window,
                 text='8',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input8,
                 relief=RAISED,
                 bd=5)
Button8.grid(row=3,column=1)

Button9 = Button(window,
                 text='9',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input9,
                 relief=RAISED,
                 bd=5)
Button9.grid(row=3,column=2)

Button0 = Button(window,
                 text='0',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=input0,
                 relief=RAISED,
                 bd=5)
Button0.grid(row=4,column=1)

Dot = Button(window,
                 text='.',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=inputDot,
                 relief=RAISED,
                 bd=5)
Dot.grid(row=5,column=3)

Plus_Button = Button(window,
                 text='+',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=Plus,
                 relief=RAISED,
                 bd=5)
Plus_Button.grid(row=1,column=3)

Sub_Button = Button(window,
                 text='-',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=Subtract,
                 relief=RAISED,
                 bd=5)
Sub_Button.grid(row=2,column=3)

Mtp_Button = Button(window,
                 text='*',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=Mtp,
                 relief=RAISED,
                 bd=5)
Mtp_Button.grid(row=3,column=3)

Dvd_Button = Button(window,
                 text='/',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=Dvd,
                 relief=RAISED,
                 bd=5)
Dvd_Button.grid(row=4,column=3)

Evaluate_Button = Button(window,
                 text='=',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=Evaluate,
                 relief=RAISED,
                 bd=5)
Evaluate_Button.grid(row=4,column=2)

Delete_Button = Button(window,
                 text='Del',
                 font=('Futura',20,'bold'),
                 width=4,
                 height=2,
                 command=Delete,
                 relief=RAISED,
                 bd=5)
Delete_Button.grid(row=4,column=0)

Clear_Button = Button(window,
                 text='Clear',
                 font=('Futura',20,'bold'),
                 height=2,
                 width=14,
                 command=Clear,
                 relief=RAISED,
                 bd=5)
Clear_Button.grid(row=5,column=0,columnspan=3)


window.mainloop()