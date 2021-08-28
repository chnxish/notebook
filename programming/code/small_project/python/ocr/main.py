import download
from ocr import Ocr
import screenshot
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 main.py option file_path')
        exit(1)

    option = sys.argv[1]
    if option == '-l':
        if len(sys.argv) < 3:
            print('Usage: python3 main.py -l ./image/string.png')
            exit(1)
        file_path = sys.argv[2]
    elif option == '-u':
        if len(sys.argv) < 3:
            print('Usage: python3 main.py -u url_of_the_image')
            exit(1)
        image_url = sys.argv[2]
        file_path = download.download_image(image_url)
    elif option == '-s':
        file_path = screenshot.specified_size_screenshot()
    else:
        print('Error: main: ' + option + ': invalid option')
        exit(1)

    o = Ocr(file_path)
    o.run()
    result = o.result()

    print(result)