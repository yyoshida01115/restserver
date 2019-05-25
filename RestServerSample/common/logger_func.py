'''
Created on 2019/05/25

@author: yutaka
'''
import sys

def mylogger(logger_name):
    from logging import getLogger,StreamHandler,FileHandler,Formatter, DEBUG,INFO,basicConfig
    logger = getLogger(logger_name)
    formatter=Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
    shandler = StreamHandler()
    shandler.setFormatter(formatter)
    fhandler = FileHandler('../log/server.log')
    fhandler.setFormatter(formatter)
    shandler.setLevel(DEBUG)
    fhandler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(shandler)
    logger.addHandler(fhandler)
    logger.propagate = False
    basicConfig(stream=sys.stdout, level=INFO)
    return logger