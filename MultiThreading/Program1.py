# Module : _thread 
# Wrapper : threading 

import threading
print('Start Code')
def fun():
    print("In fun function")

print(threading.current_thread().name)
fun()
'''
Start Code
MainThread
In fun function
'''
