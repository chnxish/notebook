from PIL import ImageGrab
import pyautogui
import sys
import time

def screenshot(bbox, folder_name = './image'):
    if bbox:
        im = ImageGrab.grab(bbox=bbox)
        tm = time.localtime(time.time())
        file_name = 'ss' + str(tm.tm_hour) + str(tm.tm_min) + str(tm.tm_sec) + '.png'
    else:
        im = ImageGrab.grab() # full screen

    file_path = '{}{}{}'.format(folder_name, '/', file_name)
    im.save(file_path)

    return file_path

def specified_size_screenshot():
    time.sleep(3)
    print('next')
    x1, y1 = pyautogui.position()
    time.sleep(3)
    x2, y2 = pyautogui.position()

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    pf = sys.platform
    if pf == 'linux':
        pass
    elif pf == 'win32':
        zoom_ratio = 1
    elif pf == 'darwin':
        zoom_ratio = 2
    else:
        zoom_ratio = 1 # default value

    bbox = [x1 * zoom_ratio, y1 * zoom_ratio, x2 * zoom_ratio, y2 * zoom_ratio]

    return screenshot(bbox)

if __name__ == '__main__':
    # -f = full screen
    # -s = specified size
    if len(sys.argv) < 2:
        print('Usage: python3 screenshot.py option')
        exit(1)

    option = sys.argv[1]
    if option == '-f':
        screenshot(None)
    elif option == '-s':
        specified_size_screenshot()
    else:
        print('Error: screenshot: ' + option + ': invalid option')
        exit(1)
