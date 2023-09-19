import os
import getpass

user = getpass.getuser()
print("user = " + user)
os.system("cd Imágenes && wget --output-document=pikmin.jpg https://i.ytimg.com/vi/ppYx1kaji5w/maxresdefault.jpg")
os.system(f"gsettings get org.gnome.desktop.background picture-uri file:///home/{user}/Imágenes/pikmin.jpg")