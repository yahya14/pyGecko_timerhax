#from tcpgecko import TCPGecko

print("""Please  launch into a recon stage before you begin.""")
	
raw_input("Press ENTER to continue.")
	
tcp = TCPGecko(ip)
print("""\n""")


amiibo_timer = True
while amiibo_timer:
	#amiibo_timer_addr = int(hexlify(tcp.readmem(0x1CAB476C, 4)), 16) + int(0x2B4)
	amiibo_timer_addr = int(hexlify(tcp.readmem(0x1CAB5778, 4)), 16) + int(0x2B4)
	
	print("""Please set time value in seconds. Anything over 180 s to 240 s (depending on the stage) will make the time freeze.\nType 0 to return to the menu.""")
	try:
		amiibo_timer = int(input(">> "))
		amiibo_timer_poke = amiibo_timer * 60
	except ValueError:
		print("Please use a whole number.")
		time.sleep(2)
        
	if amiibo_timer <= 71582780:
		if amiibo_timer < 0:
			print("Number too low.")
			time.sleep(1.5)
			os.system("cls")
			amiibo_timer = True
		elif amiibo_timer == 0:
			amiibo_timer = False
			tcp.s.close()
			print("returning to menu.")
			time.sleep(1.5)
		else:
			tcp.pokemem(amiibo_timer_addr, amiibo_timer_poke)
			print("Poked timer to %s seconds!" %(amiibo_timer))
			amiibo_timer = False
			tcp.s.close()
			time.sleep(1.5)
			
	else:
		print("Number too high.")
		time.sleep(1.5)
		os.system("cls")
		

