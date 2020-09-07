import unittest
import datafactory as df
import random
from shapely.geometry import Point, Polygon


class TestFipsGeometries(unittest.TestCase):

    def get_random_point(self, geometry):
        bounds = geometry.bounds
        low_x = bounds[0]
        low_y = bounds[1]
        high_x = bounds[2]
        high_y = bounds[3]
        is_outside = True
        while is_outside:
            x = random.uniform(low_x, high_x)
            y = random.uniform(low_y, high_y)
            p1 = Point(x, y)
            is_outside = not p1.within(geometry)
        print(bounds)
        print(p1)

    def test_get_geometry_by_fips(self):
        fg = df.FipsGeometries()
        geometry = fg.get_geometry_by_fips('01007')
        self.get_random_point(geometry)