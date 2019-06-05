'''
Created on 2019/05/25

@author: yutaka
'''
import urllib.request
import requests

if __name__ == '__main__':
    server_ipaddr="127.0.0.1"
    server_port=18888
    url="http://%s:%s/sample" % (server_ipaddr,server_port)
    
    payload = {'name': 'hello', 'data': 'hello'}
    r = requests.get(url, params=payload)
    
    print(r.text)