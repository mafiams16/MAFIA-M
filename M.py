import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/LcGBrnPS2KC3b1p7GFJqa4')
mafia=platform.architecture()[0]
if mafia=="32bit":
    #__import__("M2")
    os.system("clear")
    exit('\033[91;1m [•] Sorry Bro 32 Bit Devices Not Supported')
elif mafia=="64bit":
    __import__("M1")
