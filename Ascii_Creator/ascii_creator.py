## Ascii art creator
## Author: Capaseztell (https://www.github.com/capaseztel)
## Date: 16/02/2023

import sys
from PIL import Image

# pass the image as command line argument
try:
    image_path = sys.argv[1]
except IndexError:
    print('''Please enter the image path as command line argument.\n
    Example: python3 ascii_creator.py ./image.jpg''')
    sys.exit()

img = Image.open(image_path)

# resize the image
width, height = img.size
aspect_ratio = height / width

# Ask user for with of ascii image
new_width = int(input("Enter width (Characters): "))

new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))
# new size of image
# print(img.size)

# convert image to greyscale format
img = img.convert("L")

pixels = img.getdata()

spacepoints = int(input("For transparent, you want to use spaces(1) or points(2)?\n>> "))
# replace each pixel with a character from array
if spacepoints == 1:
    chars = ["█", "▓", "▓", "▓", "▒", "▒", "░", "░", "░", "░", " ", " "]
elif spacepoints == 2:
    chars = ["█", "▓", "▓", "▓", "▒", "▒", "░", "░", "░", "░", ".", "."]
else:
    print("Invalid input")
    sys.exit()
new_pixels = [chars[pixel // 25] for pixel in pixels]
new_pixels = "".join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [
    new_pixels[index : index + new_width]
    for index in range(0, new_pixels_count, new_width)
]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

# write to a text file.
with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)