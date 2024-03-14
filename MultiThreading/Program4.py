import threading

class MyThread(threading.Thread):
    def fun(self):
        print('In Fun method')
        print(threading.current_thread().name)
    
    def __init__(self,x,y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y

print(threading.current_thread().name)
t1 = MyThread(10,20)
t1.start()


