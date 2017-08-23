import logging
import logging.config

class LoggerDemoConf():

    def TestLog(self):
        # Create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        #Logging messages
        logger.debug('Debug Message')  # Debug messages are skipped because we set the level to Info
        logger.info('Info Message')
        logger.warning('Warning Message')
        logger.error('Error Message')
        logger.critical('Critical Message')

demo = LoggerDemoConf()
demo.TestLog()




