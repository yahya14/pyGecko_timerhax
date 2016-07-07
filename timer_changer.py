import os, sys, subprocess, time
from binascii import hexlify
from tcpgecko import TCPGecko

os.system('cls')

# check to see if setup has already been completed

if os.path.isfile("./Resources/save_ip.txt") == True:
    ip = open("./Resources/save_ip.txt", "r").read()
    

#Ask for the IP and save it to ip.txt to be read on next launch
else:
    print("""What is your Wii U's IP address? This will absolutely maximize time the next time you launch this hack, and you can totally change this later.
Example: 192.168.1.110\n""")
    fresh_ip = raw_input(">> ")
    save = open("./Resources/save_ip.txt", "w")
    save.write(fresh_ip)
    save.close()
    ip = fresh_ip



execfile("./Resources/menu.py")