import mss as MSS
import pygetwindow
from colorama import Fore
import threading
import numpy as np
import cv2
import time
from warframeDetector import getWarframeWindow
from scanning import scanScreenshot
from pathlib import Path

def toggleScreenshotting(appState):
    activeWindow = pygetwindow.getActiveWindow()

    if "Warframe" not in activeWindow.title:
        print("Warframe is not focused!!")
        return

    if appState.isRunning and not appState.screenshottingEnabled:
        appState.screenshottingEnabled = True
        print(Fore.CYAN + "Screenshotting enabled!" + Fore.RESET)

        thread = threading.Thread(target=screenshotting, args=(appState,), daemon=True)
        thread.start()
    elif appState.isRunning and appState.screenshottingEnabled:
        appState.screenshottingEnabled = False
        print(Fore.CYAN + "Screenshotting disabled!" + Fore.RESET)

def screenshotting(appState):
    ROOT_PATH = Path(__file__).resolve().parent.parent
    appState.screenshottingEnabled

    while appState.isRunning and appState.screenshottingEnabled:
        with MSS.mss() as sct:
            window = getWarframeWindow()
            screenshotParameters = {
                "top": window.top,
                "left": window.left,
                "width": window.width,
                "height": window.height
            }

            #print(screenshotParameters)
            
            screenshot = sct.grab(screenshotParameters)
            fileName = "screenshot.png"

            img = np.array(screenshot)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            crop = img[380:480, 400:1520]

            scanScreenshot(appState, crop)

            #cv2.imwrite(f"{ROOT_PATH}/screenshots/{fileName}", crop)
            #print(f"Saved to: {fileName}")
            
        time.sleep(1)