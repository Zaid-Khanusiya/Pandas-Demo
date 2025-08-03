import pandas

dataframe = pandas.read_excel("All_IPL_Match_Scores_easy.xlsx")


# Question 1) Solution:
ans1 = dataframe.groupby('Year')['Match_Number'].count().rename('Total')

first_win_filter = dataframe["Winning_Team"]=="FirstBatting"
ans2 = dataframe[first_win_filter].groupby('Year')['Match_Number'].count().rename('FirstBatting')

chase_win_filter = dataframe["Winning_Team"]=="Chasing"
ans3 = dataframe[chase_win_filter].groupby('Year')['Match_Number'].count().rename('Chasing')

tie_filter = dataframe["Winning_Team"]=="Match Tied"
ans4 = dataframe[tie_filter].groupby('Year')['Match_Number'].count().rename('Tied')

answer_1 = pandas.concat([ans1,ans2,ans3,ans4],axis=1).fillna(0).astype(int)
print(answer_1,"\n")

'''
O/P:
Year  Total  FirstBatting  Chasing  Tied
                                    
2008     58            22       36     0
2009     57            26       30     1
2010     60            31       28     1
2011     72            32       40     0
2012     74            34       40     0
2013     76            37       37     2
2014     60            22       37     1
2015     57            32       24     1

'''

# Question 2) Solution:

venues = dataframe.groupby("Venue")["Match_Number"].count()
most_matches_venue = venues.sort_values(ascending=False).head(1)
print(most_matches_venue,"\n")

'''
O/P:
Venue
Mumbai    62

'''

# Question 3) Solution:

highest_run_rate_record = dataframe.loc[dataframe['Bat_First_Run_Rate'].idxmax()]
highest_run_rate_match = highest_run_rate_record.Match_Number
highest_rate_first_bat = highest_run_rate_record.Team_Batting_First
highest_rate_runs = highest_run_rate_record.Bat_First_Runs_Scored
highest_rate_overs = highest_run_rate_record.Bat_First_Overs_Consumed
print(highest_run_rate_match,highest_rate_first_bat,highest_rate_runs,highest_rate_overs,"\n")
'''
O/P:
Year    Total  FirstBatting  Chasing  Tied  
2008     58            22       36     0
2009     57            26       30     1
2010     60            31       28     1
2011     72            32       40     0
2012     74            34       40     0
2013     76            37       37     2
2014     60            22       37     1
2015     57            32       24     1 

Venue
Mumbai    62
Name: Match_Number, dtype: int64 

391 Bangalore 106 8.0 

'''