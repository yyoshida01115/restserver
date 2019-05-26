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
        url="http://%s:%s/sample/post-sample" % (server_ipaddr,server_port)
        method = "POST"
        data={
            "fruit":"apple",
            "file":"filename"
            }
        
        r = requests.post(url, data=data)
        print(r.text)
    except:
        import traceback
        traceback.print_exc()
        #body = res.read().decode("utf-8")
        #print(body)