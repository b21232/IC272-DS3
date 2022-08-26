#importing the pandas  and matplot library
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics as st
#importing the csv file from the desktop

data= pd.read_csv("D:\Vaibhav Hacker\Desktop\IC-272 DS3\pima-indians-diabetes.csv")

lis1=[]
pregs= list(data['pregs'])
plas= list(data['plas'])
pres= list(data['pres'])
skin= list(data['skin'])
test= list(data['test'])
BMI= list(data['BMI'])
pedi= list(data['pedi'])
Age= list(data['Age'])


lis1.append(['pregs',np.mean(pregs),st.median(pregs),st.mode(pregs),np.max(pregs),np.min(pregs),np.std(pregs)])
lis1.append(['plas',np.mean(plas),st.median(plas),st.mode(plas),np.max(plas),np.min(plas),np.std(plas)])
lis1.append(['pres',np.mean(pres),st.median(pres),st.mode(pres),np.max(pres),np.min(pres),np.std(pres)])
lis1.append(['skin',np.mean(skin),st.median(skin),st.mode(skin),np.max(skin),np.min(skin),np.std(skin)])
lis1.append(['test',np.mean(test),st.median(test),st.mode(test),np.max(test),np.min(test),np.std(test)])
lis1.append(['BMI',np.mean(BMI),st.median(BMI),st.mode(BMI),np.max(BMI),np.min(BMI),np.std(BMI)])
lis1.append(['pedi',np.mean(pedi),st.median(pedi),st.mode(pedi),np.max(pedi),np.min(pedi),np.std(pedi)])
lis1.append(['Age',np.mean(Age),st.median(Age),st.mode(Age),np.max(Age),np.min(Age),np.std(Age)])

df= pd.DataFrame(lis1, columns=["Attribute","Mean", "Median", "Mode", "Maximum", "Minimum" ," Standard deviation"])
print(df)

#2
xvalues=Age
plt.scatter(xvalues,pregs,color='g',s=10)
plt.xlabel('Age',fontsize=24)
plt.ylabel('pregs',fontsize=24)
plt.show()

plt.scatter(xvalues,plas,color='g',s=10)
plt.xlabel('Age',fontsize=24)
plt.ylabel('plas',fontsize=24)
plt.show()

plt.scatter(xvalues,pres,color='g',s=10)
plt.xlabel('Age',fontsize=24)
plt.ylabel('pres',fontsize=24)
plt.show()

plt.scatter(xvalues,skin,color='g',s=10)
plt.xlabel('Age',fontsize=24)
plt.ylabel('skin',fontsize=24)
plt.show()

plt.scatter(xvalues,test,color='g',s=10)
plt.xlabel('Age',fontsize=24)
plt.ylabel('test',fontsize=24)
plt.show()

plt.scatter(xvalues,BMI,color='g',s=10)
plt.xlabel('Age',fontsize=24)
plt.ylabel('BMI',fontsize=24)
plt.show()

plt.scatter(xvalues,pedi,color='g',s=10)
plt.xlabel('Age',fontsize=24)
plt.ylabel('pedi',fontsize=24)
plt.show()


xvalues=BMI
plt.scatter(xvalues,pregs,color='g',s=10)
plt.xlabel('BMI',fontsize=24)
plt.ylabel('pregs',fontsize=24)
plt.show()

plt.scatter(xvalues,plas,color='g',s=10)
plt.xlabel('BMI',fontsize=24)
plt.ylabel('plas',fontsize=24)
plt.show()

plt.scatter(xvalues,pres,color='g',s=10)
plt.xlabel('BMI',fontsize=24)
plt.ylabel('pres',fontsize=24)
plt.show()

plt.scatter(xvalues,skin,color='g',s=10)
plt.xlabel('BMI',fontsize=24)
plt.ylabel('skin',fontsize=24)
plt.show()

plt.scatter(xvalues,test,color='g',s=10)
plt.xlabel('BMI',fontsize=24)
plt.ylabel('test',fontsize=24)
plt.show()

plt.scatter(xvalues,pedi,color='g',s=10)
plt.xlabel('BMI',fontsize=24)
plt.ylabel('pedi',fontsize=24)
plt.show()

plt.scatter(xvalues,Age,color='g',s=10)
plt.xlabel('BMI',fontsize=24)
plt.ylabel('Age',fontsize=24)
plt.show()


#3
df=data.corr(method='pearson')
print(df.iloc[:,7:8])
print(df.iloc[:,5:6])

#4

data['pregs'].hist();
plt.xlabel('pregs ---->')
plt.ylabel('Frequency ---->')
plt.show()
data['skin'].hist();
plt.xlabel('skin ---->')
plt.ylabel('Frequency ---->')
plt.show()

#5
data['pregs'].groupby(data['class']==0).hist()
plt.xlabel('pregs ---->')
plt.ylabel('Frequency ---->')
plt.show()
data['pregs'].groupby(data['class']==1).hist()
plt.xlabel('pregs ---->')
plt.ylabel('Frequency ---->')
plt.show()

#6
plt.boxplot(pregs)
plt.xlabel('pregs',fontsize=24)
plt.show()

plt.boxplot(plas)
plt.xlabel('plas',fontsize=24)
plt.show()

plt.boxplot(pres)
plt.xlabel('pres',fontsize=24)
plt.show()

plt.boxplot(skin)
plt.xlabel('skin',fontsize=24)
plt.show()

plt.boxplot(test)
plt.xlabel('test',fontsize=24)
plt.show()

plt.boxplot(BMI)
plt.xlabel('BMI',fontsize=24)
plt.show()

plt.boxplot(pedi)
plt.xlabel('pedi',fontsize=24)
plt.show()

plt.boxplot(Age)
plt.xlabel('Age',fontsize=24)
plt.show()