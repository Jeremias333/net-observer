try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..'
            )
        )
    )
except:
    raise

from net_observer import NetObserver
import time
import signal
import sys
from datetime import datetime

def main():
    count_tests = 0
    most_download_rate = 0
    most_upload_rate = 0
    less_ms_rate = 1
    date_without_connection_start = None
    time_without_connection = 0 
    count_lost_connections = 0 #Utilizar esta variável para contar quantas vezes a net caiu 
    lost_connection = False
    
    net_observer = NetObserver()
    def before_exit(signum, frame):
        msg = "Quantidade de testes de conexão: "+ str(count_tests)
        net_observer.write_log(msg, 1)
        net_observer.write_long_log(msg, 1)
        
        net_observer.write_log("Finalizado")
        net_observer.write_long_log("Finalizado")
        sys.exit(1)

    signal.signal(signal.SIGINT, before_exit)
    signal.signal(signal.SIGTERM, before_exit)
    signal.signal(signal.SIGHUP, before_exit)

    while True:
        time_start = time.time()
        has_internet = net_observer.connect()
        time_finish = time.time() - time_start
        
        if has_internet:
            if lost_connection == True:
                lost_connection = False
                net_observer.write_log("Conexão restabelecida")
                net_observer.write_long_log("Conexão restabelecida")
                time_without_connection = net_observer.time_without_connection(date_without_connection_start, datetime.now())
                net_observer.write_log(time_without_connection, 2)
                net_observer.write_long_log(time_without_connection, 2)
            msg = 'Conectado'
            msg += ' - Download: '+str(net_observer.download_test())+' MB'
            msg += ' - Upload: '+str(net_observer.upload_test())+' MB'
            msg += ' - '+str(round(time_finish, 2))+' ms'
        else:
            if lost_connection == False:
                lost_connection = True
                date_without_connection_start = datetime.now()
                net_observer.write_log("Conexão perdida")
                net_observer.write_long_log("Conexão perdida")
            msg = 'Sem conexão'
        
        count_tests += 1
        
        net_observer.write_long_log(msg)
        time.sleep(2)
    

if __name__ == "__main__":
    main()