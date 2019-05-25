'''
Created on 2019/05/23

@author: yutaka
'''

import json

class StorageFirmware(object):

    def on_get(self, req, resp):

        msg = {
            "message": "Get Storage Firmware",
        }
        resp.body = json.dumps(msg)
        


