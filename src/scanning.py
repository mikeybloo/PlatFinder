#import easyocr

def scanScreenshot(appState, crop):
    print("Now scanning screenshot...")
    result = appState.reader.readtext(crop, detail = 0)
    print("Screenshot scanned!")
    print("Recognized: " + result)

    for item in result:
        print()