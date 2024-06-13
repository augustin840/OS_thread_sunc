import threading
import multiprocessing
import os
import time

# Create a lock object
lock = multiprocessing.Lock()


# Function to write to the shared file
def write_to_file():
    with lock:
        pid = os.getpid()
        tid = threading.get_ident()
        print(f"Process {pid}, Thread {tid} is writing to the file.")

        with open("shared_file.txt", "a") as file:
            file.write(f"App 2- Process {pid}, Thread {tid} wrote this line.\n")

        time.sleep(2)  # Simulate some work


# Create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=write_to_file)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
