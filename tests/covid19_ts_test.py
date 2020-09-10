import unittest
import datafactory as df

class TestCovid19TS(unittest.TestCase):
    
    def test_constructor(self):
        tsf = df.Covid19TS()
        tsf.generate_random_points_per_day_and_fips('070808','00101', 4)