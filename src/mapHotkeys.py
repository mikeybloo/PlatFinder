import keyboard
import os
from screenshotting import toggleScreenshotting
from colorama import Fore

def exitProgram():
    print(Fore.CYAN + "Program exited!" + Fore.RESET)
    os._exit(0)

def mapHotkeysToKeyboard():
    keyboard.add_hotkey("shift+f12", exitProgram)
    keyboard.add_hotkey("shift+f5", toggleScreenshotting)