'''
Created on 2019/05/23

@author: yutaka
'''

from common import logger_func
import json
import falcon

error_msg={
    0:{"Server side exception occurred. See server log."},
    }


class Firmware(object):
    
    uri = "/firmware"
    
    def __init__(self):
        self.logger=logger_func.mylogger("Firmware")

    def on_get(self, req, resp):
        try:
            msg = {
                "message": "Get Storage Firmware",
            }
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(msg)
        except:
            import traceback
            self.logger.error(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.body = json.dumps(error_msg[0])
        

class FirmwareUpdateServicePrecheck(object):

    uri = "/firmware-update-service/precheck"
    
    def __init__(self):
        self.logger=logger_func.mylogger("FirmwareUpdateServicePrecheck")

    def on_post(self, req, resp):
        try:
            msg = {
                "message": "Storage firmware update service precheck",
            }
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(msg)
        except:
            import traceback
            self.logger.error(traceback.format_exc())
            resp.status = falcon.HTTP_500
            resp.body = json.dumps(error_msg[0])
