'''
Created on 2019/05/23

@author: yutaka
'''

import json
import falcon

class StorageFirmware(object):

    def on_get(self, req, resp):

        msg = {
            "message": "Get Storage Firmware",
        }
        resp.body = json.dumps(msg)
        


class ApiServerFactory(object):
    
    def __init(self):
        self.apiserver = falcon.API()
        self.apiserver.add_route("/storage-firmware", StorageFirmware())
        
    def getApiServer(self):
        return self.apiserver
        
