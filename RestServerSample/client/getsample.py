'''
Created on 2019/05/25

@author: yutaka
'''
import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('http://192.168.56.10:8888')
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body)