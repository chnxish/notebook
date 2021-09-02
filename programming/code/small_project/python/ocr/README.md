# Introduction
Use Baidu OCR API to recognize characters in pictures.

You need to set:

  + ocr.py

    - APP_ID

    - API_KEY

    - SECREY_KEY

  + screenshot.py

    - zoom_ratio

## Option

| Image Location | Option |
| -------------- | ------ |
| Local | -l |
| Network | -u |
| Screenshots Required | -s |

```
python3 main.py -l ./image/string.png
python3 main.py -u url_of_the_image
python3 main.py -s
```
