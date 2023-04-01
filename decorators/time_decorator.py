import time
from loguru import logger

def time_func(func):
    def times():
        tb= time.time()
        func()
        ta= time.time()
        logger.info(f"Function time: {ta - tb} sec.")
    return times

def test():
    print("Hello World")
    
test()