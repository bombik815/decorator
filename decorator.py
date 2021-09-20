import logging
import os.path

''' Декоратор логирование запросов '''
def parametrizeddecor(path_log):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.basicConfig(format='Date-Time : %(asctime)s : %(funcName)s :  %(message)s', \
                                datefmt='%d-%b-%y %H:%M:%S',
                                level = logging.DEBUG,
                                filename = path_log)
            #path_log = os.path.abspath('log_file.log')
            result =  func(*args, **kwargs)
            logging.info(func.__name__)
            logging.info(path_log)
            logging.info(args[1])
            logging.info(result)
            return result
        return wrapper
    return decorator