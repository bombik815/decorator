import logging
import os.path

''' Декоратор логирование запросов '''
def decorator(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(format='Date-Time : %(asctime)s : %(funcName)s :  %(message)s', \
                            datefmt='%d-%b-%y %H:%M:%S',
                            level = logging.DEBUG,
                            filename='log_file.log')
        path_log = os.path.abspath('log_file.log')
        logging.info(func.__name__)
        logging.info(path_log)
        logging.info(args[1])
        return func(*args, **kwargs)
    return wrapper