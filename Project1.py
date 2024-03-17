# Import the required libraries
from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("700x350")

var1=1;


def clear_cb():
    cb.set('')


thisdict = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40,
    "E": 50,
    "F": 60,
    "G": 70,
    "H": 80,
    "I": 90
}
diffValue = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9
}


def callback(*arg):
   for y in range(1):
       global disPlayedValue;
       disPlayedValue = (str)(var.get()).strip()
       v = thisdict.get(disPlayedValue)
       Label(win, text="The Selected Character is: " + disPlayedValue,
             font=('Helvetica 12')).pack()
       hb = ttk.Combobox(win, width=27, textvariable=var)
       hb['state'] = 'readonly'
       hb.pack(fill='x', padx=5, pady=5)
       global curr
       curr = diffValue.get(disPlayedValue)
       for x in range(20):
           hb['values'] = tuple(list(hb['values']) + [str(v + (x * diffValue.get(disPlayedValue)))])
       for x in range(20):
           hb['values'] = tuple(list(hb['values']) + [str(v - (x * diffValue.get(disPlayedValue)))])
       button.pack()

var = StringVar()
cb = ttk.Combobox(win, width=27, textvariable=var)
cb['state'] = 'readonly'
cb.pack(fill='x', padx=5, pady=5)

cb['values'] = (
    ' A',
    ' B',
    ' C',
    ' D',
    ' E',
    ' F',
    ' G',
    ' H',
    ' I'
)

var.trace('w', callback)

button = Button(win, text="Quit", command=quit)

def quit():
    win.destroy()
win.mainloop()
