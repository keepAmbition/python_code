import json
import sys
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path1 = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

tables = ["sl.db", "ul.db", "cl.db"]
sl_path = os.path.join(path1, tables[0])
ul_path = os.path.join(path1, tables[1])
cl_path = os.path.join(path1, tables[2])


def load_sl():
    """
    :return:
    """
    with open(sl_path, "r+") as f:
            return json.load(f)


def load_ul():
    """
    :return:
    """
    with open(ul_path, "r+") as f:
            return json.load(f)


def load_cl():
    """
    :return:
    """
    with open(cl_path, "r+") as f:
            return json.load(f)


def dumps_cl(cl_dict):
    """
    :param cl_dict:
    :return:
    """
    cl_path1 = os.path.join(path1, tables[2]+"1")
    with open(cl_path1, "w", encoding="utf-8")as fw:
        fw.write(json.dumps(cl_dict))
        os.remove(cl_path)
        fw.close()
        os.rename(cl_path1, cl_path)


def dumps_ul(ul_dict):
    """
    :param ul_dict:
    :return:
    """
    ul_path1 = os.path.join(path1, tables[1]+"1")
    with open(ul_path1, "w", encoding="utf-8")as fw:
        fw.write(json.dumps(ul_dict))
        fw.flush()
        os.remove(ul_path)
        fw.close()
        os.rename(ul_path1, ul_path)