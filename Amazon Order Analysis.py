import os
os.chdir('/Users/loannguyen/Documents/Python/Amazon Orders/Retail.OrderHistory.1')
import pandas as pd
df=pd.read_csv('Retail.OrderHistory.1.csv')
print(df['Product Name'].head())
df=df.drop(df[df['Shipping Address']==
              [redact]].index)
print(df['Product Name'].head())
print(list(df.columns))
col_drop=['Website', 'Order ID', 'Order Date', 'Purchase Order Number',
          'Currency', 'ASIN', 'Product Condition', 'Quantity', 'Order Status',
          'Shipment Status', 'Ship Date', 'Shipping Option', 'Shipping Address',
          'Billing Address', 'Carrier Name & Tracking Number', 'Gift Message',
          'Gift Sender Name', 'Gift Recipient Contact Details', 'Item Serial Number']
df=df.drop(col_drop, axis=1)
print(list(df.columns))
df['Payment Instrument Type']=df['Payment Instrument Type'].str.split('-', n=1, expand=True)[0]
print(df['Payment Instrument Type'].head())
print(df.dtypes)
df['Total Discounts']=pd.to_numeric(df['Total Discounts'], errors='coerce')
df['Shipment Item Subtotal']=pd.to_numeric(df['Shipment Item Subtotal'], errors='coerce')
df['Shipment Item Subtotal Tax']=pd.to_numeric(df['Shipment Item Subtotal Tax'], errors='coerce')
print(df.dtypes)
first_column = df.pop('Product Name')
df.insert(0, 'Product Name', first_column)
print(list(df.columns))
df.reset_index(inplace=True)
print(df.head())
df=df.drop('index', axis=1)
print(list(df.columns))
#df.to_csv('updated_Retail.OrderHistory.csv')

row_num=df[df['Total Owed']==max(df['Total Owed'])]
with pd.option_context('display.max_colwidth', None):
    print(row_num['Product Name'])
row_num1=df[df['Total Owed']==min(df['Total Owed'])]
with pd.option_context('display.max_colwidth', None):
    print(row_num1['Product Name'])

df['Payment Instrument Type']=df['Payment Instrument Type'].str.replace('Gift Certificate/Card and MasterCard', 'Gift Card and MasterCard')
df['Payment Instrument Type']=df['Payment Instrument Type'].str.replace('Gift Certificate/Card and Visa', 'Gift Card and Visa')
print(df.head())
new_df=df.groupby('Payment Instrument Type').size().reset_index(name='counts')
print(new_df)
import matplotlib.pyplot as plt
plt.bar(new_df['Payment Instrument Type'], new_df['counts'])
plt.xticks(fontsize=6)
plt.title('My most popular payment method?')
plt.show()

