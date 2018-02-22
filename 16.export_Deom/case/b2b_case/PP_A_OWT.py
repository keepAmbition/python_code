import unittest

from foo.B2B_Export_Logic import B2BExport


class TestPFAOWS(unittest.TestCase):
    """
    测试case,平台采购+成人+单程直飞
    """
    def setUp(self):
        self.start = B2BExport()

    def tearDown(self):
        pass

    def test_start(self):
            self.start.b2b_export_logic("PP", "PP_A_OW", "b2b", 2)
if __name__ == '__main__':
    unittest.main()
