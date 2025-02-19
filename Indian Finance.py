import os
print(os.getcwd())
os.chdir('/Users/loannguyen/Documents/Python')
print(os.getcwd())
import pandas as pd
data=pd.read_csv('nce_india_completed  new.csv')
df=data
print(data.head())
print(data.columns)

print(df[df['2015-16 (RE)']==df['2015-16 (RE)'].max()])
print(df[df['2015-16 (RE)']==df['2015-16 (RE)'].min()])

year=['1980','1981','1982','1983','1984','1985',
        '1986','1987','1988','1989','1990',
        '1991','1992','1993','1994','1995',
        '1996','1997','1998','1999','2000',
        '2001','2002','2003','2004','2005',
        '2006','2007','2008','2009','2010',
        '2011','2012','2013','2014','2015']
data.columns.values[1:37]=year
melted=pd.melt(data,id_vars='State',value_vars=year)
print(melted.head())
#melted.to_csv('Melted Indian Finance.csv')
import seaborn as sns
sns.lineplot(melted,x='variable',y='value',hue='State',marker='o')
import matplotlib.pyplot as plt
plt.xlabel('Year',size=15)
plt.ylabel('Tax Revenues',size=15)
plt.title('Indian Finance: 1980 - 2015',size=20)
plt.legend(bbox_to_anchor=(1,.85),loc='upper left',prop={'size':7.5})
plt.xticks(rotation=45,fontsize=10)
plt.show()
