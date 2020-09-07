import pandas as pd
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import seed_data  # relative-import the *package* containing the templates


class Fips():

    def __init__(self):
        self.fips_df = self.__load_data_frame_from_package()
        copy_fips_df = self.fips_df.copy(deep=True)
        self.statecountyname_idf, self.statecountycode_idf = self.__create_lookups(
            copy_fips_df)
        self.data_geojson = None

    def __load_data_frame_from_package(self):
        sd_f = pkg_resources.open_text(seed_data, 'st00_all_cou.csv')
        fips_df = pd.read_csv(sd_f)
        return fips_df

    def __create_lookups(self, fips_df):
        state_countyname_idf = fips_df.copy(deep=True)
        state_countyname_idf = state_countyname_idf.set_index(
            ['STATE', 'COUNTYNAME'])
        state_countycode_idf = fips_df.set_index(['STATEFP', 'COUNTYFP'])
        return state_countyname_idf, state_countycode_idf

    def get_fips_code_by_names(self, state_name, county_name):
        try:
            print(self.statecountyname_idf.head())
            row_as_list = list(
                self.statecountyname_idf.loc[(state_name, county_name)])
            state_code = str(row_as_list[0]).zfill(2)
            county_code = str(row_as_list[1]).zfill(3)
            fips_code = state_code + county_code
        except KeyError:
            return None
        return fips_code

    def get_state_and_county_by_fips(self, fips):
        try:
            fips_state = int(fips[:2])
            fips_county = int(fips[-3:])
            row_as_list = list(
            self.statecountycode_idf.loc[(fips_state, fips_county)])
        except KeyError:
            return None, None
        return row_as_list[0], row_as_list[1]
