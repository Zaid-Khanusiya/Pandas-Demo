import pandas as pd

chipo = pd.read_csv('chipotle.csv')
chipo['item_price'] = chipo['item_price'].str.replace('$','').astype(float) # this is so that it removes the dollar sign from the front of item_price and converts it to float
print('\n Shape->',chipo.shape,'\n')

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