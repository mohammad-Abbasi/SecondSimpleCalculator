import tkinter as tk

def f(x):
    if x == '.' and '.' in display.get():
        pass
    else:
        display.insert('end', x)

def g(x):
    global var1
    global last_opr
    if x in ('+', '-', '*', '/') and display.get() == '':
        pass
    else:
        last_opr = x
        var1 = float(display.get())
        display.delete(0, 1000)


def calculate():
    var2 = float(display.get())
    display.delete(0, 1000)
    if last_opr == '+':
        display.insert('end', var1 + var2)
    elif last_opr == '*':
        display.insert('end' , var1 * var2)
    elif last_opr == '-':
        display.insert('end' , var1 - var2)
    elif last_opr == '/':
        try:
            display.insert('end' , var1 / var2)
        except ZeroDivisionError:
            display.insert('end', 'operation is not possible')


root = tk.Tk()
root.title('Calculator')

config = {'width': 5, 'height': 3, 'bd': 1}
display = tk.Entry(width = 28)
display.grid(row = 0, column = 0, columnspan = 4)
tk.Button(root, text='7', command = lambda: f(7), **config).grid(row = 1, column = 0)
tk.Button(root, text='8', command = lambda: f(8), **config).grid(row = 1, column = 1)
tk.Button(root, text='9', command = lambda: f(9), **config).grid(row = 1, column = 2)
tk.Button(root, text='*', command = lambda: g('*'), **config).grid(row = 1, column = 3)
tk.Button(root, text='4', command = lambda: f(4), **config).grid(row = 2, column = 0)
tk.Button(root, text='5', command = lambda: f(5), **config).grid(row = 2, column = 1)
tk.Button(root, text='6', command = lambda: f(6), **config).grid(row = 2, column = 2)
tk.Button(root, text='/', command = lambda: g('/'), **config).grid(row = 2, column = 3)
tk.Button(root, text='1', command = lambda: f(1), **config).grid(row = 3, column = 0)
tk.Button(root, text='2', command = lambda: f(2), **config).grid(row = 3, column = 1)
tk.Button(root, text='3', command = lambda: f(3), **config).grid(row = 3, column = 2)
tk.Button(root, text='-', command = lambda: g('-'), **config).grid(row = 3, column = 3)
tk.Button(root, text='.', command = lambda: f('.'), **config).grid(row = 4, column = 0)
tk.Button(root, text='0', command = lambda: f(0), **config).grid(row = 4, column = 1)
tk.Button(root, text='+', command = lambda: g('+'), **config).grid(row = 4, column = 2)
tk.Button(root, text='=', command = lambda: calculate(), **config).grid(row = 4, column = 3)



root.mainloop()