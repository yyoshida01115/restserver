'''
Created on 2019/05/23

@author: yutaka
'''
from server import api_class

if __name__ == '__main__':
    from wsgiref import simple_server
    app = api_class.ApiServerFactory()
    httpd = simple_server.make_server("127.0.0.1", 8888, app.getApiServer())
    httpd.serve_forever()