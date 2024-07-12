#to read CSV use the pandas module
import pandas as pd
#use the os (operating syst.) module to switch working directories
import os
os.chdir('..')
#print(os.getcwd()) #/Users/loannguyen/Documents/Python
#os.chdir() = changes the current working directory to a specific path.
os.chdir('/Users/loannguyen/Documents/Python/netflix-report/CONTENT_INTERACTION')
#print(os.getcwd())
df=pd.read_csv('ViewingActivity.csv')
print(df)
df=df.drop(df[df['Supplemental Video Type']=='HOOK'].index)
df=df.drop(df[df['Supplemental Video Type']=='TRAILER'].index)
df=df.drop(df[df['Supplemental Video Type']=='TEASER_TRAILER'].index)
print(df)
new_df=df[['Duration', 'Title']].copy()
print(new_df.head(3))
#data types
print(new_df.dtypes)
#convert 'Duration' to timedelta, which is a measure of time duration
new_df['Duration']=pd.to_timedelta(new_df['Duration'])
print(new_df['Duration'].head(3))
print(new_df.dtypes)
new_df['Brief Title']=new_df['Title'].str.split(':', n=1, expand=True)[0]
new_df=new_df.groupby('Brief Title')['Duration'].sum()
data=pd.DataFrame(new_df)
#data.to_csv('updated_ViewingActivity.csv')
data=data.reset_index()
print("The number of columns is",len(data.columns),", and they are",
      list(data.columns))
print(new_df.head(5))
#Which TV show do I watch the longest?
print(data.iloc[data['Duration'].idxmax()])
#Which show do I watch the shortest?
print(data.iloc[data['Duration'].idxmin()])
for i in data['Brief Title']:
    print(i)
#What is the duration of my favorite show, "Dead Boy Detectives"?
print(data[data['Brief Title'].str.contains('Dead Boy Detectives')])
