import logging
import urllib.request
import time
import os
from datetime import datetime

class NetObserver:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path_log = os.path.join(dir_path, '..', 'report.log')
        logging.basicConfig(filename=path_log, encoding='utf-8', level=logging.DEBUG)
        self.logger = logging.getLogger('NetObserver')
        self.logger.info('Initialized')

    def connect(self):
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            return True
        except:
            return False
    
    def write_log(self, msg, type=1):
        """
            Type 1 = Info
            Type 2 = Warning
            Type 3 = Error
        """
        act_datetime = datetime.now()
        act_datetime = act_datetime.strftime('%d/%m/%Y %H:%M')
        msg = "[" + act_datetime + "] " + msg
        
        
        if type == 1:
            self.logger.info(msg)
        elif type == 2:
            self.logger.warning(msg)
        elif type == 3:
            self.logger.error(msg)
        else:
            self.logger.error('Invalid type to write log')
    