import pandas as pd

chipo = pd.read_csv('chipotle.csv')
chipo['item_price'] = chipo['item_price'].str.replace('$','').astype(float) # this is so that it removes the dollar sign from the front of item_price and converts it to float
print('\n Shape->',chipo.shape,'\n')

# Q2) What is price of each item. (print only column item_name & item_price)
name = chipo['item_price']
price = chipo['item_name']
name_price = pd.concat([name,price],axis=1)
print(name_price,'\n')

'''
O/P:
      item_price                              item_name
0           2.39           Chips and Fresh Tomato Salsa
1           3.39                                   Izze
2           3.39                       Nantucket Nectar
3           2.39  Chips and Tomatillo-Green Chili Salsa
4          16.98                           Chicken Bowl
...          ...                                    ...
4617       11.75                          Steak Burrito
4618       11.75                          Steak Burrito
4619       11.25                     Chicken Salad Bowl
4620        8.75                     Chicken Salad Bowl
4621        8.75                     Chicken Salad Bowl

[4622 rows x 2 columns] 

'''