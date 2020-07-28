import unittest
import datafactory.collectors as colls

class TestFips(unittest.TestCase):
    def test_Fips(self):
        fips_lkp = colls.Fips()
        self.assertEqual(fips_lkp, None)

if __name__ == '__main__':
    unittest.main()