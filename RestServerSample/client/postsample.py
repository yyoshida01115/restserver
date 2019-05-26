'''
Created on 2019/05/26

@author: yutaka
'''
import urllib.request
import json

if __name__ == '__main__':
    server_ipaddr="192.168.56.10"
    server_port=18888
    url="http://%s:%s/post-sample" % (server_ipaddr,server_port)
    
    param={
        "fruit":"apple",
        "file":"filename"
        }
    req_body=json.dumps(param)
    
    req = urllib.request.Request(url,req_body)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
        print(body)