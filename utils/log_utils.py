import logging



	##日志配置，自动化测试日志配置用这个。另外一个logger.py暂时不管
    # create logger
import os

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)

ch = logging.FileHandler(filename='mylog.log', encoding="utf-8")
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)