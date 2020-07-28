import pandas as pd
import numpy as np
import json

def significant_event(x):
    t = x.copy()
    bollinger_band_std = 2.0
    t['new_cases'] = t.cases - t.cases.shift(periods=1).fillna(0)
    t['rolling_new_cases_mean'] = t.new_cases.rolling(7).mean()
    t['rolling_new_cases_std'] = t.new_cases.rolling(7).std()
    t['rolling_new_cases_extreme_high'] = t.rolling_new_cases_mean + t.rolling_new_cases_std * bollinger_band_std
    t['rolling_new_cases_extreme_low'] = t.rolling_new_cases_mean - t.rolling_new_cases_std * bollinger_band_std
    t = t.fillna(0)
    t['new_cases_significance'] = np.logical_or(t.rolling_new_cases_extreme_low > t.new_cases, t.new_cases > t.rolling_new_cases_extreme_high)
    t[:7] = False
    return t

def load_covid_data():
    data = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
    data.date = pd.to_datetime(data.date)
    data_grouped = data.groupby(['fips'])
    data_significant = data_grouped.apply(lambda x: significant_event(x))
    data_significant = data_significant[data_significant.date != False]
    data_significant.to_csv("covid_significant_events.csv", index=False)
    return data_significant

def load_counties_boundries():
    data = None
    with open('/workspaces/covid19-generator/data/gz_2010_us_050_00_500k.json') as f:
        data = json.load(f)
    return data

def convert_to_panda_lookupdf(data_json):
    pdf = pd.json_normalize(data_json, 'features', max_level=2)
    pdf = pdf.rename(columns={'properties.STATE': 'STATE', 'properties.NAME': 'NAME','properties.COUNTY': 'COUNTY'})
    pdf = pdf.set_index(['STATE', 'COUNTY'])
    return pdf



if __name__ == '__main__':
    boundries_json = load_counties_boundries()
    counties_df = convert_to_panda_lookupdf(boundries_json)
