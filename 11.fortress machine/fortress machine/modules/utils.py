import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def print_err(msg, quit=False):
    """
    打印错误信息
    :param msg:信息
    :param quit:标志，True时打印错误信息程序不退出，False时，打印错误日志退出
    :return:
    """
    output = "\033[31;1mError: %s\033[0m" % msg
    if quit:
        exit(output)
    else:
        print(output)


def yaml_parser(yaml_filename):
    """
    将yaml文件中的信息序列化并返回
    :param yaml_filename:yaml文件
    :return:
    """
    try:
        yaml_file = open(yaml_filename, 'r')
        data = yaml.load(yaml_file)
        return data
    except Exception as e:
        print_err(e)