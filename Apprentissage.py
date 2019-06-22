import pandas as pd
from sklearn import svm
import os
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline



def apprentissage(type_learning,nb_annees) :
        """ renvoie un classifier entrainé avec X et Y, ou X est l'input et Y l'output exact désiré associé.
            Seulement 90% des données du couples sont utilisées, les 10% restant réservés pour le test.'type_learning' 
            correspond au type de classifier désiré et 'nb_annees' à la taille du couple X,Y en années.    """
        if type_learning == 'Lreg' :
                (X,Y,semaine)=apprentissage_data(nb_annees,'exact')
                test_len = len(X)//100+1
                X_train = X[:-test_len]
                Y_train = Y[:-test_len]        
                clf = LinearRegression(n_jobs=-1)
                clf.fit(X_train, Y_train)
        if type_learning == "Qreg2" :
                (X,Y,semaine)=apprentissage_data(nb_annees,'exact')
                test_len = len(X)//100+1
                X_train = X[:-test_len]
                Y_train = Y[:-test_len] 
                clf = make_pipeline(PolynomialFeatures(2), Ridge())
                clf.fit(X_train, Y_train)
        if type_learning == "Qreg3" :
                (X,Y,semaine)=apprentissage_data(nb_annees,'exact')
                test_len = len(X)//100+1
                X_train = X[:-test_len]
                Y_train = Y[:-test_len]
                clf = make_pipeline(PolynomialFeatures(3), Ridge())
                clf.fit(X_train, Y_train)

def score(X,Y,clf):
        """Test le clf donné en entrée, 10% des dernières données sont utilisées pour tester"""
        test_len = len(X)//100+1
        X_test = X[len(X)-test_len:]
        Y_test = Y[len(Y)-test_len:]
        confidence = clf.score(X_test, Y_test)
        print(confidence)
        return confidence
        

def apprentissage_data(nb_annees,type_outcome):
        """Construit un couple de vecteurs (X,Y) ou l'input X(i) correspond à un output Y(i). Le nombre d'éléments
        est fonction du nombre d'années et donc du nombre de données utilisées. 'type_outcome' peut être tendanciel ou 
        exact."""
        X= []
        Y=[]
        for i in range(len(os.listdir('./2018'))):
                semaine = pd.read_csv('./2018/'+str(i+1))
                semaine = semaine.sort_values(['day','hour'])
                (x,y) = DataOneFile(semaine[['Prix', 'ema','rsi']],type_outcome)
                X.append(x)
                Y.append(y)
        if nb_annees==2 or nb_annees==3 : 
                for i in range(len(os.listdir('./2017'))):
                         semaine = pd.read_csv('./2017/'+str(i+1))
                         semaine = semaine.sort_values(['day','hour'])

                         (x, y) = DataOneFile(semaine[['Prix','ema','rsi']],type_outcome)
                         X.append(x)
                         Y.append(y)
        if nb_annees==3 :
                for i in range(len(os.listdir('./2019'))):
                         semaine = pd.read_csv('./2019/'+str(i+1))
                         semaine = semaine.sort_values(['day','hour'])
                         (x, y) = DataOneFile(semaine[['Prix','ema','rsi']],type_outcome)
                         X.append(x)
                         Y.append(y)

        return(X,Y, semaine)        


def DataOneFile(semaine : pd.DataFrame,type_outcome) -> (list,list):
        """"x : une donnée input(contenant cours, ema, rsi ...) associée à un 
        y qui est un outcome (ce qu'on veut prédire : seulement le prix).
        L'outcome correspond à 1% de la donnée, il est donnée sous la forme d'une valeur de cours précise
        ou d'un chifre (-1,0,1), selon le type_outcome d'outcome demandé """
        if type_outcome == 'tendanciel' :
                (semaine,y)=get_outcome_cat(semaine)
        if type_outcome == 'exact':
                (semaine,y)=get_outcome_reg(semaine)

        x = []
        for oneHourInfo in semaine.values :
                x.extend(oneHourInfo)
        return (x,y)        


def get_outcome_reg(df):
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
        seuil=0.2/100
        if (outcome[0]>df[-1:]['Prix'].values):
                print('x : %f, y : %f, dif = %f' % (
                    outcome[0], df[-1:]['Prix'].values, (outcome[0]-df[-1:]['Prix'].values)/outcome[0]))
                if (outcome[0]-df[-1:]['Prix'].values)/outcome[0] > seuil:
                        print(-1)
                        outcome = 1
                else:
                        outcome = 0
        else :
                if (outcome[0]<df[-1:]['Prix'].values):
                        if (df[-1:]['Prix'].values-outcome[0])/df[-1:]['Prix'].values>seuil:
                                print(1)

                                outcome=-1
                        else :
                                outcome=0
                else :
                        outcome=0

        return (df, outcome)
