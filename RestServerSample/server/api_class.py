'''
Created on 2019/05/23

@author: yutaka
'''

import json

class StorageFirmware(object):
    
    uri = "/storage-firmware"

    def on_get(self, req, resp):

        msg = {
            "message": "Get Storage Firmware",
        }
        resp.body = json.dumps(msg)
        


