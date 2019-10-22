import warnings
from datetime import datetime

import pandas as pd

warnings.filterwarnings("ignore")

start = '08:00:00'
end = '18:00:00'


def suny_international():
    df = pd.read_csv('data/full_data.csv', skiprows=2, parse_dates=[['Year', 'Month', 'Day', 'Hour', 'Minute']],
                     index_col=0, date_parser=lambda x: datetime.strptime(x, '%Y %m %d %H %M'))
    df.index.name = 'date'
    df = df.iloc[:, :16]
    # df = df.drop( ['DHI', 'DNI', 'Clearsky DHI', 'Clearsky DNI',
    # 'Clearsky GHI', 'Precipitable Water', 'Fill Flag', 'Cloud Type'],axis=1)
    # df = df.iloc[:,   :8]
    # df.columns = ['ghi', 'dew', 'temp', 'press', 'rel_humid', 'zenith_ang', 'wnd_dir', 'wnd_spd']
    # df = df[['dew', 'temp', 'press', 'rel_humid', 'zenith_ang', 'wnd_dir', 'wnd_spd', 'ghi']]
    df = df.between_time(start, end)
    # df.columns = ['dew', 'temp', 'press', 'rel_humid', 'zenith_ang', 'wnd_dir', 'wnd_spd', 'ghi']
    return df


class hi_seas:
    """
    These datasets are meteorological data from the HI-SEAS weather station from four months (September through December 2016) between Mission IV and Mission V.

    For each dataset, the fields are:

    A row number (1-n) useful in sorting this export's results The UNIX time_t date (seconds since Jan 1, 1970). Useful in sorting this export's results with other export's results The date in yyyy-mm-dd format The local time of day in hh:mm:ss 24-hour format The numeric data, if any (may be an empty string) The text data, if any (may be an empty string)

    The units of each dataset are:

    Solar radiation: watts per meter^2

    Temperature: degrees Fahrenheit

    Humidity: percent
    Barometric pressure: Hg
    Wind direction: degrees
    Wind speed: miles per hour
    Sunrise/sunset: Hawaii time

    """


    @classmethod
    def load_data():
        pass
