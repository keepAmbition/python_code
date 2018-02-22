from conf import action_registers
from modules import utils, views


def help_msg():
    """
    打印帮助信息
    :return:
    """
    print("\033[31;1mAvailable commands:\033[0m")
    for key in action_registers.actions:
        print("\t", key)


def execute_from_command_line(argvs):
    """
    执行命令行
    :param argvs:参数
    :return:
    """
    if len(argvs) < 2:
        help_msg()
        exit()
    if argvs[1] not in action_registers.actions:
        utils.print_err("Command [%s] does not exist!" % argvs[1], quit=True)
    action_registers.actions[argvs[1]](argvs[1:])