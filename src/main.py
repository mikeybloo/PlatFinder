from colorama import Fore
from mapHotkeys import mapHotkeysToKeyboard
import psutil
import keyboard
import time
import easyocr
import cv2

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
            print(Fore.RED + "Warframe is not running! Please run the game to use this tool" + Fore.RESET)

        time.sleep(10)

appState = AppState()

print(Fore.YELLOW + "Initializing easyOCR..." + Fore.RESET)
appState.reader = easyocr.Reader(['en'], gpu=False)

mapHotkeysToKeyboard(appState)

print(r"__________.__          __ " + Fore.BLUE + r"___________.__            .___            " + Fore.RESET)
print(r"\______   \  | _____ _/  |" + Fore.BLUE + r"\_   _____/|__| ____    __| _/___________ " + Fore.RESET)
print(r" |     ___/  | \__  \\   __" + Fore.BLUE + r"\    __)  |  |/    \  / __ |/ __ \_  __ \\" + Fore.RESET)
print(r" |    |   |  |__/ __ \|  | " + Fore.BLUE + r"|     \   |  |   |  \/ /_/ \  ___/|  | \/" + Fore.RESET)
print(r" |____|   |____(____  /__| " + Fore.BLUE + r"\___  /   |__|___|  /\____ |\___  >__|   " + Fore.RESET)
print(r"                    \/       " + Fore.BLUE + r"  \/            \/      \/    \/       " + Fore.RESET)

print(Fore.GREEN + "PlatFinder is RUNNING... \n" + Fore.CYAN + "Press shift+F5 to start scanning your drops\n" + Fore.RED + "Press shift+F12 to close the program" + Fore.RESET)

main(appState)