import pandas as pd

URL_COVID19_CSV = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"


class Covid19Collector():
    def __init__(self):
        self.covid19_df = self.__load_covid_data()

    def __load_covid_data(self):
        covid19_df = pd.read_csv(URL_COVID19_CSV, dtype={'date': str,
                                                         'county': str,
                                                         'state': str,
                                                         'fips': str,
                                                         'cases': 'int64',
                                                         'deaths': 'int64'})
        covid19_df.date = pd.to_datetime(covid19_df.date)
        return covid19_df

    def __iter__(self):
        self.iterator = self.covid19_df.itertuples(index=True, name='Pandas')
        return self.iterator

    def __next__(self):
        self.iterator.next()
