#from tcpgecko import TCPGecko
absolutely_unused_variable = os.system("cls")

print("""Please launch into a recon stage before you begin.""")
    
raw_input("Press ENTER to continue.")
    
tcp = TCPGecko(ip)
print("\n")

recon_timer = True
while recon_timer:
    #recon_timer_addr = int(hexlify(tcp.readmem(0x1CAA913C, 4)), 16) + int(0x280) 2.8.0
    recon_timer_addr = int(hexlify(tcp.readmem(0x1CAAA144, 4)), 16) + int(0x280)
    
    print("""Please set time value in seconds. Timer will seem to freeze at values over 6039 s. \n\n<0> Set the maximum time at 71582788 s.\n<ENTER> Return to the menu.\n\n""")
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

