import pygetwindow

def getWarframeWindow():
    gameWindows = pygetwindow.getWindowsWithTitle("Warframe")

    if gameWindows:
        return(gameWindows[0])
    else: 
        print("No 'Warframe' window found!")