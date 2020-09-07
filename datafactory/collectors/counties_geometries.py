import pandas as pd
import geopandas as gpd
import json
import random
from shapely.geometry import Point, Polygon
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import seed_data  # relative-import the *package* containing the templates


class CountiesGeom():

    def __init__(self):
        self.counties_gdf = self.__initiate_counties_as_gepandas_df()

    def __load_county_data_from_package_as_geopandas(self):
        counties_f = pkg_resources.open_text(
            seed_data, 'gz_2010_us_050_00_500k.json')
        counties_gpd = gpd.read_file(counties_f)
        return counties_gpd

    def __set_up_gdf_as_lokup(self, gdf):
        gdf = gdf.rename(columns={'STATE': 'STATEFP', 'COUNTY': 'COUNTYFP'})
        gdf = gdf.astype({'STATEFP': 'int64', 'COUNTYFP': 'int64'})
        gdf = gdf.set_index(['STATEFP', 'COUNTYFP'])
        return gdf

    def __initiate_counties_as_gepandas_df(self):
        gdf = self.__load_county_data_from_package_as_geopandas()
        gdf = self.__set_up_gdf_as_lokup(gdf)
        return gdf

    def __convert_to_pandas_df(self, data_json):
        pdf = pd.json_normalize(data_json, 'features', max_level=2)
        pdf = pdf.rename(columns={'properties.STATE': 'STATEFP',
                                  'properties.NAME': 'NAME', 'properties.COUNTY': 'COUNTYFP'})
        pdf = pdf.astype({'STATEFP': 'int64', 'COUNTYFP': 'int64'})
        pdf = pdf.set_index(['STATEFP', 'COUNTYFP'])
        return pdf

    def get_geometry_by_fips(self, fips):
        try:
            fips_state = int(fips[:2])
            fips_county = int(fips[-3:])
            row_as_list = list(self.counties_gdf.loc[(fips_state, fips_county)])
            geometry = row_as_list[4]
            return geometry
        except KeyError:
            return None

    def get_name_category_geometry_by_fips(self, fips):
        try:
            fips_state = int(fips[:2])
            fips_county = int(fips[-3:])
            row_as_list = list(self.counties_gdf.loc[(fips_state, fips_county)])
            geometry = row_as_list[4]
            county_name = row_as_list[1]
            category = row_as_list[2]
            return county_name, category, geometry
        except KeyError:
            return None, None, None

    def get_n_random_points_within_fips(self, n, fips):
        n_points = []
        geometry = self.get_geometry_by_fips(fips)
        bounds = geometry.bounds
        low_x = bounds[0]
        low_y = bounds[1]
        high_x = bounds[2]
        high_y = bounds[3]
        is_outside = True
        for i in range(n):
            while is_outside:
                x = random.uniform(low_x, high_x)
                y = random.uniform(low_y, high_y)
                p1 = Point(x, y)
                is_outside = not p1.within(geometry)
            n_points.append((p1.x, p1.y))
        return n_points
