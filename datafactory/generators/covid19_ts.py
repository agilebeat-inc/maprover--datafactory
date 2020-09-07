import datafactory as df


class Covid19TS():
    def __init__(self):
        self.fips_geometries = df.FipsGeometries()

    def __generate_n_cases_within_given_fips_boundries(self, date, fips, n_cases):
        print(date, fips, n_cases)

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


