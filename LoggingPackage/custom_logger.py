import inspect
import logging

def customLogger(logLevel):

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    #By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(filename="{0}.log".format(loggerName), mode='w') #Use Streamhandler for console logging
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger