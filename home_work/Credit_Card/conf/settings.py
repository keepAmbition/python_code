import os
import sys
# __file__当前文件
# Credit_Card主目录
PATH_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH_DIR)

DATABASE = dict(engineer="file", dbpath=os.path.join(PATH_DIR, "datebase"))


# 日志文件存放路径
log_file_name = {"operation_bill": "error_bill_log",
                 "consume": "consume_log",
                 "shopping": "shopping_log",
                 "error_shopping": "error_shopping_log",
                 "operation": "operation_log",
                 "bill": "bill_log"}

# 账单报表文件路径
REPORT_PATH = os.path.join(PATH_DIR, "report")

# 转账、提现手续费
SERVICE_CHARGE = 0.05
