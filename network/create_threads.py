import threading

# Use a decorator taking a generic function to create threads.
def create_threads(list, function):

    # Keep track of threads created in a list.
    threads = []

    for ip in list:
        th = threading.Thread(target = function, args = (ip,))  # args is a tuple with a single element
        th.start()
        threads.append(th)

    # Wait for all threads to finish
    for th in threads:
        th.join()

