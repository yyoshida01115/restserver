'''
Created on 2019/05/26

@author: yutaka
'''
import urllib.request
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
        headers = {"Content-Type" : "application/json"}
        req_body=(json.dumps(data)+'\r\n').encode("utf-8")
        
        req = urllib.request.Request(url, data=req_body, headers=headers, method=method)
        with urllib.request.urlopen(req,timeout=10) as res:
            body = res.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode('utf-8'))  
        #body = res.read().decode("utf-8")
        #print(body)