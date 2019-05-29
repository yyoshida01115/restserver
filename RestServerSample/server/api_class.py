'''
Created on 2019/05/23

@author: yutaka
'''

from common import logger_func
import json
import falcon
import datetime
import traceback
from numpy import require

error_msg={
    0:{"Server side exception occurred. See server log."},
    }

apiclass_logger=logger_func.mylogger("Sample",'../log/apiclass.log')

_CHUNK_SIZE_BYTES=4096

class MandantryParameterNotSpecifiedException(Exception):
    """
    必須パラメタが指定されていない時の例外
    """
    def __init__ (self, param):
        self._param = param  # メンバ変数に代入
    def getResponse(self):                      # エラーメッセージ
        msg={"errorMessage":"Parameter '{0}' is not specified.".format (self._param)}
        return(msg)
    
class WrongSpacifiedValueException(Exception):
    """
    指定されたパラメタが定義範囲外
    """
    def __init__ (self, key,value):
        self._key,self._value = (key,value)  # メンバ変数に代入
    def getResponse(self):                      # エラーメッセージ
        msg={"errorMessage":"'{1}', a value of parameter '{0}' is wrong value.".format (self._key,self._value)}
        return (msg)
    

def check_postparam(data,param_definition):
    for key,value in param_definition.items():
        if value["mandantry"] and key not in data.keys():
            raise MandantryParameterNotSpecifiedException(key)
    for datakey,datavalue in data.items():
        if datavalue not in param_definition[datakey]["value"]:
            raise WrongSpacifiedValueException(datakey,datavalue)
    return 0
    
class Sample(object):
    
    uri = "/sample"
    
    def __init__(self):
        pass

    def on_get(self, req, resp):
        try:
            msg = {
                "message": "Get Sample",
            }
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(msg)
        except:
            apiclass_logger.error(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.body = json.dumps(error_msg[0])
            
class UploadSample(object):
    
    uri = "/sample/file"
    
    def __init__(self):
        pass

    def on_post(self, req, res):
        try:
            #filename = req.get_param('name')
            #uploadfile = req.get_param('file')
            #raw = uploadfile.file.read()
            #filepath = '../file/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
            #with open(filepath, 'wb') as f:
            #    f.write(raw)
            assert req.get_param('simple') == 'ok'
            #assert req.get_param('file').filename == 'afile.txt',req.get_param('afile').filename
            #assert req.get_param('file').file.read() == b'filecontent',req.get_param('afile').file.read()
            filename=req.get_param('file').filename
            with open('../file/upload-%s' % filename,'wb') as savefile:
                savefile.write(req.get_param('file').file.read())
            res.body = 'parsed'
            res.content_type = 'text/plain'
        except:
            apiclass_logger.error(traceback.format_exc())
            res.status = falcon.HTTP_500
            res.body = json.dumps(error_msg[0])
    
    def on_delete(self, req, res):
        try:
            # postパラメーターを取得
            assert req.get_param('simple')=="ok",req.get_param('simple')
            
            msg = {
                "message": "delete sample",
            }
            res.status = falcon.HTTP_200
            res.body = json.dumps(msg)
        except:
            import traceback
            apiclass_logger.error(traceback.format_exc())
            res.status = falcon.HTTP_500
            res.body = json.dumps(error_msg[0]).encode('utf-8')


class PostSample(object):

    uri = "/sample/post-sample"
    param_definition={
        "fruit":{"mandantry":True,
                "value":["apple","orange","banana",]},
        "file":{"mandantry":False,
                "value":["filename"]},
        }
    
    def __init__(self):
        pass
        
    def on_post(self, req, resp):
        try:
            ## get_param_as_json
            # https://code-examples.net/ja/docs/falcon~1.4/api/request_and_response#falcon.Request.get_param_as_json
            data={}
            for k,v in self.param_definition.items():
                data[k]=req.get_param(name=k,required=v["mandantry"],default=None)
                if data[k] not in v["value"]:
                    raise WrongSpacifiedValueException(k,data[k])
            
            msg = {
                "message": "Post sample",
                "data":data,
            }
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(msg)
        except falcon.HTTPBadRequest as e:
            apiclass_logger.error(traceback.format_exc())
            resp.status = e.status
            resp.body = e.to_json().encode('utf-8')
        except WrongSpacifiedValueException as e:
            apiclass_logger.error(traceback.format_exc())
            resp.status = falcon.HTTP_400
            apiclass_logger.debug(json.dumps(e.getResponse()))
            resp.body = json.dumps(e.getResponse()).encode('utf-8')
        except:
            apiclass_logger.error(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.body = json.dumps(error_msg[0]).encode('utf-8')

            
class CORSMiddleware:
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')