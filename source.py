import pyautogui as pag
import time
import random
from colorama import Fore, Back, Style





renkler = [
        (Fore.RED),
        (Fore.MAGENTA),
        (Fore.CYAN),
        (Fore.YELLOW),
        (Fore.BLUE)
        ]





bannerler = [

("""
███▄ ▄███▓ ▒█████   ███▄    █ ▄▄▄█████▓ ██▀███  ▓█████ 
▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀ 
▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒███   
▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄ 
▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░  ▒██▒ ░ ░██▓ ▒██▒░▒████▒
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░
░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░    ░      ░▒ ░ ▒░ ░ ░  ░
░      ░   ░ ░ ░ ▒     ░   ░ ░   ░        ░░   ░    ░   
       ░       ░ ░           ░             ░        ░  ░
                                                        

        """),




(r""" 

 _______  _______  _       _________ _______  _______
(       )(  ___  )( (    /|\__   __/(  ____ )(  ____ \
| () () || (   ) ||  \  ( |   ) (   | (    )|| (    \/
| || || || |   | ||   \ | |   | |   | (____)|| (__
| |(_)| || |   | || (\ \) |   | |   |     __)|  __)
| |   | || |   | || | \   |   | |   | (\ (   | (
| )   ( || (___) || )  \  |   | |   | ) \ \__| (____/\
|/     \|(_______)|/    )_)   )_(   |/   \__/(_______/



""")

        ]



print(random.choice(renkler))
print(random.choice(bannerler))



print(Style.RESET_ALL)

print(random.choice(renkler))

yazi = input("Flood için cümle yazınız: ")

print(Style.RESET_ALL)
print(random.choice(renkler))
sayi = int(input("Kaç defa yazılacağını yazınız: "))
print(Style.RESET_ALL)
print(random.choice(renkler))
sure = int(input("Kaç saniyede flood atmasını istiyorsunuz \n (bekleme olmaması için 0 yazınız) \n : "))


i = int


i = sayi

while i > 0:
  pag.write(yazi)
  pag.press("enter")
  time.sleep(sure)
  i = i - 1
