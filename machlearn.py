import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data={
'Hudud':['Samarqand','Urgut','Qorasuv','Qorasuv','Qorasuv','Qorasuv','Qorasuv','Urgut','Ishtixon','Qorasuv'],
'Xona':[3,2,2,3,3,1,1,2,2,1],
'Maydon':[57,52,42,65,70,28,30,32,51,30],
'Qavat':[4,4,4,1,3,1,2,5,3,1],
'Uy_Qavat':[4,5,4,4,5,4,4,5,4,4],
'Narx':[52000,56000,37000,49500,55000,25500,21200,20000,26200,22200]
};

df=pd.DataFrame(data)
print(df)

Uy=df[df.Hudud=='Qorasuv']
qora=Uy.head()

print(qora)

X=Uy['Maydon'].to_numpy()

Y=Uy['Narx'].to_numpy()
   
# plt.figure(figsize=(15,10))
# sns.scatterplot(data=Uy, x='Maydon', y='Narx')
# plt.show()

plt.figure(figsize=(10,6))
sns.regplot(data=Uy, x='Maydon', y='Narx', line_kws={"color":"yellow"})
plt.show()