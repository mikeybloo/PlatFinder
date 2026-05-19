from colorama import Fore
import psutil
import keyboard
import os
import threading
import time

def main():
    while(True):
        if "Warframe.x64.exe" in (i.name() for i in psutil.process_iter()):
            print(Fore.GREEN + "Warframe is running!" + Fore.RESET)
        else:
            print(Fore.RED + "Warframe is not running!" + Fore.RESET)

        time.sleep(2)

def keyManager():
    while True:
        if keyboard.is_pressed("shift+F12"):
            print(Fore.CYAN + "Program exited!" + Fore.RESET)
            os._exit(1)
        

print(Fore.BLUE + r"__________.__          __ ___________.__            .___            ") 
print(Fore.BLUE + r"\______   \  | _____ _/  |\_   _____/|__| ____    __| _/___________ ") 
print(Fore.BLUE + r" |     ___/  | \__  \\   __\    __)  |  |/    \  / __ |/ __ \_  __ \\") 
print(Fore.BLUE + r" |    |   |  |__/ __ \|  | |     \   |  |   |  \/ /_/ \  ___/|  | \/") 
print(Fore.BLUE + r" |____|   |____(____  /__| \___  /   |__|___|  /\____ |\___  >__|   ") 
print(Fore.BLUE + r"                    \/         \/            \/      \/    \/       ")
print(Fore.RESET)
print(Fore.GREEN + "PlatFinder is running... \n" + Fore.RED + "Press shift+F12 to close the program")
print(Fore.RESET)

thread2 = threading.Thread(target=keyManager)
thread2.start()
main()