'''
Created on 2019/05/26

@author: yutaka
'''
import requests
import json


if __name__ == '__main__':
    try:
        server_ipaddr="127.0.0.1"
        server_port=18888
        url="http://%s:%s/sample/file" % (server_ipaddr,server_port)
        method = "POST"

        with open("../file/snow.zip", 'rb') as f:
            files = {'file': ('snow.zip',f,'application/octet-stream')}
            #data = {'another_key': 'another_value'}
            #r = requests.post(URL, files=files, data=data)
            r = requests.post(url, data={'simple': 'ok'},
                           files=files)
            print(r.status_code)
            print(r.text)
    except:
        import traceback
        print(traceback.format_exc())
