import os
import subprocess
import sys

def runcmd(command):
    ret = subprocess.run(command, shell=True, stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, encoding='utf-8')
    if ret.returncode == 0:
        print('Success: ', ret)
    else:
        print('Error: ', ret)

def download(url_path, episode_num = 1, output_directory = './video/flv/'):
    bilibili_video_path = 'www.bilibili.com/video/'
    index = url_path.find(bilibili_video_path)
    if index == -1:
        print('Error: this url path cannot access bilibili resources')
        exit(1)

    if episode_num == 1:
        print('Start:')
        command = 'you-get ' + url_path + ' -o ' + output_directory + ' --format=flv720'
        runcmd(command)
    elif episode_num > 1:
        index = url_path.rfind('p=')
        if index == -1:
            print('Error: this url path cannot access multiple video resources')
            exit(1)

        num = 1
        url_path = url_path[:index + 1]
        while num <= episode_num:
            num_str = str(num)
            print('Start: ' + num_str)
            command = 'you-get ' + url_path + num_str + ' -o ' + output_directory + ' --format=flv720'
            runcmd(command)
    else:
        print('Error: incorrect number of video episodes')
        exit(1)

def process_files(input_directory = './video/flv/'):
    other_files = []

    for _, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.xml'):
                os.remove(os.path.join(input_directory, file))
            else:
                other_files.append(file)

    print('Unprocessed files:')
    for file in other_files:
        print('\t' + file)

def flv_to_mp4(input_directory = './video/flv/', output_directory = './video/mp4/'):
    input_files = []
    output_files = []

    for _, _, input_files in os.walk(input_directory):
        for input_file in input_files:
            if input_file.rfind('.flv') != -1:
                input_files.append(input_file)
                output_file = input_file[:input_file.rfind('.flv')]
                output_files.append(output_file + '.mp4')

    step = len(input_files)
    for i in range(step):
        num_str = str(num)
        print('Start: ' + input_files[i] + ' ' + output_files[i])
        command = 'ffmpeg -i ' + input_directory + input_files[i] + ' ' + output_directory + output_files[i]
        runcmd(command)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 main.py url_path episode_num')
        exit(1)

    url_path = sys.argv[1]
    episode_num = int(sys.argv[2])

    download(url_path, episode_num)

    process_files()

    flv_to_mp4()
