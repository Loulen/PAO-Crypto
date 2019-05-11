from getohlc import get_ohlc_data_date, get_data
from datetime import datetime
from pandas import DataFrame

class Indicateurs:
    """Objet contenant les différents indicateurs :
    - cours
    - RSI
    - SMA
    ...
    """
    def __init__(self, date, cours, rsi, sma, ema):
        self._dict={"date":date,"cours":cours,"rsi":rsi,"sma":sma,"ema":ema}

    # ---------------getters / setters ----------

    def __getattr__(self, attr):
        return self._dict[attr]

    def __iter__(self):
        for key in self._dict.keys():
            if isinstance(self._dict[key], datetime):
                yield self._dict[key].isoformat(" ")
            else:
                yield self._dict[key]

    # -------------------Descripteurs-----------------------
    def sma(cours,period=10):
        """Calcule une SMA (Simple Moving Average) sur une period"""
        sma=[]
        for i in range(period,len(cours)):
            sma.append(sum(cours[i-period:i-1])/period) #on a period valeurs du cours
        return sma

    def ema(cours,k=None,period=10):
        """Calcule une EMA (Exponential Moving Average) sur une perdiod
            avec un coefficient d'aplanissement k"""
        if k is None :
            k = 2/(period+1)
        courbe = sma(cours[0:period+1],period)
        for i in range(period+1,len(cours)):
            print(courbe)
            courbe.append(courbe[-1]*(1-k)+cours[i]*k)
        return courbe


    def rsi(cours,period=14):
        gain=float(0)
        loss=float(0)
        for i in range(0,period) :
            diff = (cours[i+1]-cours[i])
            if (diff > 0):
                gain = gain + diff
            else:
                loss = loss + abs(diff)



        AG = gain/period #On utilise la SMA pour moyenner"
        AL = loss/period
        rsi= []
        for i  in range(period,len(cours)-1) :
            if (AL==0):
                RS = 999
            else :
                RS = AG / AL #considérer cas AG (ou AL) = 0
            rsi.append(100 - (100/(1+RS)))
            diff = cours[i+1] - cours[i]
            if (diff > 0):
                AG = (AG*(period-1)+diff)/period
                AL = (AL*13)/period
            else:
                AL = (AL*(period-1)+abs(diff))/period
                AG = (AG*13)/period
        return rsi




class MatriceCrypto:
    """ Objet contenant toutes les données d'une monnaie pour un moment donné,
    càd tous les indicateurs nécéssaires.
    Il se présente sous la forme d'un dictionnaire ayant pour clé une datetime.date
    """

    def __init__(self, *indicateurs):
        self._donnees={}
        if (len(indicateurs)>1):
            for indicateur in indicateurs:
                self.ajouter(indicateur)
        elif (isinstance(indicateurs[0], list)):
            for indicateur in indicateurs[0]:
                self.ajouter(indicateur)
        else:
            self.ajouter(indicateurs[0])

    # ---------------getters / setters ----------

    def __getattr__(self, attr):
        return self._donnees[attr]

    # -------------------------------------------

    def ajouter(self, indicateur):
        self._donnees.update({indicateur.date : list(indicateur)[1:]})

    @property
    def matrice(self):
        """renvoie une matrice d*s avec :
        d : nombre de descripteurs
        s : nombre de séances """
        return DataFrame.from_dict(m._donnees, orient='index',columns=["cours", "rsi", "sma", "ema"])

data = get_data(monnaie ='XXBTZEUR', interval=60, since=None)
cours = data["close"]
cours = cours[::-1]
time = data["time"]
time = time[::-1]
c_sma = sma(cours)
c_ema = ema(cours)
c_rsi = rsi(cours)

#for i in range(20):
    #indic.append(Indicateurs(datetime(2019, 3, 6+i, 18, 00, 34), 500+i, 20+i, 30+i, i))
#m=MatriceCrypto(indic)
lesIndics= Indicateurs()
