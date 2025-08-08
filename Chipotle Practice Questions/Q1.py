import pandas as pd

chipo = pd.read_csv('chipotle.csv')
chipo['item_price'] = chipo['item_price'].str.replace('$','').astype(float) # this is so that it removes the dollar sign from the front of item_price and converts it to float
print('\n Shape->',chipo.shape,'\n')

# Q1) How many products cost more than 10.00$
more_than_10 = chipo[chipo['item_price'] > 10].shape[0]
print('\nNo of products costing more than 10.00$ : ',more_than_10,'\n')


'''
O/P:
No of products costing more than 10.00$ :  1130

'''