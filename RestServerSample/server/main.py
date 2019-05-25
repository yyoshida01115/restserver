'''
Created on 2019/05/23

@author: yutaka
'''
from server import api_class
import sys
import falcon

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
	logger=server_logger()
	try:
		from wsgiref import simple_server
		apiserver = falcon.API()
		apiserver.add_route("/storage-firmware", api_class.StorageFirmware())
		httpd = simple_server.make_server("0.0.0.0", 18888, apiserver)
		httpd.serve_forever()
	except KeyboardInterrupt:
		sys.exit(0)
	except:
		import traceback
		logger.error(traceback.format_exc())
		
		
if __name__ == '__main__':
	server_main()
