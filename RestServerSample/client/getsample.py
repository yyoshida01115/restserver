'''
Created on 2019/05/25

@author: yutaka
'''
import urllib.request

if __name__ == '__main__':
    server_ipaddr="127.0.0.1"
    server_port=18888
    url="http://%s:%s/sample" % (server_ipaddr,server_port)
    
    #data = urllib.parse.urlencode(data).encode("utf-8")

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
        print(body)