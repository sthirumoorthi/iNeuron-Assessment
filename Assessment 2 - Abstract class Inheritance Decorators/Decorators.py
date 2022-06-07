import time
from functools import wraps
import logging
logging.basicConfig(filename="DecoratorLog.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

def timer(func):
    """
    Calculates the time take to execute a loop of n times.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("... Wrapper function executed ...")
        print("*" * 50)
        print("This is printed before the function is called")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("-- Finished in {:.3f} secs".format(end-start))
        print("This is printed after the function is called")
        print("*" * 50)
        return result
    return wrapper

@timer
def countdown(n):
    """
    Repeat the loop until 'n' value reaches 0 
    """
    try:
        while n > 0:
            n -= 1
    except Exception as err:
            logging.exception(f"Exception occurred during countdown. Error: {err}")

# Main stream
if __name__ == '__main__':
    logging.info("*** Application started ***")
    countdown(10000)
    countdown(1000000)    
    logging.info("*** End of Application process ***")