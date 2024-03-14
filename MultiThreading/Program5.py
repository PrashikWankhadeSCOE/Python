import threading 
from threading import Thread 

class MyThread(Thread):
    def run(self):
        print('In run')
        print(threading.current_thread().name)

print('Main Thread start')
t1 = MyThread()
t1.start()
print('Main thread end')
