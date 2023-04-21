#!/usr/bin/python3
import os

file = open("/home/ee212783/UdemyLearning/RegularExpressions.txt", "+")

os.lseek(file, 0, os.SEEK_END)
end_position = os.lseek(file, 0, os.SEEK_CUR)

os.lseek(file, 0, os.SEEK_SET)
start_position = os.lseek(file, 0, os.SEEK_CUR)

print(f"Start Postion : {start_position}")
print(f"End Position : {end_position}")

os.close(file)


