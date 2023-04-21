import os

with open("softwareTesting.txt", "rb") as file:
    os.lseek(file.fileno(), 10, os.SEEK_SET)
    buffer = os.read(file.fileno(), 5)
    print(buffer)


