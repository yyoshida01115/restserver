'''
Created on 2019/05/25

@author: yutaka
'''

def mylogger(logger_name):
    from logging import getLogger,StreamHandler,FileHandler, DEBUG
    logger = getLogger(logger_name)
    shandler = StreamHandler()
    fhandler = FileHandler('../log/server.log')
    shandler.setLevel(DEBUG)
    fhandler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(shandler)
    logger.addHandler(fhandler)
    logger.propagate = False
    return logger