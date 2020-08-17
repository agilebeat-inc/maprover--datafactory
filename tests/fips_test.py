import unittest
import datafactory as df


class TestFips(unittest.TestCase):

    def test_query_by_fips(self):
        fips = df.Fips()
        state, county = fips.get_state_and_county_by_fips('01007')
        self.assertEqual(state, 'AL')
        self.assertEqual(county, 'Bibb County')

    def test_query_by_fips_not_found(self):
        fips = df.Fips()
        state, county = fips.get_state_and_county_by_fips('01008')
        self.assertEqual(state, None)
        self.assertEqual(county, None)

    def test_query_by_state_county(self):
        fips = df.Fips()
        fips_code = fips.get_fips_code_by_names('AL', 'Blount County')
        self.assertEqual(fips_code, '01009')

    def test_query_by_state_county_not_found(self):
        fips = df.Fips()
        fips_code = fips.get_fips_code_by_names('AL', 'Weather County')
        self.assertEqual(fips_code, None)


if __name__ == '__main__':
    unittest.main()
