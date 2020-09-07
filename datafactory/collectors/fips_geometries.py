import pandas as pd
import random
from . import Fips, CountiesGeom

class FipsGeometries():
    __fips_lkp = Fips()
    __geometries_lkp = CountiesGeom()

    def __init__(self):
        self.fips_lkp = self.__class__.__fips_lkp
        self.geometries_lkp = self.__class__.__geometries_lkp

    def get_geometry_by_fips(self, fips):
        geometry = self.geometries_lkp.get_geometry_by_fips(fips)
        return geometry




       
    
