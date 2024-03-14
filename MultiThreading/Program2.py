import threading, os

for x in range (1,10):
    print(x)

print(os.getpid())
print(threading.current_thread().name)

'''
1
2
3
4
5
6
7
8
9
121
MainThreadq
'''
