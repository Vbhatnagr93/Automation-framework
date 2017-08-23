import logging

class LoggerDemoConsole():
    def testlog(self):

        # Create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create console handler and set level to info
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S %p')

        # Add formatter to console handler -> consoleHandler
        consoleHandler.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(consoleHandler)

        # Logging messages
        logger.debug('Debug Message') #Debug messages are skipped because we set the level to Info
        logger.info('Info Message')
        logger.warning('Warning Message')
        logger.error('Error Message')
        logger.critical('Critical Message')

test = LoggerDemoConsole()
test.testlog()

