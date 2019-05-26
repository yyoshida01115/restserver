'''
Created on 2019/05/25

@author: yutaka
'''
import urllib.request

if __name__ == '__main__':
    server_ipaddr="192.168.56.10"
    server_port=18888
    url="http://%s:%s/sample" % (server_ipaddr,server_port)
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
        print(body)