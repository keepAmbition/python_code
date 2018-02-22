import unittest

from foo.B2C_Export_Logic import B2cExport


class TestPFACRTS(unittest.TestCase):
    """
    测试case,平台采购+成人+儿童+往返直飞
    """

    def setUp(self):
        self.start = B2cExport()

    def tearDown(self):
        pass

    def test_start(self):
            self.start.b2c_direct_flight_logic("PF", "PP_AC_RT", "overseas", "b2c")

if __name__ == '__main__':
    unittest.main()