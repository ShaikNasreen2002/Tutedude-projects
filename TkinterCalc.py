import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("500x500")
window.title("Calculator")
e= Entry(window , width=56 , borderwidth=5)
e.place(x=0, y=0)
def click(num):
    res = e.get()
    e.delete(0,tk.END)
    e.insert(tk.END,(str(res)+str(num)))
btn1 = tk.Button(window , text='1' ,width=12, command= lambda t='1' :click(t))
btn1.place(x=10, y=60)
btn1 = tk.Button(window , text='2' ,width=12, command= lambda t='2' :click(t))
btn1.place(x=80, y=60)
btn1 = tk.Button(window , text='3' , width=12, command= lambda t='3' :click(t))
btn1.place(x=170, y=60)
btn1 = tk.Button(window , text='4' , width=12, command= lambda t='4' :click(t))
btn1.place(x=10, y=120)
btn1 = tk.Button(window , text='5' , width=12, command= lambda t='5' :click(t))
btn1.place(x=80, y=120)
btn1 = tk.Button(window , text='6' , width=12, command= lambda t='6' :click(t))
btn1.place(x=170, y=120)
btn1 = tk.Button(window , text='7' , width=12, command= lambda t='7' :click(t))
btn1.place(x=10, y=180)
btn1 = tk.Button(window , text='8' , width=12, command= lambda t='8' :click(t))
btn1.place(x=80, y=180)
btn1 = tk.Button(window , text='9' , width=12, command= lambda t='9' :click(t))
btn1.place(x=170, y=180)
btn1 = tk.Button(window , text='0' , width=12, command= lambda t='0' :click(t))
btn1.place(x=10, y=240)

btn1 = tk.Button(window , text='+' , width=12, command= lambda t='+' :click(t))
btn1.place(x=80, y=240)

btn1 = tk.Button(window , text='-' , width=12, command= lambda t='-' :click(t))
btn1.place(x=170, y=240)


btn1 = tk.Button(window , text='/' , width=12, command= lambda t='/' :click(t))
btn1.place(x=10, y=300)


btn1 = tk.Button(window , text='*' , width=12, command= lambda t='*' :click(t))
btn1.place(x=80, y=300)
def clearing():
    e.delete(0,tk.END)
btn1 = tk.Button(window , text='clear' , width=12, command= clearing)
btn1.place(x=170, y=300)

def total():
    expression = e.get()
    print("Expression:", expression)  # Add this line for debugging
    e.delete(0, END)
    try:
        result = eval(expression)
        print("Result:", result)  # Add this line for debugging
        e.insert(0, str(result))
    except Exception as ex:
        print("Error:", ex)  # Add this line for debugging
        e.insert(0, "Error: Invalid Expression")


btn1 = tk.Button(window , text = '=' , width=12, command= total)
btn1.place(x=10, y=360)
window.mainloop()