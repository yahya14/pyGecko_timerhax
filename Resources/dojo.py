#from tcpgecko import TCPGecko


dojo_timer = True
while dojo_timer:
	absolutely_unused_variable = os.system("cls")
	print("""Please  launch into a dojo stage before you begin.""")
	
	raw_input("Press ENTER to continue.")
	
	tcp = TCPGecko(ip)
	print("""\n""")
	
	dojo_timer_addr = int(hexlify(tcp.readmem(0x1CAAA218, 4)), 16) + int(0x280)
	
	
	print("""Please set time value in seconds. Anything over 6039 s will make the time freeze. \nType 0 to return to the menu.""")
	try:
		dojo_timer = int(input(">> "))
		dojo_timer_poke = dojo_timer * 60
	except ValueError:
		print("Please use a whole number.")
		time.sleep(2)
        
	if dojo_timer <= 71582780:
		if dojo_timer < 0:
			print("Number too low.")
			time.sleep(1.5)
			dojo_timer = True
		elif dojo_timer == 0:
			dojo_timer = False
			tcp.s.close()
			print("returning to menu.")
			time.sleep(1.5)
		else:
			tcp.pokemem(dojo_timer_addr, dojo_timer_poke)
			print("Poked timer to %s seconds!" %(dojo_timer))
			dojo_timer = False
			tcp.s.close()
			time.sleep(1.5)
			
	else:
		print("Number too high.")
		time.sleep(1.5)

