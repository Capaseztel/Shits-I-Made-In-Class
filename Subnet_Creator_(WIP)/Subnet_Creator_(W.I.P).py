## Subnet creator
## Author: Capaseztell (Github.com/Capaseztel)
## Version: 0.1 (Alpha)
## Date: 2023-20-01

import math
import re
import os

# clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# get the first IP address and the number of hosts
startIP = input("Enter the first IP address: ").split(".")
hosts = int(input("Enter the number of hosts: "))

# Convert the IP address to binary
binIP = [bin(int(x))[2:].zfill(8) for x in startIP]
print(f'\ngiven ip in binary: {".".join(binIP)}')

# find the subnet mask for the given number of hosts
mask = 32 - int(math.log(hosts, 2))
print(f'\nsimplified mask: {mask}')
# convert the mask to binary
binMask = re.findall("........", str("1"*mask + "0"*(32-mask)))
print(f'\nbinary mask: {".".join(binMask)}')
# convert the mask to decimal
decMask = [str(int(x, 2)) for x in binMask]
print(f'\ndecimal mask: {".".join(decMask)}')

# aproximate hosts to the nearest power of 2
range = 2**(hosts-1).bit_length()
