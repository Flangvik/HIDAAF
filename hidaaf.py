import os

def Show_Menu():  
		print ("\n" * 100)
		print " __    __   __   _______       ___           ___       _______ "
		print "|  |  |  | |  | |       \     /   \         /   \     |   ____|"
		print "|  |__|  | |  | |  .--.  |   /  ^  \       /  ^  \    |  |__   "
		print "|   __   | |  | |  |  |  |  /  /_\  \     /  /_\  \   |   __| " 
		print "|  |  |  | |  | |  '--'  | /  _____  \   /  _____  \  |  |     "
		print "|__|  |__| |__| |_______/ /__/     \__\ /__/     \__\ |__|   "
		print "      Human Interface Device Android Attack Framework"
		print ""
		print ""
		print 30 * "-" , "MENU" , 30 * "-"
		print "1. Generate payload"
		print "2. Generate payload + APK (Metasploit)"
		print "3. Exit"
		print 67 * "-"

	
def Generate_Payload(payload):
		print ("\n" * 100)
		print "Selection : " , payload
		import xml.etree.ElementTree as ET
		payload_link = ET.parse("payloads/" + payload).getroot().find('payload').text
		print ET.parse("payloads/" + payload).getroot().find('info').text
		payload_link = payload_link.replace('\n','')
		
		dropper_name = raw_input("Please enter the name of your apk :")	
		unknown_sources = raw_input("Please translate 'Unknown sources' in your target Android langauage :")
		
		
		with open("payloads/" + payload_link, "rt") as fin:
			with open("output/payload.txt", "wt") as fout:
			
				for line in fin:
					line = line.replace('#APKNAME#', dropper_name)
					fout.write(line.replace('#SOURCES#', unknown_sources))	
		
		print "Payload written to output/payload.txt" 
		raw_input("Press any key to return to menu")
		loop=True  
		Show_Menu()
	
def List_Payloads():  
		print "Listing payloads"
		filenames = next(os.walk(os.getcwd()+ "/payloads"))[2]
		count = 1
		for payloads in filenames:
				if "raw" not in payloads:
						print "                 " ,count , " : ", payloads	
						count += 1
		payload = input("Payload?=> ")
		Generate_Payload(filenames[payload - 1 ])

	
	 
loop=True      
  
while loop:        
    Show_Menu()    
    choice = input("Do. Or do not. There is no try.")
     
    if choice==1:     
		List_Payloads()
		loop=False
		
    elif choice==2:
        print "Menu 2 has been selected"
        
    elif choice==3:
        loop=False 
    else:
        raw_input("Wrong option selection. Enter any key to try again..")

		
		
		
		
