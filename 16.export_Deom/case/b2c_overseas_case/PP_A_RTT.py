import unittest

from foo.B2C_Export_Logic import B2cExport


class TestPPARTT(unittest.TestCase):
    """
    测试case,代理采购+成人+往返中转
    """
    def setUp(self):
        self.start = B2cExport()

    def tearDown(self):
        pass

    def test_start(self):
            self.start.b2c_transfer_flight_logic("PP", "PP_A_RT", "overseas", "b2c")

if __name__ == '__main__':
    unittest.main()