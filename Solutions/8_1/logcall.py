# logcall.py

import logging
import os

def logged(func):
    # If logging not enabled, return the original function unwrapped
    if 'LOGDISABLE' in os.environ:
        return func
    print("Adding logging to", func.__name__)
    log = logging.getLogger(func.__module__)
    def wrapper(*args,**kwargs):
        log.debug("%s", func.__name__)
        return func(*args,**kwargs)
    return wrapper

        
