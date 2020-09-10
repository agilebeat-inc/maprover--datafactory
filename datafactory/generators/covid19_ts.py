import datafactory as df
import pandas as pd
import random


class Covid19TS():
    def __init__(self):
        self.__counties_geom = df.CountiesGeom()

    def __get_random_timestamp_within_24(self, date):
        return pd.to_datetime(pd.to_datetime(date).timestamp() + random.randint(0, 24*3600), unit='s')

    def __generate_n_timestamps_for_givendate(self, date, n_cases):
        time_stamps = []
        for _ in range(n_cases):
            time_stamps.append(self.__get_random_timestamp_within_24(date))
        return time_stamps

    def __generate_n_cases_within_given_fips_boundries(self, date, fips, n_cases):
        points = self.__counties_geom.get_n_random_points_within_fips(n_cases, fips)
        timestamps = self.__generate_n_timestamps_for_givendate(date, n_cases)
        cases = [(timestamps[i], points[i], timestamps[i], fips, 1) for i in range(n_cases)]
        print(cases)
        
    def generate_random_points_per_day_and_fips(self, fips, date, count):
        c19 = df.Covid19Collector()
        counter = 0
        for r in iter(c19):
            if counter == 10:
                break
            counter+=1
            date = r[1]
            fips = r[4]
            n_cases = r[5]
            self.__generate_n_cases_within_given_fips_boundries(date, fips, n_cases)


