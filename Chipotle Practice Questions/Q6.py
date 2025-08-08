import pandas as pd

chipo = pd.read_csv('chipotle.csv')
chipo['item_price'] = chipo['item_price'].str.replace('$','').astype(float) # this is so that it removes the dollar sign from the front of item_price and converts it to float
print('\n Shape->',chipo.shape,'\n')

# Q6 How many times did someone order more than one canned soda
chipo['quantity'] = chipo['quantity'].astype(int)
canned_soda = chipo[(chipo['item_name'] == 'Canned Soda') & (chipo['quantity'] > 1)]
total_times = canned_soda.shape[0]
print('Total times when someone ordered more than 1 Canned Soda:',total_times,'\n')
'''
O/P:
Total times when someone ordered more than 1 Canned Soda: 20

'''