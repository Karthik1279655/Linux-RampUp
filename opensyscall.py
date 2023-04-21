#!/usr/bin/python3
import os

# Open a file using the open() system call
fd = os.open("softwareTesting.txt", os.O_RDONLY)

if (fd == -1):
    print("Open() was failed - errno = \n", errno)
else:
    print("Open() system call executed successfully the file descriptor of opened file is : ", fd)

