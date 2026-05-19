from colorama import Fore
import psutil
import keyboard
import os
#import threading
import time

isRunning = False
screenshottingEnabled = False

def main():
    global isRunning
    while(True):
        if "Warframe.x64.exe" in (i.name() for i in psutil.process_iter()):
            isRunning = True
            print(Fore.GREEN + "Warframe is running!" + Fore.RESET)
        else:
            isRunning = False
            print(Fore.RED + "Warframe is not running!" + Fore.RESET)

        time.sleep(2)

def enableScreenshotting():
    global isRunning
    global screenshottingEnabled

    if isRunning:
        screenshottingEnabled = True
        print(Fore.CYAN + "Screenshotting enabled!" + Fore.RESET)
        
keyboard.add_hotkey("shift+f12", lambda: os._exit(1))
keyboard.add_hotkey("shift+space", enableScreenshotting)

print(Fore.BLUE + r"__________.__          __ ___________.__            .___            ") 
print(Fore.BLUE + r"\______   \  | _____ _/  |\_   _____/|__| ____    __| _/___________ ") 
print(Fore.BLUE + r" |     ___/  | \__  \\   __\    __)  |  |/    \  / __ |/ __ \_  __ \\") 
print(Fore.BLUE + r" |    |   |  |__/ __ \|  | |     \   |  |   |  \/ /_/ \  ___/|  | \/") 
print(Fore.BLUE + r" |____|   |____(____  /__| \___  /   |__|___|  /\____ |\___  >__|   ") 
print(Fore.BLUE + r"                    \/         \/            \/      \/    \/       ")
print(Fore.RESET)
print(Fore.GREEN + "PlatFinder is running... \n" + Fore.RED + "Press shift+F12 to close the program")
print(Fore.RESET)

main()