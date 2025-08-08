import pandas as pd

chipo = pd.read_csv('chipotle.csv')
chipo['item_price'] = chipo['item_price'].str.replace('$','').astype(float) # this is so that it removes the dollar sign from the front of item_price and converts it to float
print('\n Shape->',chipo.shape,'\n')

# Q4) What was the quantity of most expensive item ordered
most_expensive_index = chipo['item_price'].idxmax()
most_expensive_row = chipo.loc[most_expensive_index]
print(most_expensive_row[['quantity','item_name','item_price']],'\n')

'''
O/P:
quantity                                15
item_name     Chips and Fresh Tomato Salsa
item_price                           44.25
Name: 3598, dtype: object 

'''