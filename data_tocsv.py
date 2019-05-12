#!/usr/bin/python3
# -*- coding: utf-8 -*-
from getohlc import get_price_hourly
import pandas as pd
from indicateurs import ema, rsi

def data_frame_annee(annee=2018, monnaie='BTC', ema_period=10, rsi_period=14, hours_per_file=168):
    data=get_price_hourly(monnaie, since='1/1/'+str(annee), to='1/1/'+str(annee+1))
    data=data[::-1]
    ema_data=[]
    rsi_data=[]
    for i in range(ema_period):
        ema_data.append(0)
    for i in range(rsi_period):
        rsi_data.append(0)
    ema_data.extend(ema(list(data['Prix']),period=ema_period))
    rsi_data.extend(rsi(list(data['Prix']),period=rsi_period))
    data['ema'] = pd.Series(ema_data, index=data.index)
    data['rsi'] = pd.Series(rsi_data, index=data.index)
    # on retire les 250 premières valeurs pour tenir compte de l'actualisation du rsi
    data=data[rsi_period+250:]
    hours_left=len(data)
    file_number=1
    while hours_left>hours_per_file:
        data[len(data)-hours_left:len(data)-hours_left+hours_per_file].to_csv('./'+str(annee)+'/'+str(file_number))
        file_number=file_number+1
        hours_left=hours_left-hours_per_file


