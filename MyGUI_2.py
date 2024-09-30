from gc import disable
from textwrap import wrap
import tkinter as tk
from tkinter import Label, ttk
from turtle import color, width
from tkinter import scrolledtext
from tkinter import Menu



from nltk.app.nemo_app import colors
from pyarrow.ipc import new_file

win = tk.Tk()
win.title('MyPynthon GUI')
''
win.resizable(0,0)

monty = ttk.Labelframe(win, text="ElyBillz-Globe ")
monty.grid(column=0, row=0, padx=20, pady=40)


label = ttk.Label(monty, text="Search : ")
label.grid(column=0, row=0,)


#  Modify Button click Function  << >>

def clickme():
    action.configure(text=' Not Found!!' + name.get() + ' ' + numEnter.get())


# Changing our Label  << >>

ttk.Label(monty, text='Search: ', foreground='blue').grid(column=0, row=1)

# Adding TextBox Widgets << >>

name = tk.StringVar()
nameEnter = ttk.Entry(monty, width=12, textvariable=name)
nameEnter.grid(column=0, row=1, padx=8, pady=4)

# Adding Buttons << >>

action = ttk.Button(monty, text='Enter ', command=clickme)
action.grid(column=2, row=1, sticky='WE')
nameEnter.focus()
# action.configure(state='disable')


# Adding TextBox Widgets << >>

ttk.Label(monty, text='Select number :').grid(column=1, row=0)
num = tk.StringVar()
numEnter = ttk.Combobox(monty, width=12, textvariable=num, state='readonly')
numEnter['value'] = (1, 2, 45, 70, 1006, 120, 200, 243, 290)
numEnter.grid(column=1, row=1)
numEnter.current()

# Creating Three Checkbuttons  << >>

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, padx=20, pady=10, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, padx=20, pady=10, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, padx=20, pady=10, sticky=tk.W)



# Creating RadioButton Global call << >>

Colors = ["Blue", "Red", "Green", "Lightgray"]

# RadioButton CallBack << >>
def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background=Colors[0])
    elif radSel == 1: win.configure(background=Colors[1])
    elif radSel == 2: win.configure(background=Colors[2])
    elif radSel == 3: win.configure(background=Colors[3])

    # Three RadioButton Using One Variable << >>


radVar = tk.IntVar()

radVar.set(99)

for col in range (4):
    curRad = "rad" + str(col)
    curRad= tk.Radiobutton(monty, text=Colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, padx=20, pady=30, sticky=tk.W)


# Creating ScrolledText Control << >>

scrolW = 30
scrolH = 3

src = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
src.grid(column=0, columnspan=6, padx=10, pady=6, sticky='WE')

# create a container to hold labels << >>

labelsframe = ttk.Labelframe(win, text='Label in a frame')
labelsframe.grid(column=0, row=12, sticky=tk.W,  padx=20, pady=30 )

# place labels into the container elements  << >>

ttk.Label(labelsframe, text='Label 1').grid(column=0, row =0, sticky=tk.W)
ttk.Label(labelsframe, text='Label 2').grid(column=0, row =1, sticky=tk.W)
ttk.Label(labelsframe, text='Label 3').grid(column=0, row =2, sticky=tk.W)

# Add Spacing to it << >>

for child in labelsframe.winfo_children():
    child.grid_configure(padx=10, pady=6)


def quit():
    win.quit()
    win.destroy()
    win.exit()


# create a Menu bar << >>

menuBar = Menu(win)
win.config(menu=menuBar)

# Add Menu Items << >>

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Exit", command=exit)
menuBar.add_cascade(label="Close Win ", menu=fileMenu)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Services ")
fileMenu.add_separator()
fileMenu.add_command(label="Products ")
menuBar.add_cascade(label="About ", menu=fileMenu)


tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab1')
tabControl.pack(expand=1, fill="both")


win.mainloop()





