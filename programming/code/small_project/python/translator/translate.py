import json
import sys

import requests

def translate(word):
    # youdao translate api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    key = {
        "type": "AUTO",
        "i": word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    response = requests.post(url, data=key)
    if response.status_code == 200:
        return response.text
    else:
        print('error: no response from server')
        return None

def get_reuslt(repsonse, words):
    result = json.loads(repsonse)
    # print("Input: %s" % result['translateResult'][0][0]['src'])
    # print("Output: %s" % result['translateResult'][0][0]['tgt'])
    result_value = '%s' % result['translateResult'][0][0]['tgt']
    if result_value == words:
        print('error: translation failure')
    else:
        print(result_value)

def main():
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
