'''
Created on 2019/05/23

@author: yutaka
'''
from . import api_class
import sys

if __name__ == '__main__':
	try:
		from wsgiref import simple_server
		app = api_class.ApiServerFactory()
		httpd = simple_server.make_server("127.0.0.1", 8888, app.getApiServer())
		httpd.serve_forever()
	except KeyboardInterrupt:
		sys.exit(0)
