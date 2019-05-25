'''
Created on 2019/05/23

@author: yutaka
'''
from server import api_class
from common import logger_func
import sys
import falcon

def server_main():
	logger=logger_func.mylogger("server_main")
	try:
		from wsgiref import simple_server
		apiserver = falcon.API()
		apis=[]
		apis.append(api_class.Firmware())
		apis.append(api_class.FirmwareUpdateServicePrecheck())
		
		for api in apis:
			apiserver.add_route(api.uri, api)
		httpd = simple_server.make_server("0.0.0.0", 18888, apiserver)
		httpd.serve_forever()
	except KeyboardInterrupt:
		sys.exit(0)
	except:
		import traceback
		logger.error(traceback.format_exc())
		
		
if __name__ == '__main__':
	server_main()
