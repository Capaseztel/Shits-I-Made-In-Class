import os
import getpass

user = getpass.getuser()
print("user = " + user)
os.system("cd Imágenes && wget --output-document=pikmin.jpg https://pbs.twimg.com/media/EYzIYbcXgAAf3Gp.jpg")
os.system(f"gsettings set org.gnome.desktop.background picture-uri file:///home/{user}/Imágenes/pikmin.jpg")