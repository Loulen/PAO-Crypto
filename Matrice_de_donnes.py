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

indic=[]
for i in range(20):
    indic.append(Indicateurs(datetime(2019, 3, 6+i, 18, 00, 34), 500+i, 20+i, 30+i, i))
m=MatriceCrypto(indic)
