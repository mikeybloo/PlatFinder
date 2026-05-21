import keyboard
from src.main import exitProgram
from src.screenshotting import toggleScreenshotting

keyboard.add_hotkey("shift+f12", exitProgram)
keyboard.add_hotkey("shift+f5", toggleScreenshotting)