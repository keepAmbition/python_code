import logging
import os
import sys
import datetime
print(os.getcwd())

log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(log_path)


class LOG(object):
    """
    日志打印类
    """
    def __init__(self):
        self.now_time = datetime.datetime.now().strftime("%Y%m%d%H%M")

    def log_info(self, *args):
        """
        根据传入参数打印普通
        :param arg[0]log的功能模块名，arg[1] 保存log的文件名，arg[2]要打印的日志内容
        :return 返回logger 对象
        """
        # 创建一个logger对象
        logger = logging.getLogger(args[0])
        logger.setLevel(logging.DEBUG)

        # 创建一个向屏幕输入的handler对象
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 创建一个像文件输入的handler对象
        log_file = os.path.join(os.path.join(log_path, "log"), args[1])
        fh = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        # 设置log输入格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # logger，添加handler对象
        logger.addHandler(ch)
        logger.addHandler(fh)
        logger.info(args[2])
        #  在记录日志之后移除句柄, 不然会重复打印日志
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        return logger

    def log_warning(self, *args):
        """
        根据传入参数失败日志
        :param arg[0]log的功能模块名，arg[1] 保存log的文件名，arg[3]要打印的日志内容
        :return 返回logger 对象
        """
        # 创建一个logger对象
        logger = logging.getLogger(args[0])
        logger.setLevel(logging.DEBUG)

        # 创建一个向屏幕输入的handler对象
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 创建一个像文件输入的handler对象
        log_file = os.path.join(os.path.join(log_path, "log"), args[1])
        fh = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        # 设置log输入格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # logger，添加handler对象
        logger.addHandler(ch)
        logger.addHandler(fh)
        logger.warning(args[2])
        #  在记录日志之后移除句柄, 不然会重复打印日志
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        return logger

# if __name__ == "__main__":
