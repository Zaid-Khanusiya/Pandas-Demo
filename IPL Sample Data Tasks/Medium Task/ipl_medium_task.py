import pandas

dataframe = pandas.read_excel("All_IPL_Match_Scores.xlsx")

# Question 1) Solution:

def is_close_match(row):
    if row['Winning_Team'] == 'Tie':
        return True
    if row['Balls_Remaining'] <= 3:
        return True
    if row['Winning_Team'] == 'Chasing' and row['Bat_Second_Wickets_Lost'] >= 9:
        return True
    if row['Winning_Team'] != 'Chasing' and row['Win_Type'] == 'run' and row['Winning_Margin'] <= 5:
        return True
    return False

close_match = dataframe.apply(is_close_match, axis=1)
close_mathes = dataframe[close_match].groupby('Year').Match_Number.count()
print(close_mathes,"\n")
'''
O/P:
Year
2008    28
2009    33
2010    28
2011    35
2012    46
2013    39
2014    33
2015    39

'''

# Question 2) Solution:

teams = ['Chennai', 'Hyderabad', 'Mumbai', 'Kolkata']
result = []

for team in teams:
    A = dataframe[dataframe['Winner'] == team].shape[0]
    B = dataframe[(dataframe['Winner'] == team) & (dataframe['Team_Batting_First'] == team)].shape[0]
    if A != 0:
        percent = (B / A) * 100
    else:
        percent = None
    result.append({'Team': team, 'Percent won batting first': round(percent,2)})

df_result = pandas.DataFrame(result)
print(df_result,"\n")
'''
O/P:
        Team  Percent won batting first
0    Chennai                      56.96
1  Hyderabad                      60.78
2     Mumbai                      56.16
3    Kolkata                      41.67 

'''