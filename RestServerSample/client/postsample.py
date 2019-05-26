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
    
    data={
        "fruit":"apple",
        "file":"filename"
        }
    data = urllib.parse.urlencode(data).encode("utf-8")
    
    with urllib.request.urlopen(url=url, data=data) as res:
        body = res.read().decode("utf-8")
        print(body)