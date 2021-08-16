# -*- coding:utf-8 -*-
import os
import yaml

def main():
    # 读取yaml数据
    yaml_files = []
    with open('./file.yaml', 'r') as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
        for values in d.values():
            for value in values:
                yaml_files.append(value)
    
    # 读取txt数据
    dir_files = os.listdir('./txt')

    # 求交集
    files = list(set(yaml_files).intersection(set(dir_files)))
    
    # java -jar plantuml.jar file_name
    for f in files:
        os.system('java -jar ./plantuml.jar ./txt/' + f + ' -o ../png/')
        print(f)


if __name__ == '__main__':
    main()