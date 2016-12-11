from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from datetime import datetime,date

from glob import glob

import seaborn as sns
from matplotlib import pyplot as plt
from datetime import datetime,date,timedelta
#%matplotlib inline
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
import argparse

def Parse_CommandLine(parser):

    parser.add_argument("Team_Name", help="Team to be Analysed ")

    args = parser.parse_args()
    print("The Team to be analyzed is "+ args.Team_Name)
    return args

parser = argparse.ArgumentParser()
parse_result = Parse_CommandLine(parser)

Team_Name = parse_result.Team_Name
#print(url)

#Team_Name = url
#Team_Name = "Man United"

Attribute_columns = ['Season Year', 'Home Wins','Away Wins','Home Losses','Away Losses','Home Goals Conceeded','Away Goals Conceeded','Home Goals scored','Away Goals Scored','Total Points','Percentage Change in Points']
Attributes_all_years = pd.DataFrame(np.nan,index=[0], columns=Attribute_columns)
Attributes_single_year = list(range(11))

previous_Total_points = 65

loop_count = 0

for raw_file_ in glob("C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_1\Data\*.csv",):  #PATH_TO_DATA not working in my Windows PC
    _EPL_Year_df = pd.read_csv(raw_file_,error_bad_lines=False)
    
    season_year = raw_file_.split('\\')[-1].split('.')[0].split('_')[1]

    #Analysis #1 Get only set of Data Needed
    Analysis_1_Data = _EPL_Year_df[['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR']]

    _All_Matches_ = Analysis_1_Data.loc[(Analysis_1_Data["HomeTeam"] == Team_Name) | (Analysis_1_Data["AwayTeam"] == Team_Name)]

    _Home_Matches_ = _All_Matches_.loc[(_All_Matches_["HomeTeam"] == Team_Name)]
    _Away_Matches_ = _All_Matches_.loc[(_All_Matches_["AwayTeam"] == Team_Name)]

    Home_Wins = _Home_Matches_.loc[(_Home_Matches_["FTR"] == "H")]
    Home_Win_Count = Home_Wins.FTR.count()

    Home_loss = _Home_Matches_.loc[(_Home_Matches_["FTR"] == "A")]
    Home_loss_Count = Home_loss.FTR.count()

    Home_draw = _Home_Matches_.loc[(_Home_Matches_["FTR"] == "D")]
    Home_draw_Count = Home_draw.FTR.count()

    Away_Wins = _Away_Matches_.loc[(_Away_Matches_["FTR"] == "A")]
    Away_Wins_Count = Away_Wins.FTR.count()

    Away_loss = _Away_Matches_.loc[(_Away_Matches_["FTR"] == "H")]
    Away_loss_Count = Away_loss.FTR.count()

    Away_draw = _Away_Matches_.loc[(_Away_Matches_["FTR"] == "D")]
    Away_draw_Count = Away_draw.FTR.count()

    Home_Goals_scored = _Home_Matches_.FTHG.sum()
    Away_Goals_scored = _Away_Matches_.FTAG.sum()
    Home_Goals_conceeded = _Home_Matches_.FTAG.sum()
    Away_Goals_conceeded = _Away_Matches_.FTHG.sum()

    Total_Points = ((Home_Win_Count + Away_Wins_Count) * 3) + Home_draw_Count + Away_draw_Count
    Percentage_change_points = ((previous_Total_points - Total_Points)/previous_Total_points) * 100
    previous_Total_points = Total_Points
	
    Attributes_single_year[0] = season_year
    Attributes_single_year[1] = Home_Win_Count
    Attributes_single_year[2] = Away_Wins_Count
    Attributes_single_year[3] = Home_loss_Count
    Attributes_single_year[4] = Away_loss_Count
    Attributes_single_year[5] = Home_Goals_conceeded
    Attributes_single_year[6] = Away_Goals_conceeded
    Attributes_single_year[7] = Home_Goals_scored
    Attributes_single_year[8] = Away_Goals_scored
    Attributes_single_year[9] = Total_Points
    Attributes_single_year[10] = Percentage_change_points
    
    single_year_df = pd.DataFrame([Attributes_single_year],columns=Attribute_columns)

    Attributes_all_years = Attributes_all_years.append([single_year_df],ignore_index=True)
    
    loop_count += 1
    if loop_count == 8: break
    
Attributes_all_years = Attributes_all_years.drop(Attributes_all_years.index[0])

Attributes_all_years = Attributes_all_years.reset_index()

req_cols = ['Home Wins', 'Away Wins', 'Home Losses', 'Away Losses','Home Goals Conceeded', 'Away Goals Conceeded', 'Home Goals scored','Away Goals Scored', 'Total Points','Percentage Change in Points']
all_df = []

for col in req_cols:
    temp_df = Attributes_all_years[['Season Year',col]]
    temp_df = temp_df.rename(columns={col:'Season Statistics'})
    temp_df['Attributes'] = col
    all_df.append(temp_df)
f_df = pd.concat(all_df)

f, ax = plt.subplots(figsize=(20,10),dpi=96)
sns.set_style('whitegrid')
#sns.color_palette('afmhot')

sns.barplot(x='Season Year',y='Season Statistics',hue= 'Attributes',data=f_df,palette="YlOrBr")
ax.set_title('Team Statistics over the years',fontsize=40,color='#730039')
labels = ax.get_xticklabels()
plt.setp(labels, rotation=0, fontsize=20, color='#0165fc')
plt.xlabel('Different Seasons Year', fontsize=20, color='#00022e')
plt.ylabel('Value for Different Attributes', fontsize=20, color='#00022e')
plt.ylim([-50,100])
plt.tick_params(axis='both',which='major', width=3,length=8,color='r')

plt.savefig(r'C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Output\Analysis1.jpeg')
Attributes_all_years_file = "C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Output\Analysis_1.csv"
Attributes_all_years.to_csv(Attributes_all_years_file, sep=',', encoding='utf-8')



#plt.tick_params(which='major', length=7)
#plt.tick_params(which='minor', length=10, color='r')

#sns.barplot(x='Season Year',y='values_to_plot',label = 'Season',data=f_df)
#sns.barplot(x='hue',y='values_to_plot',label = 'hue data',data=f_df)

#ax.legend(ncol=2, loc="lower right", frameon=True)
#ax.set(xlim=(0, 24), ylabel="",
#       xlabel="Automobile collisions per billion miles")
#sns.despine(left=True, bottom=True)

#all_years