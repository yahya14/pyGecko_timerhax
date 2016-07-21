os.system('cls')
print("Please type in your new Wii U IP address. E.G [192.168.1.101] or [10.0.0.3]\n")
fresh_ip = raw_input(">> ")
save = open("./Resources/save_ip.txt", "w")
save.write(fresh_ip)
save.close()
ip = fresh_ip
print("Your Wii U IP has been updated!")
time.sleep(1.5)

execfile("./Resources/menu.py")
