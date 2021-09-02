import os
import time

import requests

def download_image(image_url, folder_name = './image'):
    try:
        response = requests.get(image_url)
    except requests.exceptions.RequestException as e:
        print(e)

    tm = time.localtime(time.time())
    file_name = 'url' + str(tm.tm_hour) + str(tm.tm_min) + str(tm.tm_sec) + '.png'
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'wb') as f:
        f.write(response.content)

    return file_path

if __name__ == '__main__':
    image_url = 'https://wx1.sinaimg.cn/mw690/003XTRPZgy1gtt08bogkyj60qo0pd76j02.jpg'
    download_image(image_url)
