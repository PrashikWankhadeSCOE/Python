import threading
from threading import Thread
import time

class Demo():
    def fun(self):
        time.sleep(10)
        print('In fun')
        print(threading.current_thread().name)

print(threading.current_thread().name)

obj = Demo()
t1 = Thread(target = obj.fun,daemon = True)

t1.start()

t1.join()
