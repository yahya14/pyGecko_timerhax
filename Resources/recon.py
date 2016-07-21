#from tcpgecko import TCPGecko
absolutely_unused_variable = os.system("cls")

print("""Please  launch into a recon stage before you begin.""")
    
raw_input("Press ENTER to continue.")
    
tcp = TCPGecko(ip)
print("\n")

recon_timer = True
while recon_timer:
    #recon_timer_addr = int(hexlify(tcp.readmem(0x1CAA913C, 4)), 16) + int(0x280) 2.8.0
    recon_timer_addr = int(hexlify(tcp.readmem(0x1CAAA144, 4)), 16) + int(0x280)
    
    print("""Please set time value in seconds. 71582788 s is the maximum.\n\n<0> to set the maximum time.\n<RETURN> to return to the menu.\n\n""")
    try:
        recon_timer = raw_input(">> ")
        recon_timer = recon_timer or -1
        recon_timer_poke = int(recon_timer) * 60
    except ValueError:
        print("Please use a whole number.")
        time.sleep(1.5)
        os.system("cls")
        continue
    recon_timer = int(recon_timer)
    if recon_timer <= 71582788:
        if recon_timer < -1:
            print("Number too low.")
            time.sleep(1.5)
            os.system("cls")
            time.sleep(1)
        elif recon_timer == -1:
            recon_timer = False
            tcp.s.close()
            print("returning to menu.")
            time.sleep(1)
        elif recon_timer == 0:
            tcp.pokemem(recon_timer_addr, 0xFFFFFFFE)
            print("Poked timer to 71582788 seconds!")
            recon_timer = False
            tcp.s.close()
            time.sleep(1)
        else:
            tcp.pokemem(recon_timer_addr, recon_timer_poke)
            print("Poked timer to %s seconds!" %(recon_timer))
            recon_timer = False
            tcp.s.close()
            time.sleep(1)
            
    else:
        print("Number too high.")
        time.sleep(1)
        os.system("cls")



#old embarrasing code, 
'''
while recon_timer:
    os.system("cls")
    
    #tcp = TCPGecko(ip)
    
    print("""Starting...\n\nYou first have to launch into a recon stage before you begin.""")
    
    raw_input("Press ENTER to continue.")
    
    recon_timer_addr = int(hexlify(tcp.readmem(0x1CAA913C, 4)), 16) + int(0x280)
    
    print("""\nInput the time in seconds""")
    
    recon_timer = raw_input(">> ")
    
    tcp.pokemem(recon_timer_addr, recon_timer)
    
    print "Success!"
    time.sleep(1.6)  # Delay for 3 seconds

    #tcp.s.close()
'''

