from threading import *
from time import *
 
def Hello():
    for i in range(5):
        print(f'{current_thread().name} is printing Hello')
        sleep(1) # After printing, we suspend the execution by 1 second by using time.sleep() function
 
def Hi():
    for i in range(5):
        print(f'{current_thread().name} is printing Hi')
        sleep(1) # After printing, we suspend the execution by 1 second by using time.sleep() function
 
t1 = Thread(target = Hello, name = "Thread1") # Target Function t1 thread executes in Hello()
t2 = Thread(target = Hi, name = "Thread2") # Target Function t2 thread executes is Hi()
 
t1.start() # To start executing thread t1 
t2.start() # To start executing thread t2
 
############################################################################################################################
 
# Now, lets see two threading accessing the same function without any lock.
 
import threading, time
 
def Hello():
    for i in range(10):
        print(f'{threading.current_thread().name} is printing Hello')
        time.sleep(1)
 
t1 = threading.Thread(target = Hello, name = "Thread1") # Target Function t1 thread executes in Hello()
t2 = threading.Thread(target = Hello, name  = "Thread2") # Target Function t2 thread executes is Hello()
 
t1.start() # To start executing thread t1 
t2.start() # To start executing thread t2
 
 
###############################################################################################################################

# Multiple threads accessing the same method with Lock
 
import threading, time
 
lock = threading.Lock() # Lock
def Hello():
    lock.acquire() # Lock gets acquired by a thread, and until the lock is released no thread can enter this block of code
    for i in range(10):
        print(f'{threading.current_thread().name} is printing Hello')
        time.sleep(1)
    lock.release() # Lock gets released by the thread, and now it is available for the next thread to acquire the lock
 
 
t1 = threading.Thread(target = Hello, name = "Thread1") # Target Function t1 thread executes in Hello()
t2 = threading.Thread(target = Hello, name = "Thread2") # Target Function t2 thread executes is Hello()
 
t1.start() # To start executing thread t1 
t2.start() # To start executing thread t2
 
##################################################################################################################################
