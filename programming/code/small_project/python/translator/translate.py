#!/usr/bin/python3
# -*- coding:utf-8 -*-
import json
import requests
import sys

# 翻译函数，word 需要翻译的内容
def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return response.text
    else:
        print('error: no response from server')
        # 相应失败就返回空
        return None

def get_reuslt(repsonse, words):
    # 通过 json.loads 把返回的结果加载成 json 格式
    result = json.loads(repsonse)
    # print ("输入的词为：%s" % result['translateResult'][0][0]['src'])
    # print ("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])
    result_value = "%s" % result['translateResult'][0][0]['tgt']
    if result_value == words:
        print('error: translation failure')
    else:
        print(result_value)

def main():
    # print("本程序调用有道词典的API进行翻译，可达到以下效果：")
    # print("外文-->中文")
    # print("中文-->英文")
    # word = input('请输入你想要翻译的词或句：')
    if len(sys.argv) < 2:
        print('error: too few parameters')
        exit(1)

    words = ''
    for word in sys.argv:
        if word == sys.argv[0]:
            continue
        elif word == sys.argv[len(sys.argv) - 1]:
            words += word
        else:
            words += word + ' '

    list_trans = translate(words)
    get_reuslt(list_trans, words)

if __name__ == '__main__':
    main()
