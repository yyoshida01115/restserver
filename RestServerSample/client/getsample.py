'''
Created on 2019/05/25

@author: yutaka
'''
import urllib

if __name__ == '__main__':
    req = urllib.request.Request('http://192.168.56.10:8888/storage-firmware')
    print(req)