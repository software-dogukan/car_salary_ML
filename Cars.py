import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
ohe=OneHotEncoder()
le=LabelEncoder()
data=pd.read_csv("CarPrice_Assignment.csv")

fueltype= data.iloc[:,3].values
fueltype=le.fit_transform(fueltype)
fueltype=pd.DataFrame(fueltype)

aspira=data.iloc[:,4].values
aspira=le.fit_transform(aspira)
aspira=pd.DataFrame(aspira)

doornumber=data.iloc[:,5].values
doornumber=le.fit_transform(doornumber)
doornumber=pd.DataFrame(doornumber)

carbody=data.iloc[:,6].values
carbody=ohe.fit_transform(carbody.reshape(-1, 1)).toarray()
carbody=pd.DataFrame(carbody)

drivew=data.iloc[:,7].values
drivew=ohe.fit_transform(drivew.reshape(-1, 1)).toarray()
drivew=pd.DataFrame(drivew)

enginloc=data.iloc[:,5].values
enginloc=le.fit_transform(enginloc)
enginloc=pd.DataFrame(enginloc)

engintype=data.iloc[:,14].values
engintype=ohe.fit_transform(engintype.reshape(-1, 1)).toarray()
engintype=pd.DataFrame(engintype)


cylindernumber=data.iloc[:,15].values
cylindernumber=ohe.fit_transform(cylindernumber.reshape(-1, 1)).toarray()
cylindernumber=pd.DataFrame(cylindernumber)

fuelsystem=data.iloc[:,17].values
fuelsystem=ohe.fit_transform(fuelsystem.reshape(-1, 1)).toarray()
fuelsystem=pd.DataFrame(fuelsystem)

y=data.iloc[:,-1].values
data = data.drop(["fueltype","aspiration","doornumber","carbody","drivewheel","enginelocation","enginetype","cylindernumber","fuelsystem","price"],axis=1)
data=pd.concat([data,fueltype],axis=1)
data.rename(columns={0:"fueltype"},inplace=True)
data=pd.concat([data,aspira],axis=1)
data.rename(columns={0:"aspira"},inplace=True)
data=pd.concat([data,doornumber],axis=1)
data.rename(columns={0:"doornumber"},inplace=True)
data=pd.concat([data,carbody],axis=1)
data.rename(columns={0:"carbody1",1:"carbody2",2:"carbody3",3:"carbody4",4:"carbody5"},inplace=True)
data=pd.concat([data,drivew],axis=1)
data.rename(columns={0:"drivew1",1:"drivew2",2:"drivew3"},inplace=True)
data=pd.concat([data,enginloc],axis=1)
data.rename(columns={0:"enginloc"},inplace=True)
data=pd.concat([data,engintype],axis=1)
data.rename(columns={0:"engintype1",1:"engintype2",2:"engintype3",3:"engintype4",4:"engintype5",5:"engintype6",6:"engintype7"},inplace=True)
data=pd.concat([data,cylindernumber],axis=1)
data.rename(columns={0:"cylindernumber1",1:"cylindernumber2",2:"cylindernumber3",3:"cylindernumber4",4:"cylindernumber5",5:"cylindernumber6",6:"cylindernumber7"},inplace=True)
data=pd.concat([data,fuelsystem],axis=1)
data.rename(columns={0:"fuelsystem1",1:"fuelsystem2",2:"fuelsystem3",3:"fuelsystem4",4:"fuelsystem5",5:"fuelsystem6",6:"fuelsystem7",7:"fuelsystem8"},inplace=True)


print(data.columns)
