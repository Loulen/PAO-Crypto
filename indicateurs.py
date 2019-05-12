def sma(cours, period=10):
    """Calcule une SMA (Simple Moving Average) sur une period"""
    sma = []
    for i in range(period, len(cours)):
        # on a period valeurs du cours
        sma.append(sum(cours[i - period:i - 1]) / period)
    return sma

def ema(cours, k=None, period=10):
    """Calcule une EMA (Exponential Moving Average) sur une perdiod
        avec un coefficient d'aplanissement k"""
    if k is None:
        k = 2 / (period + 1)
    courbe = sma(cours[0:period + 1], period)
    for i in range(period + 1, len(cours)):
        courbe.append(courbe[-1] * (1 - k) + cours[i] * k)
    return courbe

def rsi(cours, period=14):
    gain = float(0)
    loss = float(0)
    for i in range(0, period-1):
        diff = (cours[i + 1] - cours[i])
        if (diff > 0):
            gain = gain + diff
        else:
            loss = loss + abs(diff)

    AG = gain / period  # On utilise la SMA pour moyenner"
    AL = loss / period
    rsi = []
    for i in range(period-1, len(cours) - 1):
        if (AL == 0):
            RS = 999
        else:
            RS = AG / AL  # considérer cas AG (ou AL) = 0
        rsi.append(100 - (100 / (1 + RS)))
        diff = cours[i + 1] - cours[i]
        if (diff > 0):
            AG = (AG * (period - 1) + diff) / period
            AL = (AL * 13) / period
        else:
            AL = (AL * (period - 1) + abs(diff)) / period
            AG = (AG * 13) / period
    return rsi
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            