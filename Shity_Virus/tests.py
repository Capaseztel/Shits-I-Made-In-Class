import os
import time

while True:
    os.system("xrandr -o right")
    os.system("xrandr -o inverted")
    os.system("xrandr -o left")
    os.system("xrandr -o normal")
    time.sleep(5)