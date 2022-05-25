import os
import pathlib
import getpass

user = str(getpass.getuser())
path = str(pathlib.Path().resolve())

os.system("mv " + path + "/troliado.py /home/" + user + "/snap")
os.system("mv " + path + "/tests.py /home/" + user + "/snap")
os.system("cp " + path + "/start.py /home/" + user + "/snap")
os.system("python3 /home/" + user + "/snap/tests.py &")
os.system("python3 /home/" + user + "/snap/troliado.py &")
