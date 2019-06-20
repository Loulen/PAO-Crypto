import pandas as pd
from sklearn import svm
import os
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def apprentissage():
        X= []
        Y=[]
        for i in range(len(os.listdir('./2018'))):
                # for i in range(200):
                semaine = pd.read_csv('./2018/'+str(i+1))
                (x, y) = DataOneFile(semaine[['Prix', 'ema', 'rsi']])
                X.append(x)
                Y.append(y)
        # for i in range(len(os.listdir('./2017'))):
        #         # for i in range(200):
        #         semaine = pd.read_csv('./2017/'+str(i+1))
        #         (x, y) = DataOneFile(semaine[['Prix', 'ema', 'rsi']])
        #         X.append(x)
        #         Y.append(y)

        for i in range(len(os.listdir('./2019'))):
                # for i in range(200):
                semaine = pd.read_csv('./2019/'+str(i+1))
                (x, y) = DataOneFile(semaine[['Prix', 'ema', 'rsi']])
                X.append(x)
                Y.append(y)

        return(X,Y, semaine)
        #On divise les données en 2 parties, la partie "train" qui
        # va nous servir à train le classifier, et la partie "test"
        # qui nous permettra de tester notre classifier. On prend 
        # arbitrairement 10% de nos données pour tester.

               


def DataOneFile(semaine : pd.DataFrame) -> (list,list):
        """"x : une donnée input(contenant cours, ema, rsi ...) associée à un 
        y qui est un outcome (ce qu'on veut prédire : seulement le prix).
        L'outcome correspond à 1% de la donnée """
        (semaine,y)=get_outcome(semaine)
        x = []
        for oneHourInfo in semaine.values :
                x.extend(oneHourInfo)
        return (x,y)        
                        
                

        
        # récuperer 1% des données d outcome de la dataframe
        # reshape la matrice en un vecteur
        # chopper l outcome correspondant au dernier pourcent de vecteur
        # stocker le vecteur dans une matrice X, l outcome dans Y
        # BALANCE LE ML MON POTE


def get_outcome(df):
        outcome = []
        # nb_valeurs =int((len(df.index)//100)+1)
        nb_valeurs = 1
        cours = df['Prix']
        df = df.iloc[:len(df.index)-nb_valeurs]
        outcome = list(cours[-nb_valeurs:].values)
        return (df, outcome)


def get_outcome_cat(df):
        """retourne l'outcome sous forme {1;0;-1} avec :
        1 = croissance du cours
        0 = pas de modification significative
        -1 = décroissance du cours"""
        outcome = []
        nb_valeurs = 1
        cours = df['Prix']
        df = df.iloc[:len(df.index)-nb_valeurs]
        outcome = list(cours[-nb_valeurs:].values)

        # on détermine un seuil, qui correspond au pourcentage d'évolution
        # du cours.
        seuil=0.5
        if outcome[0]>df[-1:]:
                if (outcome[0]-df[-1:])/outcome[0] > seuil:
                        outcome = -1
                else:
                        outcome = 0

        if outcome[0]<df[-1:]:
                if (df[-1:]-outcome[0])/df[-1:]>seuil:
                        outcome=-1
                else :
                        outcome=0

        return (df, outcome)

(X,Y,semaine)=apprentissage()
test_len = len(X)//100+1
X_train = X[:-test_len]
Y_train = Y[:-test_len]
X_test = X[len(X)-test_len:]
Y_test = Y[len(Y)-test_len:]

# # Linear regression
# clfreg = LinearRegression(n_jobs=-1)
# clfreg.fit(X_train, Y_train)


# # Quadratic Regression 2
clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
clfpoly2.fit(X_train, Y_train)

# Quadratic Regression 3
# clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
# clfpoly3.fit(X_train, Y_train)

# confidencereg = clfreg.score(X_test, Y_test)
confidencepoly2 = clfpoly2.score(X_test, Y_test)
print(confidencepoly2)
# confidencepoly3 = clfpoly3.score(X_test, Y_test)
