import mss as MSS
import pygetwindow
from colorama import Fore
import numpy as np
import cv2
import time
from warframeDetector import getWarframeWindow
from scanning import scanScreenshot
import os
from utility import title
from pathlib import Path

def screenshotListener(appState):
    while True:
        if not appState.screenshottingEnabled:
            time.sleep(0.1)
            continue

        try:
            screenshotting(appState)
        except Exception as e:
            print(f"Error: {e}")

        appState.screenshottingEnabled = False

def toggleScreenshotting(appState):
    activeWindow = pygetwindow.getActiveWindow()

    if not activeWindow or "testScreenshot.png" not in activeWindow.title:
        print("testScreenshot is not focused!!")
        return

    if not appState.isWarframeRunning:
        print(Fore.RED + "Warframe must be running in order to be able to scan drops!" + Fore.RESET)
        return

    if appState.screenshottingEnabled:
        print(Fore.RED + "Scanning in process please wait for results before retrying!" + Fore.RESET)
        return
    
    appState.screenshottingEnabled = True

    os.system('cls')
    title()
    print(Fore.CYAN + "Scanning enabled!" + Fore.RESET)

def screenshotting(appState):
    SCREENSHOT_PATH = Path(__file__).resolve().parent.parent / "screenshots"
    SCREENSHOT_PATH.mkdir(exist_ok=True)

    while appState.isWarframeRunning and appState.screenshottingEnabled:
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
            file_path = SCREENSHOT_PATH / fileName

            img = np.array(screenshot)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
            img = cv2.convertScaleAbs(img, alpha=2.5, beta=0)
            crop = img[380:480, 400:1520]

            scanScreenshot(appState, crop)

            success = cv2.imwrite(str(file_path), crop)

            print(f"Saved: {success}")
            print(f"Saved to: {SCREENSHOT_PATH}\screenshots\{fileName}")
            
        time.sleep(1)