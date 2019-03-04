#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import date

def obtenirMois(nbjours, annee):

    mois=0
    if nbjours<=31:
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-31
        mois=mois+1

    if annee%4==0:
        if nbjours <=29:
            mois=mois+1
            return (mois, nbjours)
        else:
            mois=mois+1
            nbjours=nbjours-29
    else:
        if nbjours <=28:
            mois=mois+1
            return (mois, nbjours)
        else:
            mois=mois+1
            nbjours=nbjours-28
    if nbjours<=31:#mars
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-31
        mois=mois+1
    if nbjours<=30:#avril
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-30
        mois=mois+1
    if nbjours<=31:#mai
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-31
        mois=mois+1
    if nbjours<=30:#juin
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-30
        mois=mois+1
    if nbjours<=31:#juillet
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-31
        mois=mois+1
    if nbjours<=31:#aout
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-31
        mois=mois+1
    if nbjours<=30:#septembre
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-30
        mois=mois+1
    if nbjours<=31:#oct
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-31
        mois=mois+1
    if nbjours<=30:#novembre
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-30
        mois=mois+1
    if nbjours<=31:#decembre
        mois=mois+1
        return (mois, nbjours)
    else:
        nbjours=nbjours-31
        mois=mois+1
    return (mois, nbjours)


def epoch2date(n):
    from datetime import date

    nbannees=1970+n//31536000000
    n=n%31536000000
    nbjours=1+n//86400000-(nbannees-1970)//4
    if nbjours<=0:
        nbjours=1
    #vu que la prochaine année qu'on devra prendre en compte comme ça c'est 2100 on est tranquilles un peu
    tempdate=obtenirMois(nbjours,nbannees)
    # n=n%86400-nbannees//4+1
    # nbheures=n//3600
    # n=n%3600
    # nbminutes=n//60
    # n=n%60
    # nbsecondes=n
    d=date(nbannees,tempdate[0],tempdate[1])
    return d
