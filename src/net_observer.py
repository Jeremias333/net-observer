import logging
import urllib.request
import time
import os
from datetime import datetime
import speedtest
from datetime import datetime

class NetObserver:
    def __init__(self):
        self.logger = None
        self.__initilized_info()
        self.speed_test = speedtest.Speedtest()

    def connect(self):
        try:
            urllib.request.urlopen('https://google.com') #Python 3.x
            return True
        except:
            return False
    
    def upload_test(self):
        return self.__bytes_to_mb(self.speed_test.upload())
    
    def download_test(self):
        return self.__bytes_to_mb(self.speed_test.download())

    def time_without_connection(self, date_start, date_end):
        sub_date = date_end - date_start
        str_result = "Conexão perdida por: "
        if sub_date.total_seconds() < 59:
            str_result += str(round(sub_date.total_seconds(), 2)) + "s"
            return str_result
        str_result += str(round((sub_date.total_seconds()/60), 2)) + "min"
        return str_result

    def write_log(self, msg, type=1):
        """
            Type 1 = Info
            Type 2 = Warning
            Type 3 = Error
        """
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
        #Initializing o log long
        path_log = os.path.join(dir_path, '..', 'report.log')
        self.logger = self.__config_log(path_log, "NET Observer System")

        act_datetime = datetime.now()
        act_datetime = act_datetime.strftime('%d/%m/%Y %H:%M')
        msg = "[" + act_datetime + "] " + str(msg)
        
        
        if type == 1:
            self.logger.info(msg)
        elif type == 2:
            self.logger.warning(msg)
        elif type == 3:
            self.logger.error(msg)
        else:
            self.logger.error('Invalid type to write log')
    
    def write_long_log(self, msg, type=1):
        """
            Type 1 = Info
            Type 2 = Warning
            Type 3 = Error
        """
                
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
        #Initializing o log long
        path_log = os.path.join(dir_path, '..', 'report_long.log')
        self.logger = self.__config_log(path_log, "NET Observer System")

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
    
    def __config_log(self, path, name="NET Observer"):
        fileh = logging.FileHandler(path, 'a')
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        fileh.setFormatter(formatter)

        log = logging.getLogger(name)  # root logger
        for hdlr in log.handlers[:]:  # remove all old handlers
            log.removeHandler(hdlr)
        log.addHandler(fileh)      # set the new handler
        log.setLevel(logging.DEBUG)
        return log

    def __initilized_info(self):
        msg = "Inicializado"
        
        act_datetime = datetime.now()
        act_datetime = act_datetime.strftime('%d/%m/%Y %H:%M')
        msg = "[" + act_datetime + "] " + msg
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
        #Initializing o log long
        path_log = os.path.join(dir_path, '..', 'report_long.log')
        self.logger = self.__config_log(path_log, "NET Observer System")
        self.logger.info(msg)
        
        #Initializing short log
        path_log = os.path.join(dir_path, '..', 'report.log')
        self.logger = self.__config_log(path_log, "NET Observer System")
        self.logger.info(msg)


    def __bytes_to_mb(self, bytes):
        KB = 1024 # One Kilobyte is 1024 bytes
        MB = KB * 1024 # One MB is 1024 KB
        return int(bytes/MB)