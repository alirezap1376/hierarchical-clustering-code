import pandas as pd
import numpy as np

dataframe1=pd.DataFrame([[0,2,181,221,625,821],[2,0,145,181,557,745],[181,145,0,2,136,250],
                         [221,181,2,0,106,212],[625,557,136,106,0,26],[821,745,250,212,26,0]] 
             , columns=["A","B","C","D","E","F"] , index=["A","B","C","D","E","F"])


namec= dataframe1.index


columnname=list( namec )
indexname=list( namec )


columnname=[str(x) for x in columnname]
indexname=[str(x) for x in indexname]

dataframe1.set_axis(  indexname , axis=0 ,inplace=True)
dataframe1.set_axis(  columnname , axis=1 ,inplace=True)


for i in range(dataframe1.shape[0]):
    for j in range(dataframe1.shape[1]):
        if i==j:
            dataframe1.iloc[i,j]=1000000000000
            
            
x=dataframe1.shape[0]

dicti={}
for i in range(2,x+2):
    dicti[i]={}

len(dicti)
dicti[len(dicti) + 1] = list(dataframe1.index)



while x> 1:
    dataframe1.min().min()   
    dataframe2 = dataframe1[dataframe1 == dataframe1.min().min()   ]
    l=[]
    l = list(dataframe2[dataframe2.notnull()].stack().index)
    dataframe2 = dataframe1.copy()


    dataframe2.drop( l[0][0] , axis=0,inplace=True )
    dataframe2.drop( l[0][1] , axis=0,inplace=True )

    dataframe2.drop( l[0][0] , axis=1,inplace=True )
    dataframe2.drop( l[0][1] , axis=1,inplace=True )



    newname1= l[0][0] +  l[0][1]
    

    dataframe2.loc[newname1,:]=None
    dataframe2.loc[:,newname1]=None
    

    dataframe2.iloc[: , -1]

    for i in dataframe2.index[:-1]:    
        dataframe2.loc[i,newname1]=  None
        dataframe2.loc[newname1,i]=  None
        
        
        
    for i in dataframe2.index[:-1]:    

            dataframe2.loc[i,newname1]=  (  dataframe1.loc[i, l[0][0]] +   dataframe1.loc[i, l[0][1]]    )/2
            dataframe2.loc[newname1,i]=  (  dataframe1.loc[i, l[0][0]] +   dataframe1.loc[i, l[0][1]]    )/2
     
  
        
        
#    for i in dataframe2.index[:-1]:    
#        if max(  dataframe1.loc[i, l[0][0]] ,  dataframe1.loc[i, l[0][1]]    )  < 4:
#            dataframe2.loc[i,newname1]=  (  dataframe1.loc[i, l[0][0]] +   dataframe1.loc[i, l[0][1]]    )/2
#           dataframe2.loc[newname1,i]=  (  dataframe1.loc[i, l[0][0]] +   dataframe1.loc[i, l[0][1]]    )/2
#        else:
#            dataframe2.loc[i,newname1]= ((  dataframe1.loc[i, l[0][0]] +   dataframe1.loc[i, l[0][1]]    )/2 )*5
#            dataframe2.loc[newname1,i]= ((  dataframe1.loc[i, l[0][0]] +   dataframe1.loc[i, l[0][1]]    )/2 )*5
    

    
    for i in range(dataframe2.shape[0]):
        for j in range(dataframe2.shape[1]):
            if i==j:
                dataframe2.iloc[i,j]=1000000000000
            
    
    dicti[x]=([newname1,dataframe2.min().min()])
    
    
    dataframe1=dataframe2.copy()  
    

    x=x-1
                
    
    
    
    
     
    
h=list(dicti.values())    
h    
len(h)    


#range(start, stop, step)
    
for i in range(len(h)-1 , -1 , -1 )  :
    #print(i)
    #print(i,h[i])
    #print(i,h[i][1])
    print(i,h[i][0])
     
    
candid=[]    
for i in range(len(h)-1 , -1 , -1 )  :
    #print(i)
    #print(i,h[i])
    #print(i,h[i][1])
    #print(i,h[i][0])  
    #print(h[i][0])
    candid.append((h[i][0]))
    
    
lastdict={}    
for i in range(1,len(candid)+2):
    lastdict[i]={}
        
 
    
 
m=list( dicti.values() )[len(list( dicti.values() ))-1]  

for i in range( 1 , len(candid)+2 ):
    
    #given = candid[i-1]
    #print(given)
    #lastdict[i] = m
    
    if i ==1:
        lastdict[i] = m
    else:
        #print(i)
        given = candid[i-2]
        lastdict[i] =[k for k in lastdict[i-1] if k not in given] + [given]


newD = {}

for i in list(lastdict.values()):
    print(i)
    newD[len(i)] = i






dataframe1=pd.DataFrame([[0,5,2,1,3],[5,0,4,6,7],[2,4,0,8,9],[1,6,8,0,3],[3,7,9,3,0]] 
             , columns=["A","B","C","D","E"] , index=["A","B","C","D","E"])




firstdataframe = dataframe1.copy()

firstdataframe['Label']=None
newD[3]


k = eval(  input('give me your best number of clusters: ') )

    
for i in range(0,len(newD[k]))  :
    for j in firstdataframe.index :
        if j in newD[k][i]:
            firstdataframe.loc[j,'Label'] =  newD[k].index(newD[k][i])


