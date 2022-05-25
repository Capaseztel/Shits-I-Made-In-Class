from click import secho
import keyboard
import time
import os

text = str(input("number of the text (text'x') >>  "))

txt = str(open("text" + text,"r").read())
sec = float(input("seconds beetween lines (separate by '.') >>   "))

format = txt.replace("í","i")
format = format.replace("Í","I")
format = format.replace("á","a")
format = format.replace("Á","A")
format = format.replace("é","e")
format = format.replace("É","E")
format = format.replace("ó","o")
format = format.replace("Ó","O")
format = format.replace("ú","u")
format = format.replace("Ú","U")
format = format.replace("?","")
format = format.replace("¿","")
format = format.replace("!","")
format = format.replace("¡","")
format = format.replace(",","")
format = format.replace(")","")
format = format.replace("(","")
format = format.replace("«","")
format = format.replace("»","")
format = format.replace("\n"," ")

format = format.split(" ")
num =  len(format)
var = -1
os.system("clear")
print("charging.")
time.sleep(1)
os.system("clear")
print("charging..")
time.sleep(1)
os.system("clear")
print("charging...")
time.sleep(1)
os.system("clear")
print("Writing ^-^")

print("number of Words -> " + str(num))

while var < num:
    time.sleep(sec)
    keyboard.write(format[var].lower())
    keyboard.press_and_release("return")
    var = var + 1

print("\nFinished OwO")