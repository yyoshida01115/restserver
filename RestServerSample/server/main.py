'''
Created on 2019/05/23

@author: yutaka
'''
from server import api_class
from common import logger_func
import sys
import falcon
from falcon_multipart.middleware import MultipartMiddleware

def server_main():
	logger=logger_func.mylogger("server_main",'../log/server.log')
	## https://codeday.me/jp/qa/20190301/342294.html
	## stdout,stderrをlogger出力
	sys.stdout = logger_func.LoggerWriter(logger.debug)
	sys.stderr = logger_func.LoggerWriter(logger.warning)
	
	try:
		from wsgiref import simple_server
		## Upload API
		## Ref https://qiita.com/komakomako/items/5ba6a1b2a582464a7748
		##
		apiserver = falcon.API(middleware=[api_class.CORSMiddleware(), MultipartMiddleware()])

		apis=[]
		apis.append(api_class.Sample())
		apis.append(api_class.UploadSample())
		apis.append(api_class.PostSample())

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
