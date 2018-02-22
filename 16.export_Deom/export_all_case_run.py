import unittest
import os
import sys
import HTMLTestReportCN

from foo.B2B_Export_Logic import B2BExport
from foo.B2C_Export_Logic import B2cExport
from foo.send_email import SendEmail


class AllExportCase(unittest.TestCase):
    """
     测试case集合类，包含B2B接口平台采购8个case,代理采购8个case, B2C境内接口8个case,B2C境外接口8个case
     参数解释：
     PP:平台代理   PF:采购代理
     A:单个成人    AC:单个成人+单个儿童
    OW:直飞航班   RT:中转航班
    1: 直飞航班   2:中转航班
    a:deva环境
    """
    def setUp(self):
        self.b2b_start = B2BExport()
        self.b2c_start = B2cExport()

    def tearDown(self):
        pass

    # B2B接口平台采购的8个case
    def test_b2b_PF_A_OW_direct(self):
        self.b2b_start.b2b_export_logic("PF", "PP_A_OW", "b2b", 1, "a")

    def test_b2b_PF_A_OW_transit(self):
        self.b2b_start.b2b_export_logic("PF", "PP_A_OW", "b2b", 2, "a")

    def test_b2b_PF_AC_OW_direct(self):
        self.b2b_start.b2b_export_logic("PF", "PP_AC_OW", "b2b", 1, "a")

    def test_b2b_PF_AC_OW_transit(self):
        self.b2b_start.b2b_export_logic("PF", "PP_AC_OW", "b2b", 2, "a")

    def test_b2b_PF_A_RT_direct(self):
        self.b2b_start.b2b_export_logic("PF", "PP_A_RT", "b2b", 1, "a")

    def test_b2b_A_RT_transit(self):
        self.b2b_start.b2b_export_logic("PF", "PP_A_RT", "b2b", 2, "a")

    def test_b2b_AC_RT_direct(self):
        self.b2b_start.b2b_export_logic("PF", "PP_AC_RT", "b2b", 1, "a")

    def test_b2b_PF_AC_RT_transit(self):
        self.b2b_start.b2b_export_logic("PF", "PP_AC_RT", "b2b", 2, "a")

    ###################################################################
    ###################################################################

    #  B2B接口代理采购的8个case
    def test_b2b_PP_A_OW_direct(self):
        self.b2b_start.b2b_export_logic("PP", "PP_A_OW", "b2b", 1, "a")

    def test_b2b_PP_A_OW_transit(self):
        self.b2b_start.b2b_export_logic("PP", "PP_A_OW", "b2b", 2, "a")

    def test_b2b_PP_AC_OW_direct(self):
        self.b2b_start.b2b_export_logic("PP", "PP_AC_OW", "b2b", 1, "a")

    def test_b2b_PP_AC_OW_transit(self):
        self.b2b_start.b2b_export_logic("PP", "PP_AC_OW", "b2b", 2, "a")

    def test_b2b_PP_A_RT_direct(self):
        self.b2b_start.b2b_export_logic("PP", "PP_A_RT", "b2b", 1, "a")

    def test_b2b_PP_A_RT_transit(self):
        self.b2b_start.b2b_export_logic("PP", "PP_A_RT", "b2b", 2, "a")

    def test_b2b_PP_AC_RT_direct(self):
        self.b2b_start.b2b_export_logic("PP", "PP_AC_RT", "b2b", 1, "a")

    def test_b2b_PP_AC_RT_transit(self):
        self.b2b_start.b2b_export_logic("PP", "PP_AC_RT", "b2b", 2, "a")

    ###################################################################
    ###################################################################

    #b2b境内接口的8个case

    def test_domestic_b2c_PP_A_OW_direct(self):
        self.b2c_start.b2c_export_logic("PP", "PP_A_OW", "domestic", "b2c", 1, "a")

    def test_domestic_b2c_PP_A_OW_transit(self):
        self.b2c_start.b2c_export_logic("PP", "PP_A_OW", "domestic", "b2c", 2, "a")

    def test_domestic_b2c_PP_AC_OW_direct(self):
        self.b2c_start.b2c_export_logic("PP", "PP_AC_OW", "domestic", "b2c", 1, "a")

    def test_domestic_b2c_PP_AC_OW_transit(self):
        self.b2c_start.b2c_export_logic("PP", "PP_AC_OW", "domestic", "b2c", 2, "a")

    def test_domestic_b2c_PP_A_RT_direct(self):
        self.b2c_start.b2c_export_logic("PP", "PP_A_RT", "domestic", "b2c", 1, "a")

    def test_domestic_b2c_PP_A_RT_transit(self):
        self.b2c_start.b2c_export_logic("PP", "PP_A_RT", "domestic", "b2c", 2, "a")

    def test_domestic_b2c_PP_AC_RT_direct(self):
        self.b2c_start.b2c_export_logic("PP", "PP_AC_RT", "domestic", "b2c", 1, "a")

    def test_domestic_b2c_PP_AC_RT_transit(self):
        self.b2c_start.b2c_export_logic("PP", "PP_AC_RT", "domestic", "b2c", 2, "a")

    ###################################################################
    ###################################################################

    #b2b境外接口的8个case
    def test_overseas_b2c_PP_A_OW_direct(self):
        self.b2c_start.b2c_export_logic("PP", "PP_A_OW", "overseas", "b2c", 1, "a")

    def test_overseas_b2c_PP_A_OW_transit(self):
        self.b2c_start.b2c_export_logic("PP", "PP_A_OW", "overseas", "b2c", 2, "a")

    def test_overseas_b2c_PP_AC_OW_direct(self):
        self.b2c_start.b2c_export_logic("PP", "PP_AC_OW", "overseas", "b2c", 1, "a")

    def test_overseas_b2c_PP_AC_OW_transit(self):
        self.b2c_start.b2c_export_logic("PP", "PP_AC_OW", "overseas", "b2c", 2, "a")

    def test_overseas_b2c_PP_A_RT_direct(self):
        self.b2c_start.b2c_export_logic("PP", "PP_A_RT", "overseas", "b2c", 1, "a")

    def test_overseas_b2c_PP_A_RT_transit(self):
        self.b2c_start.b2c_export_logic("PP", "PP_A_RT", "overseas", "b2c", 2, "a")

    def test_overseas_b2c_PP_AC_RT_direct(self):
        self.b2c_start.b2c_export_logic("PP", "PP_AC_RT", "overseas", "b2c", 1, "a")

    def test_overseas_b2c_PP_AC_RT_transit(self):
        self.b2c_start.b2c_export_logic("PP", "PP_AC_RT", "overseas", "b2c", 2, "a")


if __name__ == '__main__':
    # module_name = os.path.basename(sys.argv[0]).split(".")[0]
    # module = __import__(module_name)
    path = os.path.dirname(__file__)
    # fp = open(os.path.join(path, "report.html"), "wb")
    # runner = HTMLTestReportCN.HTMLTestRunner(stream=fp)
    # all_suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    # runner.run(all_suite)
    # fp.close()
    # s = SendEmail()
    # s.send_email()
    os.remove(os.path.join(os.path.join(path, "log"), "B2CExport_log"))
    os.remove(os.path.join(os.path.join(path, "log"), "B2BExport_log"))