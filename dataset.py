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
