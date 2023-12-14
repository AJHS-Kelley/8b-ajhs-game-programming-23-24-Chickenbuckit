#python performance monitoring modle, Casey Boyce, v0.1
import time

def exec_start():
    start_time = time.time()
    return start_time

def exec_stop():
    stop_time = time.time()
    return stop_time

def exce_time(start_time, stop_time):
    return f"Execution Time: {start_time - stop_time} Seconds.\n"