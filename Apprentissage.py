import pandas as pd
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def apprentissage():
        X= []
        Y=[]
        # for i in len(os.listdir('./2018')) :
        for i in range(2000):
                # semaine = pd.read_csv('./2018/'+str(i))
                semaine = pd.read_csv('./2018/'+str(i+1))
                (x,y) = DataOneFile(semaine)
                X.append(x)
                Y.append(y)

        return(X,Y)
        #On divise les données en 2 parties, la partie "train" qui
        # va nous servir à train le classifier, et la partie "test"
        # qui nous permettra de tester notre classifier. On prend 
        # arbitrairement 10% de nos données pour tester.
        # test_len=len(X)//100+1
        # X_train = X[:-test_len]
        # Y_train = Y[:-test_len]
        # X_test = X[len(X)-test_len:]
        # Y_test = Y[len(Y)-test_len:]


        # clf = svm.SVC(gamma='auto')
        # clf.fit(X_train,Y_train)
        # print(clf.score(X_test,Y_test))
               


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

(X,Y)=apprentissage()
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
# confidencepoly3 = clfpoly3.score(X_test, Y_test)
