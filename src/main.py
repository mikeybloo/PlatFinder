from colorama import Fore
import psutil
import keyboard
import sys
import time
import easyocr
import cv2

isRunning = False
screenshottingEnabled = False


class AppState:
    def __init__(self):
        self.isRunning = False
        self.screenshottingEnabled = False
        self.reader = None

def main(appState):
    while(True):
        if "Warframe.x64.exe" in (i.name() for i in psutil.process_iter()):
            appState.isRunning = True
            print(Fore.GREEN + "Warframe is running!" + Fore.RESET)
        else:
            appState.isRunning = False
            print(Fore.RED + "Warframe is not running!" + Fore.RESET)

        time.sleep(2)

def exitProgram():
    print(Fore.CYAN + "Program exited!" + Fore.RESET)
    sys.exit(0)

appState = AppState()
print(Fore.YELLOW + "Initializing easyOCR... \n" + Fore.RESET)
appState.reader = easyocr.Reader(['en'], gpu=False)

print(Fore.BLUE + r"__________.__          __ ___________.__            .___            ") 
print(Fore.BLUE + r"\______   \  | _____ _/  |\_   _____/|__| ____    __| _/___________ ") 
print(Fore.BLUE + r" |     ___/  | \__  \\   __\    __)  |  |/    \  / __ |/ __ \_  __ \\") 
print(Fore.BLUE + r" |    |   |  |__/ __ \|  | |     \   |  |   |  \/ /_/ \  ___/|  | \/") 
print(Fore.BLUE + r" |____|   |____(____  /__| \___  /   |__|___|  /\____ |\___  >__|   ") 
print(Fore.BLUE + r"                    \/         \/            \/      \/    \/       ")
print(Fore.RESET)
print(Fore.GREEN + "PlatFinder is RUNNING... \n" + Fore.CYAN + "Press shift+F5 to start scanning your drops\n" + Fore.RED + "Press shift+F12 to close the program" + Fore.RESET)

main(appState)