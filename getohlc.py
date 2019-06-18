import krakenex
from pykrakenapi import KrakenAPI
from cryptocompareperso import get_historical_price_hour
from datetime import datetime, timedelta,date, time
import pandas as pd

def get_ohlc_data_date(data, moment=None):
    """Fonction retournant une DataFrame contenant une unique valeur,
    la plus proche possible du moment choisi à partir des données data."""
    offset=timedelta(hours=1)
    t1= time((moment-offset).hour, (moment-offset).minute, (moment-offset).second)
    t2= time(moment.hour, moment.minute, moment.second)
    tempdate=date(moment.year, moment.month, moment.day)
    temp=data.filter(like=tempdate.isoformat(), axis=0)
    return temp.between_time(t1,t2)

def get_data(monnaie ='XXBTZEUR', interval=60, since=None):
    """Renvoie une DataFrame de max 720 valeurs selon :
        - la paire de monnaie (monnaie) choisie sous forme de string. Par
        defaut elle vaut 'XXBTZEUR' et renvoie donc la valeur du Bitcoin en Euros.
        Si la paire pose problème, tenter de rajouter un X devant la cryptomonaie et
        un Z devant la monnaie "classique", comme pour la valeur par défaut. (se référer
        aux monnaies disponibles sur la plateforme Kraken)
        - l'intervalle (interval) en minutes, qui représente l'intervalle temporel
        entre deux entrées de la DataFrame. Par défaut elle vaut 60.
        - la date de début (since). Par défaut la fonction renvoie
        les 720 dernières valeurs selon l'intervalle choisi.
    """
    api = krakenex.API()
    k = KrakenAPI(api)
    ohlc = k.get_ohlc_data(monnaie, interval, since)
    return ohlc[0]

def get_range(interval='4H'):
    """sert pas a grand chose franchement."""
    dates_tab=pd.date_range('2018-01-01', end=datetime.now(),freq=interval).to_pydatetime()
    data=get_data()
    infos=pd.DataFrame()
    for moment in dates_tab:
        infos=infos.append(data.filter(like=moment.isoformat(' '), axis=0))
    return infos


def get_price_hourly(monnaieCrypto='BTC', monnaieFiat='EUR', since='1/1/2018', to='1/08/2018'):
    """"""
    dates=pd.date_range(start=since, end=to, freq='1H')
    nbval=len(dates)
    ts={}
    h_price=[]

    # L'API de CryptoCompare nous permet uniquement de récupérer les valeurs horaires par paquets de 2000
    if nbval>2000:
        limit=2000
        while nbval>2000 :
            ts.update({dates[nbval-1]:2000})
            nbval=nbval-2000
    ts.update({dates[nbval-1]:nbval})
    for date, lim in ts.items():
        h_price.extend(get_historical_price_hour(monnaieCrypto, date, monnaieFiat, lim)['Data'])

    cours = {}
    for hour in h_price:
        cours.update({hour['time']:hour['open']})
    return pd.DataFrame.from_dict(cours, orient='index', columns=['Prix'])


