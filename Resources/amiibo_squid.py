#from tcpgecko import TCPGecko
absolutely_unused_variable = os.system("cls")

print("""Please  launch into a recon stage before you begin.""")
    
raw_input("Press ENTER to continue.")
    
tcp = TCPGecko(ip)
print("\n")

amiibo_timer = True
while amiibo_timer:
    #amiibo_timer_addr = int(hexlify(tcp.readmem(0x1CAB476C, 4)), 16) + int(0x2B4)
    amiibo_timer_addr = int(hexlify(tcp.readmem(0x1CAB5778, 4)), 16) + int(0x2B4)
    
    print("""Please set time value in seconds. 71582788 s is the maximum.\n\n<0> to set the maximum time.\n<RETURN> to return to the menu.\n\n""")
    try:
        amiibo_timer = raw_input(">> ")
        amiibo_timer = amiibo_timer or -1
        amiibo_timer_poke = int(amiibo_timer) * 60
    except ValueError:
        print("Please use a whole number.")
        os.system("cls")
        time.sleep(1.5)
        continue
    amiibo_timer = int(amiibo_timer)
    if amiibo_timer <= 71582788:
        if amiibo_timer < -1:
            print("Number too low.")
            time.sleep(1.5)
            os.system("cls")
            amiibo_timer = True
        elif amiibo_timer == -1:
            amiibo_timer = False
            tcp.s.close()
            print("returning to menu.")
            time.sleep(1)
        elif amiibo_timer == -0:
            tcp.pokemem(amiibo_timer_addr, 0xFFFFFFFE)
            print("Poked timer to 71582788 seconds!")
            amiibo_timer = False
            tcp.s.close()
            time.sleep(1)
        else:
            tcp.pokemem(amiibo_timer_addr, amiibo_timer_poke)
            print("Poked timer to %s seconds!" %(amiibo_timer))
            amiibo_timer = False
            tcp.s.close()
            time.sleep(1)
            
    else:
        print("Number too high.")
        time.sleep(1.5)
        os.system("cls")
        

