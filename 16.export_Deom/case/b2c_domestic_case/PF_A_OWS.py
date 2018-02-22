import unittest

from foo.B2C_Export_Logic import B2cExport


class TestPFAOWS(unittest.TestCase):
    """
    测试case,平台采购+成人+单程直飞
    """
    def setUp(self):
        self.b2c_start = B2cExport()

    def tearDown(self):
        pass

    # def test_domestic_b2c_PP_A_OW_direct(self):
    #     self.b2c_start.b2c_export_logic("PF", "PP_A_OW", "domestic", "b2c", 1, "a")
    #
    # def test_domestic_b2c_PP_A_OW_transit(self):
    #     self.b2c_start.b2c_export_logic("PF", "PP_A_OW", "domestic", "b2c", 2, "a")
    #
    # def test_domestic_b2c_PP_AC_OW_direct(self):
    #     self.b2c_start.b2c_export_logic("PF", "PP_AC_OW", "domestic", "b2c", 1, "a")
    #
    def test_domestic_b2c_PP_AC_OW_transit(self):
        self.b2c_start.b2c_export_logic("PF", "PP_AC_OW", "domestic", "b2c", 2, "a")

    # def test_domestic_b2c_PP_A_RT_direct(self):
    #     self.b2c_start.b2c_export_logic("PF", "PP_A_RT", "domestic", "b2c", 1, "a")

    # def test_domestic_b2c_PP_A_RT_transit(self):
    #     self.b2c_start.b2c_export_logic("PF", "PP_A_RT", "domestic", "b2c", 2, "a")

    def test_domestic_b2c_PP_AC_RT_direct(self):
        self.b2c_start.b2c_export_logic("PF", "PP_AC_RT", "domestic", "b2c", 1, "a")

    def test_domestic_b2c_PP_AC_RT_transit(self):
        self.b2c_start.b2c_export_logic("PF", "PP_AC_RT", "domestic", "b2c", 2, "a")

if __name__ == '__main__':
        unittest.main()
