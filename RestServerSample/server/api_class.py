'''
Created on 2019/05/23

@author: yutaka
'''

from common import logger_func
import json
import falcon
import datetime
import traceback

error_msg={
    0:{"Server side exception occurred. See server log."},
    }

apiclass_logger=logger_func.mylogger("Sample",'../log/apiclass.log')

class MandantryParameterNotSpecifiedException(Exception):
    """
    必須パラメタが指定されていない時の例外
    """
    def __init__ (self, param):
        self._param = param  # メンバ変数に代入
    def getResponse(self):                      # エラーメッセージ
        msg={"errorMessage":'必須パラメタ "{0}" が指定されていません。'.format (self._param)}
        return(msg)
    
class WrongSpacifiedValueException(Exception):
    """
    指定されたパラメタが定義範囲外
    """
    def __init__ (self, key,value):
        self._key,self._value = (key,value)  # メンバ変数に代入
    def getResponse(self):                      # エラーメッセージ
        msg={"errorMessage":'パラメタ "{0}" の値 "{1}" は定義範囲外です。'.format (self._key,self._value)}
        return (msg)
    

def check_postparam(data,param_definition):
    for key,value in param_definition.items():
        if value == value["mandantry"] and key not in data.keys():
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
            uploadfile = req.get_param('file')
            raw = uploadfile.file.read()
            filepath = '../file/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
            with open(filepath, 'wb') as f:
                f.write(raw)
        
            resp = {
                'result': filepath + ' uploaded',
            }
            res.body = json.dumps(resp)
        except:
            apiclass_logger.error(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.body = json.dumps(error_msg[0])
        

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
            # postパラメーターを取得
            body = req.stream.read().decode("utf-8")
            apiclass_logger.debug(body)
            data = json.loads(body)
            
            ## parameter check
            check_postparam(data, self.param_definition)
            
            msg = {
                "message": "Post sample",
            }
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(msg)
        except MandantryParameterNotSpecifiedException as e:
            apiclass_logger.error(traceback.format_exc())
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(e.getResponse())
        except WrongSpacifiedValueException as e:
            apiclass_logger.error(traceback.format_exc())
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(e.getResponse())
        except:
            apiclass_logger.error(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.body = json.dumps(error_msg[0])
            
            
class CORSMiddleware:
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')