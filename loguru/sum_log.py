from loguru import logger
import time


def sum(a,b):
    try:
        logger.debug(f"Func(sum) arguments: {a} and {b} ")
        time_before =time.time()
        sum =a+b
        time_after =time.time()
        logger.debug(f"Result: {sum}" )
        logger.debug(f"Time: {time_after - time_before} sec.")
        logger.info("Func(sum) done!")
    except:
        logger.error("Func(sum) don't work!")
    return sum

sum(2,7)
