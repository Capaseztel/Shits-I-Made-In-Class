import builtins
from tkinter import *
from typing import Collection
ventana = Tk()
ventana.title("Calculadora")
ventana.resizable(False, False)

#variables
mult = 0 #multiplicacion
div = 0 #division
mas = 0 #Suma

#pantalla
out = Entry(ventana, width=15, font = ("Calibri 20"))
out.grid(column= 0, row= 0, columnspan= 4)

#funciones
def wr1():
    out.insert("end", 1)

def wr2():
    out.insert("end", 2)

def wr3():
    out.insert("end", 3)

def wr4():
    out.insert("end", 4)

def wr5():
    out.insert("end", 5)

def wr6():
    out.insert("end", 6)

def wr7():
    out.insert("end", 7)

def wr8():
    out.insert("end", 8)

def wr9():
    out.insert("end", 9)

def wr0():
    out.insert("end", 0)

def wrmas():
    global mas
    mas = int(out.get())
    out.delete(0, "end")

def wrmult():
    global mult
    mult = int(out.get())
    out.delete(0, "end")

def wrdiv():
    global div
    div = int(out.get())
    out.delete(0, "end")

def wrrest():
	global rest
	rest = int(out.get())
	out.delete(0, "end")

def wrigu():
    Y = int(out.get())
    global mas
    global mult
    global div
    global rest
    if mas >= 1:
        sol = mas + Y
    elif mult >= 1:
        sol = mult * Y
    elif div >= 1:
        sol = div / Y
    elif rest >= 1:
        sol = rest - Y
    out.delete(0, "end")
    out.insert(0, sol)
    mas = 0
    mult = 0
    div = 0
    rest = 0

def erase():
    out.delete(0, "end")

#Botones
boton1 = Button(ventana,text=("1") ,width= 5, height= 2, command= wr1)
boton2 = Button(ventana,text=("2") ,width= 5, height= 2, command= wr2)
boton3 = Button(ventana,text=("3") ,width= 5, height= 2, command= wr3)
boton4 = Button(ventana,text=("4") ,width= 5, height= 2, command= wr4)
boton5 = Button(ventana,text=("5") ,width= 5, height= 2, command= wr5)
boton6 = Button(ventana,text=("6") ,width= 5, height= 2, command= wr6)
boton7 = Button(ventana,text=("7") ,width= 5, height= 2, command= wr7)
boton8 = Button(ventana,text=("8") ,width= 5, height= 2, command= wr8)
boton9 = Button(ventana,text=("9") ,width= 5, height= 2, command= wr9)
boton0 = Button(ventana,text=("0") ,width= 5, height= 2, command= wr0)
boton_igual = Button(ventana, text=("="), width= 5, height= 2, command= wrigu)
boton_mas = Button (ventana, text=("+"), width= 5, height= 2, command= wrmas)
boton_mult = Button (ventana, text=("x"), width= 5, height= 2, command= wrmult)
boton_div = Button (ventana, text=("/"), width= 5, height= 2, command= wrdiv)
boton_erase = Button (ventana, text=("AC"), width= 5, height= 2, command= erase)
boton_rest = Button (ventana, text=("-"), width= 5, height= 2, command= wrrest)

#Imprimir botones
boton1.grid(column= 0, row= 1)
boton2.grid(column= 1, row= 1)
boton3.grid(column= 2, row= 1)
boton4.grid(column= 0, row= 2)
boton5.grid(column= 1, row= 2)
boton6.grid(column= 2, row= 2)
boton7.grid(column= 0, row= 3)
boton8.grid(column= 1, row= 3)
boton9.grid(column= 2, row= 3)
boton0.grid(column= 0, row= 4)
boton_mas.grid(column= 3, row= 3,)
boton_mult.grid(column= 3, row= 2)
boton_div.grid(column= 3, row= 1)
boton_erase.grid(column= 2, row= 4)
boton_igual.grid(column= 1, row= 4)
boton_rest.grid(column = 3, row = 4)

#firma
firma = Label(ventana, text= "Created by ||  Capaseztell  ||", bg= "deep sky blue")
firma.grid(column= 1, row= 5, columnspan=3)

ventana.mainloop()