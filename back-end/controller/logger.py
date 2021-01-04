import logging
import time
import os

class logger:
    logger = None
    date = None
    path = None
    fh = None # fileHandler

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.date = time.strftime('%Y%m%d', time.localtime(time.time()))
        self.init()

    def init(self,path = None,filename=None):
        '''

        :param filename: 日志路径
        :return:
        '''
        if(filename == None):
            filename = self.date  # 当前时间
        if(path == None):
            self.path = os.path.dirname(os.getcwd()) + '/logs/'

        logFile = self.path + filename + '.log'
        self.fh = logging.FileHandler(logFile, mode="a")
        self.fh.setLevel("INFO")
        # 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        self.fh.setFormatter(formatter)
        # 将logger添加到handler里面
        self.logger.addHandler(self.fh)

    def isNewDay(self):
        if (self.date != time.strftime('%Y%m%d', time.localtime(time.time()))):
            return True
        return False

    def newDayProcess(self,date=None):
        if(date == None):
            date = self.date
        self.date = time.strftime('%Y%m%d', time.localtime(time.time()))
        self.logger.removeHandler(self.fh)
        self.init(date)

    def info(self, text):
        if(self.isNewDay()):
            self.newDayProcess()
        self.logger.info(text)

if __name__ == '__main__':
    log = logger()
    log.info("11111111111111111")
    log.newDayProcess("2test")
    log.info("22222222222222222")