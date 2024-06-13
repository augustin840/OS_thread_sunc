import threading
import multiprocessing
import os
import time


lock = multiprocessing.Lock()


# function that write  the shared file
def write_to_file():
    with lock:
        pid = os.getpid()
        tid = threading.get_ident()
        print(f"processe {pid}, thread {tid} is writing the file.")

        with open("shared_file.txt", "a") as file:
            file.write(f"App 1- process {pid}, thread {tid} is writing this file.\n")

            time.sleep(2) # ssimulate some work

# Create multiple threads
threads = []
for i in range(8):
    t = threading.Thread(target=write_to_file)
    threads.append(t)
    t.start()
""
for t in threads:
    t.join()
