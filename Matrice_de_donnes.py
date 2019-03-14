from getohlc import get_ohlc_data_date, get_data
from datetime import datetime


class MatriceCrypto:
    """ Objet aggrégeant dans l'ordre chronologique des
    """

class Indicateurs:
    """Objet contenant les différents indicateurs :
    - cours
    - RSI
    - SMA
    ...
    """
    def __init__(self, date, cours, rsi, sma):
        self._dict={"date":date,"cours":cours,"rsi":rsi,"sma":sma}

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
        else:
            self.ajouter(indicateurs[0])

    def ajouter(self, indicateur):
        self._donnees.update({indicateur.date : indicateur})
