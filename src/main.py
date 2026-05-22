from colorama import Fore
from mapHotkeys import mapHotkeysToKeyboard
import psutil
import keyboard
import time
import easyocr
from appState import AppState
from utility import title

def main(appState):
    while(True):
        if "Warframe.x64.exe" in (i.name() for i in psutil.process_iter()):
            appState.isWarframeRunning = True
            print(Fore.GREEN + "Game detected! Press shift+F5 to scan your drops when they appear on the screen." + Fore.RESET)
        else:
            appState.isWarframeRunning = False
            print(Fore.RED + "Warframe is not running! Please run the game to use this tool" + Fore.RESET)

        time.sleep(10)
        
appState = AppState()

print(Fore.YELLOW + "Initializing easyOCR..." + Fore.RESET)
appState.reader = easyocr.Reader(['en'], gpu=False)

mapHotkeysToKeyboard(appState)
appState.screenshotThread.start()

title()

print(Fore.GREEN + "PlatFinder is RUNNING... \n" + Fore.CYAN + "Press shift+F5 to start scanning your drops\n" + Fore.RED + "Press shift+F12 to close the program" + Fore.RESET)

main(appState)