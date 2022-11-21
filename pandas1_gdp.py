import pandas as pd

df = pd.read_csv("GDPlist.csv",encoding= "ISO-8859-1")

#print(df.info())

df.rename(columns={'Country':'Nuoc','Continent':'Chau luc','GDP (millions of US$)':'GDP(trieu $)'},inplace= True)
print(df)
df.insert(1,'Thanh Pho',pd.Series(df['Nuoc'],index = df.index)) 
print(df)
df['Thanh Pho'] = df['Thanh Pho'].apply(lambda x: str(x).strip())
print(df)
df['Thanh Pho'].replace('Vietnam','Hanoi',inplace= True)
print(df)

check = df.loc[df['Chau luc'] == 'Asia'].index.to_list()
print(check)
data = df.drop(index = check ,axis= 0)
print(data)

check = df.loc[df['GDP(trieu $)'] < 300000].index.to_list()

data = df.drop(index= check, axis= 10)
print(data)