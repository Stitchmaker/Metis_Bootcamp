import pandas as pd
import numpy as np

from sklearn.linear_model    import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model    import RidgeCV
from sklearn.pipeline        import make_pipeline
from sklearn.preprocessing   import PolynomialFeatures
from sklearn.model_selection import KFold
from sklearn.preprocessing   import StandardScaler
from sklearn.metrics         import mean_squared_error
from sklearn.linear_model    import Lasso
from sklearn                 import linear_model

import seaborn as sns
import matplotlib.pyplot as plt

from math import sqrt

import pickle

'''
Function:  plot_curves()
Arguements: df - dataframe with data
            lift_lines - lines of constant lift from prediction, default=None
            title - title to put on the plot, default=''
Returns:  

'''

def plot_curves(df,lift_lines=None,title=''):
    plt.figure(figsize=(12,7))

    col_list = { 10:'blue',
                 20:'red',
                 30:'green',
                 40:'gold',
                 50:'purple'
               }
    # set the colors for the lift points
    def pltcolor(lift,col_list):
        cols=[]
        for l in lift:
            if l <= 15:
                cols.append(col_list[10])
            elif (l > 15) and (l <= 25):
                cols.append(col_list[20])
            elif (l > 25) and (l <= 35):
                cols.append(col_list[30])
            elif (l > 35) and (l <= 45):
                cols.append(col_list[40])
            elif (l > 45):
                cols.append(col_list[50])
        return cols

    # if there is predicted lift lines, plot these
    if lift_lines:
        for key in lift_lines:
            x_line = lift_lines[key][0]
            y_line = lift_lines[key][1]
            plt.plot(x_line,y_line,c='white',linewidth=3.0)            
            plt.plot(x_line,y_line,c=col_list[key],linewidth=1.0,label=f'{key} degrees F Lift')
            
    # call function to set the bands of colors
    bands = pltcolor(list(df['DTLift']),col_list)

    plt.scatter(x=df['Load'],y=df['kW/Ton'],s=2,c=bands,label='')

    if (title == 'B1') or (title == 'B2') or (title == 'B3'):
        york = pd.read_csv('data/Chiller_Characteristics/YorkCurves.csv')
        plt.plot(york['Load']/100.,york['YKKJKLH9-CWF'],c='black',marker='o',linewidth=2.0) 

    elif (title == 'S1') or (title == 'S2') or (title == 'S3') or (title == 'S4'):
        york = pd.read_csv('data/Chiller_Characteristics/YorkCurves.csv')
        plt.plot(york['Load']/100.,york['YKPFP4K2-FBG'],c='black',marker='o',linewidth=2.0)            

    plt.legend(fontsize=15)
    plt.xlabel('Load',size=20)
    plt.ylabel('kW/Ton',size=20)
    plt.title(title, size=20)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.grid(True)
    plt.ylim(0,1)
    plt.xlim(0,1)
    plt.show()




'''
Function:  getXy()
Arguements: file_name - file name from which to read the chiller data
            features - list of which features to add, choose from empty, 'HigherOrder' or 'AddOther'
            RatedTon - rated tonage for chiller
Returns:  X - DataFrame of input features
          y - Target, kW/Ton
          df - dataframe read from file_name

Read the file, clean up the data, create DataFrame with features

'''
def get_Xy(file_name,RatedTon,features=[]):
    def clean_NaN(df):
        # Look for rows with NaN and drop
        #print(df[df['Load'].isnull() == True])
        #print(df[df['DTLift'].isnull() == True])
        #print(df[df['kW/Ton'].isnull() == True])
      
        # drop rows with NaN
        #df.dropna(subset=['Load','DTLift','kW/Ton'],inplace=True)
        df.dropna(subset=['Load','DTLift','kW/Ton','CompSH','EvapApproach','CondApproach','IGV','REFLVL'],inplace=True)
        
        return df

    df = pd.read_csv(file_name)

    num_rows = df.shape[0]
    df = clean_NaN(df)
    print('DataFrame rows with NaN removed: ',num_rows - df.shape[0])


    y = df['kW/Ton'].copy()
    X = df[['Load','DTLift']].copy()

    if 'HigherOrder' in features:
        X['Load^2'] = df['Load']**2
#        X['DTLift^2'] = df['DTLift']**2
        X['Load*DTLift'] = df['Load']*df['DTLift']
#        X['Load*DTLift^2'] = df['Load']*df['DTLift']**2
        X['Load^2*DTLift'] = (df['Load']**2)*df['DTLift']
    if 'AddOther' in features:    
        X['CompSH_mean']   = df['CompSH'].mean()
        X['CompSH_std']    = df['CompSH'].std()
        X['CompSH_median'] = df['CompSH'].median()

        X['EvapApproach_mean']   = df['EvapApproach'].mean()
        X['EvapApproach_std']    = df['EvapApproach'].std()
        X['EvapApproach_median'] = df['EvapApproach'].median()

        X['CondApproach_mean']   = df['CondApproach'].mean()
        X['CondApproach_std']    = df['CondApproach'].std()
        X['CondApproach_median'] = df['CondApproach'].median()

        #X['IGV'] = df['IGV']

        X['REFLVL_mean']   = df['REFLVL'].mean()
        X['REFLVL_std']    = df['REFLVL'].std()
        X['REFLVL_median'] = df['REFLVL'].median()

        X['RatedTon'] = RatedTon

    return X, y, df

