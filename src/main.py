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

def main():
    net_observer = NetObserver()
    while True:
        msg = 'connected' if net_observer.connect() else 'no internet!'
        net_observer.write_log(msg)
        time.sleep(5)


if __name__ == "__main__":
    main()