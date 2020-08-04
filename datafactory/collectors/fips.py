import pandas as pd
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import seed_data  # relative-import the *package* containing the templates




class Fips():

    def __init__(self):
        self.fips_df = self.load_data_frame_from_package()
        self.data_geojson = None

    def load_data_frame_from_package(self):
        sd_f = pkg_resources.open_text(seed_data, 'FIPS_Lookup_2020_07.csv')
        fips_df = pd.read_csv(sd_f)
        return fips_df