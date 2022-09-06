#importing the pandas  and matplot library
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics as st
#importing the csv file from the desktop


# def miss_Value(lis):
#     t=0
#     for i in range(len(lis)):
#         if (type(lis[i])=='float'):
#             t=t+1
#     return t
    

data= pd.read_csv("D:\Vaibhav Hacker\Desktop\IC-272 DS3\landslide_data3_miss.csv")
data_org=pd.read_csv("D:\Vaibhav Hacker\Desktop\IC-272 DS3\landslide_data3_original.csv")
# dates= list(data['dates'])
# stationid= list(data['stationid'])
# temperature= list(data['temperature'])
# humidity= list(data['humidity'])
# pressure= list(data['pressure'])
# rain= list(data['rain'])
# lightavgwo0= list(data['lightavgw/o0'])
# lightmax= list(data['lightmax'])
# moisture=list(data['moisture'])
# print(type(temperature[3]))


#lis_X=['dates','stationid','temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']
# lis_Y=[miss_Value(stationid),miss_Value(temperature),miss_Value(humidity),miss_Value(pressure),miss_Value(rain),miss_Value(lightavgwo0),miss_Value(lightmax),miss_Value(moisture)]
# fig= plt.figure(figsize=(10,5))      
# plt.bar(lis_X,lis_Y, color='maroon',width='0.4')

# ques1
data.isnull().sum().plot(kind='bar')
plt.xlabel("Attributes Name ---->")
plt.ylabel("No.of missing values ---->")
plt.title("No. of missing values in a particular attribute.")
plt.show()
print(data['temperature'].isnull().sum())
#ques2(a)
drop=data['stationid'].dropna()
new=pd.isnull(data["stationid"])

print("Number of tuples deleted :",len(data[new]))

#ques2(b)

df=data.dropna(axis=0,thresh=7)
print("Number of tuples deleted :",len(data)-len(df))


#ques3
missing_values=df.isnull().sum()
print(missing_values)

print("Total number of missing values in the file:",missing_values.sum())

#ques4(a)(i)
mean=data.mean()
df1=data.fillna(mean)
print(df1.mean())
print(df1.median())
print(df1.mode())
print(df1.std())

print(data_org.mean())
print(data_org.median())
print(data_org.mode())
print(data_org.std())

#ques4(a)(ii)
def RMSE(df,df_org,N):
    df1=df_org-df
    df1=df1**2
    return (((df1.sum())/N)**0.5)
    

lis_RMSE=[]
lis_RMSE.append(RMSE(df1['temperature'],data_org['temperature'],data['temperature'].isnull().sum()))
lis_RMSE.append(RMSE(df1['humidity'],data_org['humidity'],data['humidity'].isnull().sum()))
lis_RMSE.append(RMSE(df1['pressure'],data_org['pressure'],data['pressure'].isnull().sum()))
lis_RMSE.append(RMSE(df1['rain'],data_org['rain'],data['rain'].isnull().sum()))
lis_RMSE.append(RMSE(df1['lightavgw/o0'],data_org['lightavgw/o0'],data['lightavgw/o0'].isnull().sum()))
lis_RMSE.append(RMSE(df1['lightmax'],data_org['lightmax'],data['lightmax'].isnull().sum()))
lis_RMSE.append(RMSE(df1['moisture'],data_org['moisture'],data['moisture'].isnull().sum()))
print(lis_RMSE)


lis_X=['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']


fig= plt.figure(figsize=(10,5))      
plt.scatter(lis_X,lis_RMSE, color='maroon')
plt.xlabel("Attributes Name ---->")
plt.ylabel("RMSE values ---->")
plt.title("No. of missing values in a particular attribute.")
plt.grid()
plt.show()

#ques4(b)(i)
df2=data.interpolate(method='linear')
print(df2.mean())
print(df2.median())
print(df2.mode())
print(df2.std())

#ques4(b)(ii)
lis_RMSE2=[]
lis_RMSE2.append(RMSE(df2['temperature'],data_org['temperature'],data['temperature'].isnull().sum()))
lis_RMSE2.append(RMSE(df2['humidity'],data_org['humidity'],data['humidity'].isnull().sum()))
lis_RMSE2.append(RMSE(df2['pressure'],data_org['pressure'],data['pressure'].isnull().sum()))
lis_RMSE2.append(RMSE(df2['rain'],data_org['rain'],data['rain'].isnull().sum()))
lis_RMSE2.append(RMSE(df2['lightavgw/o0'],data_org['lightavgw/o0'],data['lightavgw/o0'].isnull().sum()))
lis_RMSE2.append(RMSE(df2['lightmax'],data_org['lightmax'],data['lightmax'].isnull().sum()))
lis_RMSE2.append(RMSE(df2['moisture'],data_org['moisture'],data['moisture'].isnull().sum()))
print(lis_RMSE2)


lis_X=['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']


fig= plt.figure(figsize=(10,5))      
plt.scatter(lis_X,lis_RMSE2, color='maroon')
plt.xlabel("Attributes Name ---->")
plt.ylabel("RMSE values ---->")
plt.title("No. of missing values in a particular attribute.")
plt.grid()
plt.show()

#ques5
df_quantile=df2.quantile([0.25,0.75])
df_iqr=df_quantile.iloc[1]-df_quantile.iloc[0]

df_lb=df_quantile.iloc[0]-(1.5*df_iqr)
df_ub=df_quantile.iloc[1]+(1.5*df_iqr)

outlier_lb=df2['temperature']<df_lb['temperature'] 
outlier_ub=df2['temperature']>df_ub['temperature']
df_outlier1=df2['temperature'][outlier_lb|outlier_ub]
print(df_outlier1)

outlier_lb1=df2['rain']<df_lb['rain'] 
outlier_ub1=df2['rain']>df_ub['rain']
df_outlier2=df2['rain'][outlier_lb1|outlier_ub1]
print(df_outlier2)

plt.boxplot(df2['temperature'])
plt.xlabel('Temperature',fontsize=24)
plt.show()

plt.boxplot(df2['rain'])
plt.xlabel('Rain',fontsize=24)
plt.show()

#ques5(b)
median=df2['temperature'].median()
df2.loc[df2['temperature']<df_lb["temperature"],'temperature'] =np.nan
df2.fillna(median,inplace=True)

median_r=df2['rain'].median()
df2.loc[df2['rain']>df_ub["rain"],'rain'] =np.nan
df2.fillna(median_r,inplace=True)

plt.boxplot(df2['temperature'])
plt.xlabel('Temperature',fontsize=24)
plt.show()

plt.boxplot(df2['rain'])
plt.xlabel('Rain',fontsize=24)
plt.show()


