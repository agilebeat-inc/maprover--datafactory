import unittest
import datafactory as df

class TestFips(unittest.TestCase):

    def test_upper(self):
        fips = df.Fips()
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()