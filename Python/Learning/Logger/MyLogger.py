#-*-encoding:utf-8-*-

import logging

logfile = 'log.txt'
logger = logging.getLogger()
hdlr = logging.FileHandler(logfile)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.NOTSET)
logger.info('message')
