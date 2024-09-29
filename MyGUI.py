
from gc import disable
from textwrap import wrap
import tkinter as tk
from tkinter import Label, ttk
from turtle import color, width
from tkinter import scrolledtext



win = tk.Tk()
win.title('MyPynthon GUI')
''
win.resizable(0,0)
label = ttk.Label(win, text="labael ")
label.grid(column=0, row=0)

#  Modify Button click Function  << >>

def clickme():
    action.configure( text=' Not Found!!'  + name.get() +' ' + numEnter.get())


# Changing our Label  << >>

ttk.Label(win, text='Search:', foreground='blue').grid(column=0, row=0)

# Adding TextBox Widgets << >>

name = tk.StringVar()
nameEnter = ttk.Entry(win, width=12, textvariable=name)
nameEnter.grid(column=0, row=1)

# Adding Buttons << >>

action = ttk.Button(win, text='Enter ', command=clickme)
action.grid(column=4, row=1)
nameEnter.focus()
# action.configure(state='disable')


# Adding TextBox Widgets << >>

ttk.Label(win, text='Select number :').grid(column=1, row=0)
num = tk.StringVar()
numEnter = ttk.Combobox(win, width=12, textvariable=num, state='readonly')
numEnter['value'] = (1, 2, 45, 70, 1006, 120, 200, 243, 290)
numEnter.grid(column=1, row=1)
numEnter.current()

# Creating Three Checkbuttons  << >>

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Creating RadioButton Global call << >>

Color1 = "blue"
Color2 = "red"
Color3 = "green"


# RadioButton CallBack << >>
def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=Color1)
    elif radSel == 2:
        win.configure(background=Color2)
    elif radSel == 3:
        win.configure(background=Color3)

    # Three RadioButton Using One Variable << >>


radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=Color1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=Color2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=Color3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

# Creating ScrolledText Control << >>

scrolW = 30
scrolH = 3

src = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
src.grid(column=0, columnspan=3)

win.mainloop()





