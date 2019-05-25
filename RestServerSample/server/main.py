'''
Created on 2019/05/23

@author: yutaka
'''
from server import api_class
import sys

def server_logger():
	from logging import getLogger,StreamHandler,FileHandler, DEBUG
	logger = getLogger("RestServerLogger")
	shandler = StreamHandler()
	fhandler = FileHandler('../log/server.log')
	shandler.setLevel(DEBUG)
	fhandler.setLevel(DEBUG)
	logger.setLevel(DEBUG)
	logger.addHandler(shandler)
	logger.addHandler(fhandler)
	logger.propagate = False
	return logger

def server_main():
	try:
		logger=server_logger()
		from wsgiref import simple_server
		app = api_class.ApiServerFactory()
		httpd = simple_server.make_server("0.0.0.0", 18888, app.getApiServer())
		httpd.serve_forever()
	except KeyboardInterrupt:
		sys.exit(0)
	except:
		import traceback
		logger.error(traceback.format_exc())
		
		
if __name__ == '__main__':
	server_main()
