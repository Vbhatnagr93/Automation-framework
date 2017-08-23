import logging
import LoggingPackage.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('Debug Message')
        self.log.info('Info Message')
        self.log.warning('Warning Message')
        self.log.error('Error Message')
        self.log.critical('Critical Message')

    def method2(self):
        self.log.debug('Debug Message')
        self.log.info('Info Message')
        self.log.warning('Warning Message')
        self.log.error('Error Message')
        self.log.critical('Critical Message')

    def method3(self):
        self.log.debug('Debug Message')
        self.log.info('Info Message')
        self.log.warning('Warning Message')
        self.log.error('Error Message')
        self.log.critical('Critical Message')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()