import unittest
import datafactory as df


class TestCovid19Collector(unittest.TestCase):
    
    def test_constructor(self):
       c19c = df.Covid19Collector()
       self.assertIsNotNone(c19c)

    def test_covid19collector_iterator(self):
        c19c = df.Covid19Collector()
        iterator = iter(c19c)
        row_count = 0
        for i in iterator:
            row_count+=1
        self.assertLess(0, row_count)