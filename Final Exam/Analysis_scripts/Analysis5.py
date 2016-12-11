from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from datetime import datetime,date

from glob import glob

import seaborn as sns
from matplotlib import pyplot as plt
from datetime import datetime,date,timedelta
#%matplotlib inline

Team_Name5 = 'Man United'
Prediction_Teams = ['Man United'  ,'Man City',  'Chelsea', 'Arsenal', 'Tottenham', 'Everton', 'West Ham', 'Liverpool']

cnt = 0

Prediction_list_length = len(Prediction_Teams)
cnt1 = 0
    
predict_columns = ['Team 1 ','Team 2','Home Form','Away Form','Home Wins','Home Losses','Home draws','Away Wins','Away Losses','Away draws']
predict_all_years = pd.DataFrame(np.nan,index=[0], columns=predict_columns)    
predict_single_year = list(range(10))

for pred_team in Prediction_Teams:
    if Team_Name5 == pred_team: continue
    Home_form_list = []
    Away_form_list = []
    
    Home_Wins = 0
    Home_Losses = 0
    Home_draws = 0
    Away_Wins = 0
    Away_Losses = 0
    Away_draws = 0
    
    
    for Prediction_file_ in glob("C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_5\Prediction\*.csv",):
        _prediction_df_ = pd.read_csv(Prediction_file_,error_bad_lines=False)

        year = Prediction_file_.split('\\')[-1].split('.')[0].split('_')[1]

        Analysis_5_Data = _prediction_df_[['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR']]

        _prediction_All_Matches_ = Analysis_5_Data.loc[(Analysis_5_Data["HomeTeam"] == Team_Name5) | (Analysis_5_Data["AwayTeam"] == Team_Name5)]

        _Home_prediction_Matches_ = _prediction_All_Matches_.loc[(_prediction_All_Matches_["HomeTeam"] == Team_Name5)]
        _Away_prediction_Matches_ = _prediction_All_Matches_.loc[(_prediction_All_Matches_["AwayTeam"] == Team_Name5)]

    
        Home_temp_df = _prediction_All_Matches_.loc[(_prediction_All_Matches_["HomeTeam"] == Team_Name5) 
                                                & (_prediction_All_Matches_["AwayTeam"] == pred_team)]
           
        if not Home_temp_df.empty:
            Home_temp_df = Home_temp_df.reset_index()
            if Home_temp_df.FTR[0] == 'H':
                home_form_ch = 'W'
                Home_Wins +=1                
            elif Home_temp_df.FTR[0] == 'A':
                home_form_ch = 'L'
                Home_Losses += 1
            elif Home_temp_df.FTR[0] == 'D':
                home_form_ch = 'D'
                Home_draws += 1

            Home_form_list.append(home_form_ch)
        else:
            Home_form_list.append('') 
    
        Away_temp_df = _prediction_All_Matches_.loc[(_prediction_All_Matches_["HomeTeam"] == pred_team) 
                                                   & (_prediction_All_Matches_["AwayTeam"] == Team_Name5)]
    
        if not Away_temp_df.empty:
            Away_temp_df = Away_temp_df.reset_index()
            if Away_temp_df.FTR[0] == 'H':
                away_form_ch = 'W'
                Away_Wins += 1
            elif Away_temp_df.FTR[0] == 'A':
                away_form_ch = 'L'
                Away_Losses += 1
            elif Away_temp_df.FTR[0] == 'D':
                away_form_ch = 'D'
                Away_draws += 1

            Away_form_list.append(away_form_ch)
        else:
            Away_form_list.append('')
        
        cnt +=1 
        if cnt == 30: break
        
    predict_single_year[0] =  Team_Name5
    predict_single_year[1] =  pred_team
    predict_single_year[2] =  ' '.join(Home_form_list) 
    predict_single_year[3] =  ' '.join(Away_form_list)
    predict_single_year[4] =  Home_Wins
    predict_single_year[5] =  Home_Losses
    predict_single_year[6] =  Home_draws
    predict_single_year[7] =  Away_Wins
    predict_single_year[8] =  Away_Losses
    predict_single_year[9] =  Away_draws
    
    predict_single_df = pd.DataFrame([predict_single_year],columns=predict_columns)
    
    predict_all_years = predict_all_years.append([predict_single_df],ignore_index=True)

    cnt1 += 1
    if cnt1 == 10: break
        

print(Home_form_list)
print(Away_form_list)


predict_all_years = predict_all_years.drop(predict_all_years.index[0])
#predict_all_years

#prediction algorithm
#1.  previous years  at this point average wins and    30 
#2  Previous meetings with team   30 
#3  Current form                  40
 
 
def current_form(Home_team, Away_team, Result):
    
    if (Home_team == Team_Name5) and (Away_team != Team_Name5):
        if Result == 'H':
            return 'W'
        if Result == 'A':
            return 'L'
        if Result == 'D':
            return 'D'        
    if (Home_team != Team_Name5) and (Away_team == Team_Name5):
        if Result == 'H':
            return 'L'     
        if Result == 'A':
            return 'W'         
        if Result == 'D':
            return 'D'         

temp_file = pd.read_csv(r'C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_5\Prediction\EPL_2016-2017.csv')
Average_Predict_file = temp_file[['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR']]
_Average_predict_df_ = Average_Predict_file.loc[(Average_Predict_file["HomeTeam"] == Team_Name5) | (Average_Predict_file["AwayTeam"] == Team_Name5)]

_Average_predict_df_ = _Average_predict_df_.reset_index()

_Current_Home_Matches_ = _Average_predict_df_.loc[(_Average_predict_df_["HomeTeam"] == Team_Name5)]
_Current_Away__Matches_ = _Average_predict_df_.loc[(_Average_predict_df_["AwayTeam"] == Team_Name5)]

        
_AverageHome_Wins = _Current_Home_Matches_.loc[(_Average_predict_df_["FTR"] == "H")]
_AverageHome_Win_Count = _AverageHome_Wins.FTR.count()

_AverageHome_draw = _Current_Home_Matches_.loc[(_Average_predict_df_["FTR"] == "D")]
_AverageHome_draw_Count = _AverageHome_draw.FTR.count()

_AverageAway_Wins = _Current_Away__Matches_.loc[(_Average_predict_df_["FTR"] == "A")]
_AverageAway_Wins_Count = _AverageAway_Wins.FTR.count()

_AverageAway_draw = _Current_Away__Matches_.loc[(_Average_predict_df_["FTR"] == "D")]
_AverageAway_draw_Count = _AverageAway_draw.FTR.count()


_AverageTotal_Wins = _AverageHome_Win_Count + _AverageAway_Wins_Count
_AverageTotal_Points = ((_AverageTotal_Wins) * 3) + _AverageHome_draw_Count + _AverageAway_draw_Count

_Average_predict_df_['Current Form'] = _Average_predict_df_.apply(lambda X: current_form(X['HomeTeam'],X['AwayTeam'],X['FTR']),axis=1)

#_Average_predict_df_


Current_league_len = len(_Average_predict_df_)

Max_form_matrix = 0

Current_form_list = list(_Average_predict_df_['Current Form'])

Current_form_list_length = len(Current_form_list)

Current_form_Matrix = 0

for form_idx in range(0,Current_form_list_length):
    if Current_form_list[form_idx] == 'W': 
        Max_form_matrix += 3
        Current_form_Matrix += 3
    elif Current_form_list[form_idx] == 'L':
        Max_form_matrix += 3
        #Current_form_Matrix -= 3    
    if Current_form_list[form_idx] == 'D':
        Max_form_matrix += 3
        Current_form_Matrix += 1
        
#Current_form_Matrix
#Max_form_matrix


temp_value3 = ((Max_form_matrix - Current_form_Matrix)/Max_form_matrix) * 100
#temp_value3


#making to 15% range
temp_value_4 = (temp_value3 * 40) /100
Predict_value_3 = 40 - temp_value_4
#Predict_value_3



cnt = 0

predict_avg_columns = ['Total Points','Total Wins']
predict_avg_years = pd.DataFrame(np.nan,index=[0], columns=predict_avg_columns)    
predict_avg_single_year = list(range(2))


for Prediction_file1_ in glob("C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_5\Prediction\*.csv",):
    
    _prediction_df1_ = pd.read_csv(Prediction_file1_,error_bad_lines=False)

    year = Prediction_file1_.split('\\')[-1].split('.')[0].split('_')[1]

    Analysis_5_Data1 = _prediction_df1_[['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR']]

    temp_prediction = Analysis_5_Data1.loc[(Analysis_5_Data1["HomeTeam"] == Team_Name5) | (Analysis_5_Data1["AwayTeam"] == Team_Name5)]
    
    _prediction_All_Matches1_ = temp_prediction.reset_index().loc[:Current_league_len,:]

    _Home_prediction_Matches1_ = _prediction_All_Matches1_.loc[(_prediction_All_Matches1_["HomeTeam"] == Team_Name5)]
    _Away_prediction_Matches1_ = _prediction_All_Matches1_.loc[(_prediction_All_Matches1_["AwayTeam"] == Team_Name5)]
    
    
    Home_Wins = _Home_prediction_Matches1_.loc[(_Home_prediction_Matches1_["FTR"] == "H")]
    Home_Win_Count = Home_Wins.FTR.count()

    Home_draw = _Home_prediction_Matches1_.loc[(_Home_prediction_Matches1_["FTR"] == "D")]
    Home_draw_Count = Home_draw.FTR.count()

    Away_Wins = _Away_prediction_Matches1_.loc[(_Away_prediction_Matches1_["FTR"] == "A")]
    Away_Wins_Count = Away_Wins.FTR.count()

    Away_draw = _Away_prediction_Matches1_.loc[(_Away_prediction_Matches1_["FTR"] == "D")]
    Away_draw_Count = Away_draw.FTR.count()

    Home_Goals_scored = _Home_prediction_Matches1_.FTHG.sum()
    Away_Goals_scored = _Away_prediction_Matches1_.FTAG.sum()
    Home_Goals_conceeded = _Home_prediction_Matches1_.FTAG.sum()
    Away_Goals_conceeded = _Away_prediction_Matches1_.FTHG.sum()
    
    Total_Wins = Away_Wins_Count + Home_Win_Count
    Total_Points = ((Home_Win_Count + Away_Wins_Count) * 3) + Home_draw_Count + Away_draw_Count
    
    predict_avg_single_year[0] =  Total_Points
    predict_avg_single_year[1] =  Total_Wins

    
    predict_avg_single_df = pd.DataFrame([predict_avg_single_year],columns=predict_avg_columns)
    
    predict_avg_years = predict_avg_years.append([predict_avg_single_df],ignore_index=True)
    
    cnt += 1
    if cnt == 19: break

predict_avg_years = predict_avg_years.drop(predict_avg_years.index[0])
#predict_avg_years



Average_Total_point_At_this_point = predict_avg_years['Total Points'].mean()
Average_Total_wins_At_this_point = predict_avg_years['Total Wins'].mean()


#1   How much down 

Current_point_percentage = ((Average_Total_point_At_this_point - _AverageTotal_Points)/ Average_Total_point_At_this_point)* 100
#Current_point_percentage


#making to 15% range
temp_value_1 = (Current_point_percentage * 15) /100
Predict_value_1 = 15 - temp_value_1
#Predict_value_1


Current_wins_percentage = ((Average_Total_wins_At_this_point - _AverageTotal_Wins)/ Average_Total_wins_At_this_point)* 100
#Current_wins_percentage

#making to 15% range
temp_value_2 = (Current_wins_percentage * 15) /100
Predict_value_2 = 15 - temp_value_2
#Predict_value_2

def old_form(Home_form):
   
    form_list = Home_form.split(' ')
    form_list_length = len(form_list)
    Max_old_form_matrix  = 0
    Old_form_Matrix = 0
        
    for idx in range(0,form_list_length):
        if form_list[idx] == 'W':
            Max_old_form_matrix += 3
            Old_form_Matrix += 3
        elif form_list[idx] == 'L':
            Max_old_form_matrix  += 3
            Old_form_Matrix -= 3
        elif form_list[idx] == 'D':
            Max_old_form_matrix  += 3
            Old_form_Matrix += 1
    
    temp_value5 = ((Max_old_form_matrix - Old_form_Matrix)/Max_old_form_matrix) * 100
    temp_value_6 = (temp_value5 * 30) /100
    Predict_value_4 = 30 - temp_value_6

    return (Predict_value_1 + Predict_value_2 + Predict_value_3 + Predict_value_4 )

Average_predict_all_years = predict_all_years[['Team 2','Home Form','Away Form','Home Wins','Home Losses','Home draws','Away Wins','Away Losses','Away draws']]
Average_predict_all_years['Home Prediction'] = Average_predict_all_years['Home Form'].apply(old_form,1)
Average_predict_all_years['Away Prediction'] = Average_predict_all_years['Away Form'].apply(old_form,1)
#Average_predict_all_years
Average_predict_all_years_file = r"C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Output\Analysis_5.csv"
Average_predict_all_years.to_csv(Average_predict_all_years_file, sep=',', encoding='utf-8') 


sns.set(style="whitegrid")

# Initialize the matplotlib figure
f, ax5 = plt.subplots(figsize=(100, 25))

sns.barplot(x="Home Prediction", y="Team 2", data=Average_predict_all_years,
            label="Home win Prediction %", color="#fffd01")

#sns.barplot(x="Away Prediction", y="Team 2", data=Average_predict_all_years,
 #           label="Away win Prediction %", color="#ffda03")

sns.barplot(x="Home Wins", y="Team 2", data=Average_predict_all_years,
            label="Home Wins", color="#21fc0d")

#sns.set_color_codes("muted")
#sns.barplot(x="Home Losses", y="Team 2", data=predict_all_years,
#            label="Home Losses", color="#b6ffbb")

#sns.set_color_codes("bright")
sns.barplot(x="Away Wins", y="Team 2", data=Average_predict_all_years,
            label="Away Wins", color="#010fcc")


ax5.set_title('What are the chances of Winning the Next Match at Home or Away',fontsize=90,color='#155084')
labels = ax5.get_xticklabels()
plt.setp(labels, rotation=90, fontsize=50, color='#410200')

labels2 = ax5.get_yticklabels()
plt.setp(labels2, rotation=0, fontsize=60, color='#410200')

plt.xlabel('Number of Wins/Losses/Home Prediction/Away Prediction', fontsize=70, color='#650021')
plt.ylabel('Prediction aganist Top Teams - Names', fontsize=70, color='#00022e')
#plt.ylim([0,90])
plt.tick_params(axis='both',which='major', width=10,length=16,color='r')



ax5.legend(ncol=4, loc="upper right", frameon=True,prop={'size':65})
#ax.set(xlim=(0, 24), ylabel="",
#       xlabel="Automobile collisions per billion miles")
#sns.despine(left=True, bottom=True)


plt.savefig(r'C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Output\Analysis5.jpeg')





