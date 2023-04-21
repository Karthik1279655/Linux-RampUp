#!/usr/bin/python3
import os

filename = "example.txt"

try:
    # Open the file using the open() system call
    fd = os.open(filename, os.O_RDWR)
except FileNotFoundError:
    print(f"Error: file '{filename}' not found.")
except PermissionError:
    print(f"Error: permission denied to open file '{filename}'.")
else:
    # Write to the file using the file descriptor
    os.write(fd, b"This is an example.")
    # Close the file using the file descriptor
    os.close(fd)

