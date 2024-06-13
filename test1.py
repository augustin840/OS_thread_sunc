import threading

import time


# function that write  the shared file
def write_to_file():
    with open("shared_file.txt", "a") as file:
        file.write(f"App 1- is writing this file.\n")

        time.sleep(2)  # ssimulate some work


if __name__ == "__main__":
    threads = []

    for i in range(8):
        t = threading.Thread(target=write_to_file)
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
