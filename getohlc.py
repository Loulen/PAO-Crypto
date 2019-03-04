import krakenex
from pykrakenapi import KrakenAPI
from datetime import datetime, timedelta,date, time
import pandas as pd

def get_ohlc_data_date(data, moment=None):
    offset=timedelta(hours=1)
    t1= time((moment-offset).hour, (moment-offset).minute, (moment-offset).second)
    t2= time(moment.hour, moment.minute, moment.second)
    tempdate=date(moment.year, moment.month, moment.day)
    temp=data.filter(like=tempdate.isoformat(), axis=0)
    return temp.between_time(t1,t2)

def get_data(interval=60, since=None):
    api = krakenex.API()
    k = KrakenAPI(api)
    ohlc = k.get_ohlc_data('BCHUSD', interval, since)
    return ohlc[0]

def get_range(interval='4H'):
    dates_tab=pd.date_range('2018-01-01', end=datetime.now(),freq=interval).to_pydatetime()
    data=get_data()
    infos=pd.DataFrame()
    for moment in dates_tab:
        infos=infos.append(data.filter(like=moment.isoformat(' '), axis=0))
    return infos

def get_price_open(data) :
    return (data.loc[:,'open']).as_matrix()

def data_matrix(cours)
