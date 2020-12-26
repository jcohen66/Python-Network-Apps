import threading
import time

def my_function():
    print("Start a thread")
    time.sleep(3)
    print("End a trhead")

threads = []

for i in range(5):
    th = threading.Thread(target = my_function)
    th.start()
    threads.append(th)

for th in threads:
    th.join()
