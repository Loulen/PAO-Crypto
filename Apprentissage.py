import pandas as pd


def apprentissage():
        X= []
        Y=[]
        # for i in len(os.listdir('./2018')) :
        for i in range(10):
                # semaine = pd.read_csv('./2018/'+str(i))
                semaine = pd.read_csv('./2018/'+str(i+1))
                (x,y) = DataOneFile(semaine)
                X.append(x)
                Y.append(y)
        return (X,Y)
               


def DataOneFile(semaine : pd.DataFrame) -> (list,list):
        """"x : une donnée input(contenant cours, ema, rsi ...) associée à un 
        y qui est un outcome (ce qu'on veut prédire : seulement le prix).
        L'outcome correspond à 1% de la donnée """
        (semaine,y)=get_outcome(semaine)
        x = []
        for oneHourInfo in semaine.values :
                x.extend(oneHourInfo[1:])
        return (x,y)        
                        
                

        
        # récuperer 1% des données d outcome de la dataframe
        # reshape la matrice en un vecteur
        # chopper l outcome correspondant au dernier pourcent de vecteur
        # stocker le vecteur dans une matrice X, l outcome dans Y
        # BALANCE LE ML MON POTE


def get_outcome(df):
        outcome=[]
        nb_valeurs =int((len(df.index)//100)+1)
        cours = df['Prix']
        df = df.iloc[:len(df.index)-nb_valeurs]
        outcome = list(cours[-nb_valeurs:].values)
        return (df,outcome) 
