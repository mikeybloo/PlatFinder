from colorama import Fore
from mss import MSS
import mss.tools
import psutil
import keyboard
import os
import threading
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

def toggleScreenshotting():
    global isRunning
    global screenshottingEnabled

    if isRunning and not screenshottingEnabled:
        screenshottingEnabled = True
        print(Fore.CYAN + "Screenshotting enabled!" + Fore.RESET)
        threading.Thread(target=screenshotting).start()
    elif isRunning and screenshottingEnabled:
        screenshottingEnabled = False
        print(Fore.CYAN + "Screenshotting disabled!" + Fore.RESET)

def screenshotting():
    global isRunning
    global screenshottingEnabled

    if isRunning and screenshottingEnabled:
        with MSS() as sct:
            monitor = sct.monitors[2]
            screenshot = sct.grab(monitor)
            fileName = "screenshot.png"

            mss.tools.to_png(screenshot.rgb, screenshot.size, output=fileName)
            print(fileName)

    elif isRunning and not screenshottingEnabled:
        exit()

    time.sleep(1)

def exitProgram():
    print(Fore.CYAN + "Program exited!" + Fore.RESET)
    os._exit(1)
        
keyboard.add_hotkey("shift+f12", exitProgram)
keyboard.add_hotkey("shift+space", toggleScreenshotting)

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