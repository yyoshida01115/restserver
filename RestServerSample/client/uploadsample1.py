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
        
        #https://github.com/yohanboniface/falcon-multipart/blob/master/tests/test_middleware.py
        ##https://github.com/kennethreitz/requests/issues/1495#issuecomment-21581939
        files = {'afile': ('afile.txt','filecontent','text/plain')}

        r = requests.post(url, data={'simple': 'ok'},
                       files=files)
        print(r.status_code)
        print(r.text)
    except:
        import traceback
        print(traceback.format_exc())
