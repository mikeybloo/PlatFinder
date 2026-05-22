import threading
from screenshotting import screenshotListener

class AppState:
    def __init__(self):
        self.isWarframeRunning = False
        self.screenshottingEnabled = False
        self.reader = None
        self.screenshotThread = threading.Thread(
            target=screenshotListener,
            args=(self,),
            daemon=True,
        )