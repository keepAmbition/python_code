import hashlib
import datetime
import random


def encryption(string):
    """
    :param string:
    :return:
    """
    hash = hashlib.md5(b"homework")
    hash.update(string.encode("utf-8"))
    result = hash.hexdigest()
    return result


def date_conversion(weekday_num):
    """
    :param weekday_num:
    :return:
    """
    china_weekday = ('一', '二', '三', '四', '五', '六', '日')
    num = int(weekday_num)
    return china_weekday[num]


def create_new_id():
    """
    :return:
    """
    new_credit_id = ""
    for i in range(10):
        a = str(random.randint(1, 9))
        new_credit_id += a
    return new_credit_id


time = datetime.datetime.now()
week_time = date_conversion(time.weekday())
date_time = time.date()
time_time = time.time().strftime("%H:%M:%S")

