from tkinter import *

root = Tk()
root.geometry('500x500')

def drag_start(event):
    global widget, xstart,ystart
    widget = event.widget
    xstart = event.x
    ystart = event.y
    
def drag_motion(event):
    widget.place(x=widget.winfo_x()+event.x-xstart,y=widget.winfo_y()+event.y-ystart)

label = Label(root,bg='red',width=10,height=5)
label.place(x=0,y=0)
label2 = Label(root,bg='blue',width=10,height=5)
label2.place(x=200,y=200)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)





root.mainloop()