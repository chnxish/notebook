import os
import re
import sys

from ftc import Ftc
import tabular

def recursively_traverse_directories(file_path):
    # info = [[file1, path1], [file2, path2], ...]
    info = []
    for root, dirs, files in os.walk(file_path):
        for f in files:
            info.append([f, root])

    return info

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 main.py file_path')
        exit(1)

    file_path = sys.argv[1]
    info = recursively_traverse_directories(file_path)

    mylist = list()
    for i in info:
        # delete the part of './' or '../' in the file_path
        r = re.search('\w', i[1])
        if r == None:
            r = ''
        else:
            r = i[1][r.span()[0]:]

        mylist.append(Ftc(i[0], r))

    # (Paco) https://www.zhihu.com/question/30389643/answer/412385014
    # ss = [1, 2, 333, 8, 234, 5923, 7, 49]
    # sss = sorted(ss, key=functools.cmp_to_key(lambda a,b: int(str(a)+str(b))-int(str(b)+str(a))), reverse=True)
    mylist.sort(key = lambda ftc: ftc.file_type + ftc.file_name[ftc.file_name.rfind('.'):] + ftc.file_name.lower())

    tabular.tabular(mylist)
