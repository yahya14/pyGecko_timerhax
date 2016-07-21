absolutely_unused_variable = os.system("cls")

print("""Please  launch into a recon stage before you begin.""")
    
raw_input("Press ENTER to continue.")
    
tcp = TCPGecko(ip)
print("\n")

dojo_timer = True
while dojo_timer:
    dojo_timer_addr = int(hexlify(tcp.readmem(0x1CAAA218, 4)), 16) + int(0x280)
    
    print("""Please set the time value in seconds. Timer will seem to freeze at values over 6039 s. \n\n<0> Set the maximum time at 71582788 s.\n<ENTER> Return to the menu.\n\n""")
    try:
        dojo_timer = raw_input(">> ")
        dojo_timer = dojo_timer or -1
        dojo_timer_poke = int(dojo_timer) * 60
    except ValueError:
        print("Please use a whole number.")
        time.sleep(1.5)
        os.system("cls")
        continue
    dojo_timer = int(dojo_timer)
    if dojo_timer <= 71582788:
        if dojo_timer < -1:
            print("Number too low.")
            time.sleep(1.5)
            os.system("cls")
            time.sleep(1)
        elif dojo_timer == -1:
            dojo_timer = False
            tcp.s.close()
            print("returning to menu.")
            time.sleep(1)
        elif dojo_timer == 0:
            tcp.pokemem(dojo_timer_addr, 0xFFFFFFFE)
            print("Poked timer to 71582788 seconds!")
            dojo_timer = False
            tcp.s.close()
            time.sleep(1)
        else:
            tcp.pokemem(dojo_timer_addr, dojo_timer_poke)
            print("Poked timer to %s seconds!" %(dojo_timer))
            dojo_timer = False
            tcp.s.close()
            time.sleep(1)
            
    else:
        print("Number too high.")
        time.sleep(1.5)
        os.system("cls")
