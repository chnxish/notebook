# Introduction
Download videos from bilibili using you-get and ffmpeg.

## Option

```
python3 main.py url_path episode_num
```

  + if the number of episodes of the video you downloaded is only one episode:

    - url_path: like https://www.bilibili.com/video/BV1Dk4y1q781

    - episode_num = 1

  + if the number of episodes of the video you downloaded has many episodes:

    - url_path: like https://www.bilibili.com/video/BV1Dk4y1q781?p=1

    - episode_num = n

## Folder

  + You need to execute `mkdir video/ video/flv/ video/mp4/` command
