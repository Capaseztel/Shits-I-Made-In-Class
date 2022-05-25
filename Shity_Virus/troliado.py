import os
import requests
import shutil
import getpass
import time

user = getpass.getuser()
image_url1 = "https://i.ytimg.com/vi/R0lqowYD_Tg/maxresdefault.jpg"
filename1 = image_url1.split("/")[-1]
image_url2 = "https://www.nationalgeographic.com.es/medio/2018/02/27/monos__1280x720.jpg"
filename2 = image_url2.split("/")[-1]
r1 = requests.get(image_url1, stream = True)
r2 = requests.get(image_url2, stream = True)
if r1.status_code == 200:
    r1.raw.decode_content = True
    with open(filename1,'wb') as f:
        shutil.copyfileobj(r1.raw, f)
    os.system("mv " + filename1 + " /home/" + user + "/Imágenes/")
    os.system("eog /home/" + user + "/Imágenes/" + filename1 + " &")
else:
    print("error = 1")
if r2.status_code == 200:
    r2.raw.decode_content = True
    with open(filename2,'wb') as f:
        shutil.copyfileobj(r2.raw, f)
        os.system("mv " + filename2 + " /home/" + user + "/Imágenes/")
    while True:
        os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/" + user + "/Imágenes/" + filename2)
        eogop = str(os.popen("ps -e | grep -o eog").read())
        if eogop != "eog\n":
            os.system("eog /home/" + user + "/Imágenes/" + filename1 + " &")
            time.sleep(2)
        else:
            pass
else:
    print("error = 2")