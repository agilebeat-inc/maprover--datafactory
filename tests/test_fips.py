import unittest
from datafactory import Fips

class TestFips(unittest.TestCase):
    def test_Fips(self):
        fips_lkp = Fips()
        self.assertEqual(fips_lkp, None)

if __name__ == '__main__':
    unittest.main()