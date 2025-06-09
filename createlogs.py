import logging
from functools import wraps
"""
logging.info("This is info log")
logging.debug("This is debug log")
logging.warning("This is warning log")
logging.error("This is error log")
logging.critical("This is critical log")
"""


logging.basicConfig(filename="mylogs.txt",
                    level=logging.DEBUG,
                    format="%(asctime)s %(filename)s %(funcName)s %(lineno)d %(message)s",
                    datefmt="%d/%m/%Y %H:%M:%S"
                    )

def add(x,y):
    x=99
    logging.info(f"Addition of {x} and {y} is {x+y}")
    return x+y

def sub(x,y):
    logging.debug(f"subtration of {x} and {y} is {x-y}")
    return x-y


print("From createlogs.py", add(100,200))
#print(sub(600,200))

"""
def mylogs(funcp):
    import logging
    logging.basicConfig(filename="mylogs.txt",
                        level=logging.DEBUG,
                        format="%(asctime)s %(filename)s %(message)s",
                        datefmt="%d/%m/%Y %H:%M:%S"
                        )
    @wraps(funcp)
    def wrapper(*args,**kwargs):
        result=funcp(*args,**kwargs)
        logging.info(f"operation {funcp.__name__}  Result of {args} is {result}")
        return result
    return wrapper

@mylogs
def add(x,y):
    return x+y

@mylogs
def sub(x,y):
    return x-y

print(add(100,200))
print(sub(600,200))
"""
