from tkinter import *
from tkinter import filedialog,colorchooser,font

def Open():
    filepath = filedialog.askopenfilename(title='Open your txt file',
                                          filetypes=(("Text Files", "*.txt"),))
    Maint_Text_Area.insert('1.0',open(filepath,'r').read())

def Save():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text File",".txt"),
                                               ("HTML File",".txt")])
    if file is None:
        return
    Text = Maint_Text_Area.get(1.0,END)
    file.write(Text)
    pass

def Copy():
    Copied_Text = ''

def Cut():
    pass

def Paste():
    pass

def SelALL():
    Maint_Text_Area.tag_add(SEL, "1.0", END)
    Maint_Text_Area.mark_set(INSERT, "1.0")
    Maint_Text_Area.see(INSERT)
    return 'break'

def Information():
    Information_window = Toplevel()
    Information_label = Label(Information_window,
                              text='This program was created by Rabii on the 16th of august 2023 :)',
                              font=('Times',20),
                              width=80,
                              height=5).pack()
    
def ColorChooser():
    color = colorchooser.askcolor()
    Maint_Text_Area.config(fg=color[1])
    window.update()

def FontChooser():
    print(font.families(root=None, displayof=None))

window = Tk()
window.geometry("500x500")
window.title("Rabii's text editor")

menubar = Menu(window,)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
editMenu = Menu(menubar,tearoff=0)
helpMenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label="File",menu=fileMenu)
menubar.add_cascade(label='Edit',menu=editMenu)
menubar.add_cascade(label='Help',menu=helpMenu)

fileMenu.add_command(label='Open',command=Open)
fileMenu.add_command(label='Save',command=Save)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

editMenu.add_command(label='Copy',command=Copy)
editMenu.add_command(label='Paste',command=Paste)
editMenu.add_command(label='Cut',command=Cut)
editMenu.add_command(label='Select All',command=SelALL)

helpMenu.add_command(label='About',command=Information)

Maint_Text_Area = Text(window,
                       fg="#A2AD91",
                       bg="#3A2D32",
                       relief=RAISED,
                       bd=10,
                       width=32,
                       height=13,
                       font=('Times',20))
Maint_Text_Area.pack()

button_frame = Frame(window,
                     width=400,
                     height=200,)
button_frame.pack()

ColorChooser_Button = Button(button_frame,
                             font=('Times',15),
                             width=10,
                             height=2,
                             text='Color',
                             relief=RAISED,
                             bd=5,
                             command=ColorChooser
                             )
ColorChooser_Button.grid(row=0,column=0)

FontChooser_Button = Button(button_frame,
                             font=('Times',15),
                             width=10,
                             height=2,
                             text='Font',
                             relief=RAISED,
                             bd=5,
                             command=FontChooser
                             )
FontChooser_Button.grid(row=0,column=1)

Size_Button = Button(button_frame,
                             font=('Times',15),
                             width=10,
                             height=2,
                             text='Size',
                             relief=RAISED,
                             bd=5
                             )
Size_Button.grid(row=0,column=2)

window.mainloop()