import os
import time

pid = os.fork()

if pid == 0:
    # Child process
    print("Child process is running")
    time.sleep(10)
    print("Child process is exiting")
else:
    # Parent process
    print(f"Parent process created child process with PID {pid}")
    time.sleep(5)
    print("Parent process is exiting")

