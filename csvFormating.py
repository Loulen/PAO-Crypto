#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import os

def csvRead(path):
    with open(path, newline='') as f:
        reader=csv.reader(f)
        currenciesName=[]
        currencies=[]
        for row in reader:
            currencies.append(row)
            if row[0] not in currenciesName:
                currenciesName.append(row[0])
    createDir(currencies)


def createDir(list):
    from datetime import datetime, timezone
    for item in list[1:]:
        if int(item[1])>1000000000000:
            item[1]=int(item[1])//1000
        # item[1]=datetime.fromtimestamp(int(item[1]), timezone.utc)
        path='./'+item[0]
        if not os.path.isdir(path):
            os.mkdir(path)
        path=path+'/'+item[0]+'.csv'
        with open(path, 'a', newline='') as f:
            writer=csv.writer(f)
            writer.writerow(item)
