import pandas as pd


def apprentissage():
        for i in len(os.listdir('./2018')) :
                semaine = pd.read_csv('./2018/'+str(i))
                (semaine,y)=get_outcome(semaine)
                

        
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
        outcome = cours[-nb_valeurs:]
        return (df,outcome) 
