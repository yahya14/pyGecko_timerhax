os.system('cls')
print("Please type in your new IP address.\n")
fresh_ip = raw_input(">> ")
save = open("./Resources/save_ip.txt", "w")
save.write(fresh_ip)
save.close()
ip = fresh_ip
print("Your Wii U IP has been updated!")
time.sleep(2)

execfile("./Resources/menu.py")