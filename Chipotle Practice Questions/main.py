import pandas as pd

chipo = pd.read_csv('chipotle.csv')
chipo['item_price'] = chipo['item_price'].str.replace('$','').astype(float) # this is so that it removes the dollar sign from the front of item_price and converts it to float
print('\n Shape->',chipo.shape,'\n')

'''
Breakdown of how .shape[] works:

DataFrame.shape → returns a Python tuple like this: --> (number_of_rows, number_of_columns)
now mostly we need no of rows and we use this after our filter for example this -->  more_than_10 = chipo[chipo_float_price > 10].shape[0]
doing this will first filter out based on condition and then apply .shape[] and then we tell to get no_or_rows by .shape[0]
and if we ever need no_of_column for some reason .shape[1] is the way... ;)
'''

# Q1) How many products cost more than 10.00$
more_than_10 = chipo[chipo['item_price'] > 10].shape[0]
print('\nNo of products costing more than 10.00$ : ',more_than_10,'\n')
'''
O/P:
No of products costing more than 10.00$ :  1130

'''

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

# Q5) How many times was "Veggie Salad Bowl" ordered
veggie_rows = chipo[chipo['item_name'] == 'Veggie Salad Bowl']
orders_count = veggie_rows.shape[0] # this will only count orders of veggie salab bowl not total quantity
veggie_quantities = veggie_rows['quantity']
total_bowls = veggie_quantities.sum() # this will calculate total quantity which is sold so if there are more than 1 bowl in same order it will consider that
print("Orders containing Veggie Salad Bowl:", orders_count)
print("Total Veggie Salad Bowls sold:", total_bowls,'\n')
'''
O/P:
Orders containing Veggie Salad Bowl: 18
Total Veggie Salad Bowls sold: 18

'''


# Q6 How many times did someone order more than one canned soda
chipo['quantity'] = chipo['quantity'].astype(int)
canned_soda = chipo[(chipo['item_name'] == 'Canned Soda') & (chipo['quantity'] > 1)]
total_times = canned_soda.shape[0]
print('Total times when someone ordered more than 1 Canned Soda:',total_times,'\n')
'''
O/P:
Total times when someone ordered more than 1 Canned Soda: 20

'''