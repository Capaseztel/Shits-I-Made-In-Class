import cv2
import os
import time

com = int(input("Que vas a hacer? \n\n1) Crear animación                       2) Usar animación ya hecha\n\n>> "))


if com == 1:
  ani_num = input("\nNumero de Animación >> ")
  print("animation nº" + str(ani_num))
  file = str(input("Nombre del video >> "))
  vidcap = cv2.VideoCapture(file)
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ' + str(count), success)
    count += 1
  os.system("rm -r animated/anim" + str(ani_num))
  os.system("mkdir animated/anim" + str(ani_num))
  os.system("mv frame* animated/anim" + str(ani_num))

elif com == 2:
  ani_num = input("\nNumero de Animación >> ")
  file_list = os.listdir("animated/anim" + str(ani_num))
  file_num = int(len(file_list))
  print(str(file_num) + " frames")
  count = 0
  path = os.path.abspath(os.getcwd())
  print("\n----------\n iniciado\n----------")
  while True:
    while count < file_num:
      time.sleep(0.02)
      os.system("gsettings set org.gnome.desktop.background picture-uri file://" + path + "/animated/anim" + str(ani_num) + "/frame" + str(count) + ".jpg")
      count = count + 1
    count = 0

else:
  print("eso no es una acción gilipollas")