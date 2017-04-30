# HIDAAF

> ```
> __    __   __   _______       ___           ___       _______ 
> |  |  |  | |  | |       \     /   \         /   \     |   ____|
> |  |__|  | |  | |  .--.  |   /  ^  \       /  ^  \    |  |__   
> |   __   | |  | |  |  |  |  /  /_\  \     /  /_\  \   |   __|  
> |  |  |  | |  | |  '--'  | /  _____  \   /  _____  \  |  |     
> |__|  |__| |__| |_______/ /__/     \__\ /__/     \__\ |__| 
> ```
## Human Interface Device Android Attack Framework

HIDAAF is a python framework that makes it easy to generate HID attack scripts for the Android platform with corresponding phone models.
The HIDAAF output format is intended for the Bash Bunny (Provided by the great guys behind Hak5)
Due to the custom Android images released with certain phones (Like the Samsung Galaxy series) HIDAAF is heavily dependent on your contributions
to cover as many phone models as possible.!

Soon to be released!


Teaser: 


## How do i contribute ?


To submit a payload, simply make 2 files in the payload directory 


Example:
S7_Install_Backdoor 
 and  S7_Install_Backdoor_Raw

The S7_Install_Backdoor_Raw file is the actual bash bunny payload 
it can contain 2 variables (currently) that the framework will ask to replace
#SOURCES# and #APKNAME# , there will be added more

The 7_Install_Backdoor file is a XML style information file with the link to the raw file


	<data>
		<info>
			Target: Samsung S7 / S7 + running latest update. 
			Payload will enable unknown sources on the device and procces to download, install and run an APK of your choose.

			It uses ECM_Ethernet + HID in the bash bunny to host the APK file.
		</info>



		<payload>
			S8_Install_Backdoor_raw.txt
		</payload>
	</data>

Like so :)


