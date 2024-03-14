from threading import Thread
import threading

class Demo():

    def dispInfo(self):
        print('In DispInfo')
        print(threading.current_thread().name)

    def dispData(self):
        print('In DispData')
        print(threading.current_thread().name)

print('Main Thread')
obj = Demo()
t1 = Thread(target = obj.dispInfo)
t2 = Thread(target = obj.dispData)

t1.name = 'Core2Web'
t2.name = 'Incubator'

t1.start()
t2.start()
