import logging
import os
import sys

log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(log_path)


def log_print(log):
    """
    指定文件打印日志
    :param log 需打印的日志
    :return 返回logger 对象
    """
    # 创建一个logger对象
    logger = logging.getLogger("test.log")
    logger.setLevel(logging.DEBUG)

    # 创建一个向屏幕输入的handler对象
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 创建一个像文件输入的handler对象
    log_file = os.path.join(os.path.join(log_path, "log"), "log")
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    # 设置log输入格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # logger，添加handler对象
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.info(log)
    #  在记录日志之后移除句柄, 不然会重复打印日志
    logger.removeHandler(ch)
    logger.removeHandler(fh)
    return logger