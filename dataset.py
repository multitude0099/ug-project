import warnings
from datetime import datetime

import pandas as pd

warnings.filterwarnings("ignore")


class suny_international:
    """
    
    """
    atmospheric_factors = ('Cloud Type', 'Dew Point', 'Temperature', 'Pressure',
       'Relative Humidity', 'Solar Zenith Angle', 'Precipitable Water',
       'Wind Direction', 'Wind Speed', 'Fill Flag')

    @staticmethod
    def load_data (start='08:00:00',end='18:00:00'):
        df = pd.read_csv('data/suny_international/full_data.csv',
                         skiprows=2, parse_dates=[['Year', 'Month', 'Day', 'Hour', 'Minute']],
                         index_col=0, date_parser=lambda x: datetime.strptime(x, '%Y %m %d %H %M'))
        df.index.name = 'date'
        df = df.iloc[:, :16]
        df = df.between_time(start, end)
        return df


class hi_seas:
    """
    These datasets are meteorological data from the HI-SEAS weather station from four months 
    (September through December 2016) between Mission IV and Mission V.

    For each dataset, the fields are:

    A row number (1-n) useful in sorting this export's results 
    The UNIX time_t date (seconds since Jan 1, 1970). Useful in sorting this export's results 
    with other export's results The date in yyyy-mm-dd format 
    The local time of day in hh:mm:ss 24-hour format
    The numeric data, if any (may be an empty string) The text data, if any (may be an empty string)

    The units of each dataset are:

    Solar radiation: watts per meter^2

    Temperature: degrees Fahrenheit

    Humidity: percent
    Barometric pressure: Hg
    Wind direction: degrees
    Wind speed: miles per hour
    Sunrise/sunset: Hawaii time

    """


    @staticmethod
    def load_data():
        df = pd.read('data/hi_seas/data.csv')
        df=df.drop(['UNIXTime','Data','Time','TimeSunRise','TimeSunSet'],axis=1)
        return df
