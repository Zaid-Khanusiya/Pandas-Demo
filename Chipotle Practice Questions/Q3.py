import pandas as pd

chipo = pd.read_csv('chipotle.csv')
chipo['item_price'] = chipo['item_price'].str.replace('$','').astype(float) # this is so that it removes the dollar sign from the front of item_price and converts it to float
print('\n Shape->',chipo.shape,'\n')

# Q3) Sort by the name of item
sorted_by_name = chipo.sort_values(by='item_name')
print(sorted_by_name,'\n')

'''
O/P:
       order_id  quantity          item_name                                 choice_description  item_price
3389       1360         2  6 Pack Soft Drink                                        [Diet Coke]       12.98
341         148         1  6 Pack Soft Drink                                        [Diet Coke]        6.49
1849        749         1  6 Pack Soft Drink                                             [Coke]        6.49
1860        754         1  6 Pack Soft Drink                                        [Diet Coke]        6.49
2713       1076         1  6 Pack Soft Drink                                             [Coke]        6.49
...         ...       ...                ...                                                ...         ...
2384        948         1  Veggie Soft Tacos  [Roasted Chili Corn Salsa, [Fajita Vegetables,...        8.75
781         322         1  Veggie Soft Tacos  [Fresh Tomato Salsa, [Black Beans, Cheese, Sou...        8.75
2851       1132         1  Veggie Soft Tacos  [Roasted Chili Corn Salsa (Medium), [Black Bea...        8.49
1699        688         1  Veggie Soft Tacos  [Fresh Tomato Salsa, [Fajita Vegetables, Rice,...       11.25
1395        567         1  Veggie Soft Tacos  [Fresh Tomato Salsa (Mild), [Pinto Beans, Rice...        8.49

[4622 rows x 5 columns] 

'''