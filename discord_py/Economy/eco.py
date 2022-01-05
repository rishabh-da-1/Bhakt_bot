from os import path
import pandas as pd 
import csv 

path_main = "./Economy/DB/currency.csv"
path_init = "./DB/currency.csv"

col = ['userid','name','coins','CD']

def __increase_BKTC__(user_id):
    user_id = str(user_id)
    reader = pd.read_csv(path_main,names = col)
    
    userid = reader.userid.tolist()
    coins = reader.coins.tolist()
    CD = reader.CD.tolist()
    
    
    index = userid.index(str(user_id))
    if CD[index] == '0':
        coins = int(coins[index])
        coins = coins+1 
        coins = str(coins)
        
        reader.loc[index,'coins'] = coins
        reader.loc[index,'CD'] = '10'
        reader = reader.iloc[1: , :]
        reader.to_csv(path_main,index = False)

  

def cool_down(uid):
    reader = pd.read_csv(path_main, names = col)
    
    user_id = reader.userid.tolist()
    cd = reader.CD.tolist()
    
    if str(uid) in user_id:
        index =  user_id.index(str(uid))
        if int(cd[index]) != 0:
            cd1 = cd[index]
            cd1 = int(cd1)
            cd1 = cd1 -1
            
            reader.loc[index,'CD'] = str(cd1)
            reader = reader.iloc[1: , :]
            reader.to_csv(path_main,index = False)
       

def __register__(user_id,user_name):
    
    file = open(path_main)

    reader = pd.read_csv(file,names=col)
    uid = reader.userid.tolist()
   
    if user_id in uid:
        pass    
    else :
        __append__values__ = pd.DataFrame({'user_id':[user_id],
                                            'user_name':[user_name],
                                            'coins':[str(0)],
                                            'CD':[str(0)]
                                            })
        __append__values__.to_csv(path_main, mode='a', header=False,index=False)
       
    