#!/usr/bin/python3

import time

def timeit_decorator(function):

    def wrapper():

        start_time = time.process_time()
        print(f"Starting Time : {start_time} seconds")

        result = function()
        end_time = time.process_time()
        print(f"Ending Time : {end_time} seconds")

        print(f"Execution time: {end_time - start_time} seconds")
        
        return result
    
    return wrapper


@timeit_decorator
def slow_function():
    print(f"Halt the system.......")
    time.sleep(2)
    return "\nExecution Done"

print(slow_function())

