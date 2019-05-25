'''
Created on 2019/05/25

@author: yutaka
'''
import sys

def mylogger(logger_name,filepath):
    from logging import getLogger,StreamHandler,Formatter, DEBUG,INFO,basicConfig
    import logging.handlers
    logger = getLogger(logger_name)
    formatter=Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
    shandler = StreamHandler()
    shandler.setFormatter(formatter)
    fhandler = logging.handlers.RotatingFileHandler(filepath,maxBytes=1024*1024, backupCount=3)
    fhandler.setFormatter(formatter)
    shandler.setLevel(DEBUG)
    fhandler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(shandler)
    logger.addHandler(fhandler)
    logger.propagate = False
    basicConfig(stream=sys.stdout, level=INFO)
    return logger

class LoggerWriter:
    def __init__(self, level):
        # self.level is really like using log.debug(message)
        # at least in my case
        self.level = level

    def write(self, message):
        # if statement reduces the amount of newlines that are
        # printed to the logger
        if message != '\n':
            self.level(message)

    def flush(self):
        # create a flush method so things can be flushed when
        # the system wants to. Not sure if simply 'printing'
        # sys.stderr is the correct way to do it, but it seemed
        # to work properly for me.
        self.level(sys.stderr)