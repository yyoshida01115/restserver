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

    apiserver=None
    
    def __init(self):
        apiserver = falcon.API()
        apiserver.add_route("/storage-firmware", StorageFirmware())
        self.apiserver=apiserver
        
    def getApiServer(self):
        return self.apiserver
        
