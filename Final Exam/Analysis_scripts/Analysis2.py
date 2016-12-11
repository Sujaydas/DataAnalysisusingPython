from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from datetime import datetime,date

from glob import glob

import seaborn as sns
from matplotlib import pyplot as plt
from datetime import datetime,date,timedelta
#%matplotlib inline
import argparse

def Parse_CommandLine(parser):

    parser.add_argument("Team_Name", help="Team to be Analysed ")

    args = parser.parse_args()
    print("The Team to be analyzed is "+ args.Team_Name)
    return args

parser = argparse.ArgumentParser()
parse_result = Parse_CommandLine(parser)

Team_Name1 = parse_result.Team_Name


#Team_Name1 = "Chelsea"

_manger_file_ = r"C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_2\Manager\EPL_Managers.csv"
_Raw_file_ = pd.read_csv(_manger_file_)
_EPL_Managers_df = _Raw_file_[['Name','Club','From','Until','Duration (days)','Years in Premier League']]

_Team_Managers_ = _EPL_Managers_df[_EPL_Managers_df['Club'] == Team_Name1]

Managers_subset  = _Team_Managers_[['Name','From','Until']]
Managers_From_Until_df = Managers_subset.reset_index(drop=True)
Managers_From_Until_df.loc[len(Managers_From_Until_df) - 1 :,'Until'] = datetime.now().strftime("%d-%b-%y")
Managers_From_Until_df['From'] = Managers_From_Until_df['From'].apply(lambda X: datetime.strptime(X, "%d-%b-%y").date().strftime("%d/%m/%y"))
Managers_From_Until_df['Until'] = Managers_From_Until_df['Until'].apply(lambda X: datetime.strptime(X, "%d-%b-%y").date().strftime("%d/%m/%y"))

#Managers_From_Until_df

def GetYearFormat(x):
    ret_str = ""
    temp = x.split('/')[-1]
    if temp <= '16':
        ret_str = "20" + str(temp)
    elif temp > '16':
        ret_str = "19" + str(temp)
    else:
        ret_str = str(temp)
    return ret_str

def change_time(time):
    return datetime.strptime(time, "%d/%m/%y").timestamp()
    
    
Manager_year = Managers_From_Until_df[['From','Until']]
Manager_year['StartYear'] = Manager_year.apply(lambda X: GetYearFormat(X['From']), axis=1)
Manager_year['EndYear'] = Manager_year.apply(lambda X: GetYearFormat(X['Until']), axis=1)

Manager_year['FromEpoch'] = Manager_year.apply(lambda X: change_time(X['From']), axis=1)
Manager_year['UntilEpoch'] = Manager_year.apply(lambda X: change_time(X['Until']), axis=1)

#Manager_year

merged_manager = pd.merge(Managers_From_Until_df,Manager_year)

_MANGERS_and_Year = merged_manager[merged_manager['StartYear'] >= '2000'].reset_index(drop=True)
#_MANGERS_and_Year

dup_managers  = _MANGERS_and_Year[['Name','From','Until','StartYear','EndYear','FromEpoch','UntilEpoch']]
_MANGERS_TO_ANALYSE_ = dup_managers.drop_duplicates().reset_index(drop=True)
#_MANGERS_TO_ANALYSE_

def change_time_epoch(time):
    return datetime.strptime(time, "%d/%m/%y").timestamp()

def change_time_epoch2(time):
    return datetime.strptime(time, "%d/%m/%Y").timestamp()

def Get_Current_Manger(int_start_year, int_end_year):
    start_year = str(int_start_year)

    Start_year_list = _MANGERS_TO_ANALYSE_.loc[(_MANGERS_TO_ANALYSE_['StartYear'] == start_year)]['Name']
    Manager_name_split = Start_year_list.to_string().split(' ')[-2:]
    Manager_name = ' '.join(Manager_name_split)
    return Manager_name
    
    
def Get_manager(match_epoch, manager_start,manager_end,name):
    Match_day_str = str(match_epoch).split(' ')[-1]   #'990244800.0'
    Manger_start_str = str(float(manager_start.to_string().split(' ')[-1]))   #'9.68818e+08'
    Manger_end_str = str(float(manager_end.to_string().split(' ')[-1]))   #'9.68818e+08'

    if float(Match_day_str) > float(Manger_start_str):
        if float(Match_day_str) < float(Manger_end_str):
            return name
    else:
        print("")

    return "Interim Managers"

cnt = 0

Base_File_Name = "C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_1\Data\\"

Number_of_Managers = len(_MANGERS_TO_ANALYSE_)

for manager_number in range(0,Number_of_Managers):

    name = _MANGERS_TO_ANALYSE_.loc[manager_number,:].to_frame().transpose()['Name']

    Start_year = _MANGERS_TO_ANALYSE_.loc[manager_number,:].to_frame().transpose()['StartYear']
    End_year = _MANGERS_TO_ANALYSE_.loc[manager_number,:].to_frame().transpose()['EndYear']

    int_start_year = int(Start_year)
    int_end_year = int(End_year)

    Start_date = _MANGERS_TO_ANALYSE_.loc[manager_number,:].to_frame().transpose()['FromEpoch']
    End_date = _MANGERS_TO_ANALYSE_.loc[manager_number,:].to_frame().transpose()['UntilEpoch'] 

    No_seasons_in_Charge = int_end_year - int_start_year
    end = int_start_year + 1
    FIle_Name = Base_File_Name + "EPL" + "_" + str(int_start_year) + "-" + str(end) + ".csv"

    Season_file = pd.read_csv(FIle_Name,error_bad_lines=False)

    Analysis_2_Data = Season_file[['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR']]

    _All_Matches_ = Analysis_2_Data.loc[(Analysis_2_Data["HomeTeam"] == Team_Name1) | (Analysis_2_Data["AwayTeam"] == Team_Name1)]

    not_first_time = False

    if No_seasons_in_Charge == 0:
        _All_Matches_['DateEpoch'] = _All_Matches_.apply(lambda X: change_time_epoch(X['Date']), axis=1)

        matches_length = len(_All_Matches_['DateEpoch'])
        
        _All_Matches_['Manager'] = _All_Matches_.apply(lambda Y: Get_Current_Manger(int_start_year, int_end_year), axis=1)
        base_file = r"C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_2\Manager_season\\"
        Manager_season_file1 = base_file + "Managers_" + "EPL" + "_" + str(int_start_year) + "-" + str(int_start_year + 1) + ".csv"
            
        _All_Matches_.to_csv(Manager_season_file1, sep=',', encoding='utf-8')
            
    else:
    
        for season_in_charge in range(0,No_seasons_in_Charge + 1):            

            if not_first_time:

                int_start_year = int(Current_year) + 1
                int_end_year = int_start_year + 1
                FIle_Name = Base_File_Name + "EPL" + "_" + str(int_start_year) + "-" + str(int_end_year) + ".csv"
                Season_file = pd.read_csv(FIle_Name,error_bad_lines=False)     
                Analysis_2_Data = Season_file[['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR']]

                _All_Matches_ = Analysis_2_Data.loc[(Analysis_2_Data["HomeTeam"] == Team_Name1) | (Analysis_2_Data["AwayTeam"] == Team_Name1)]
            
            date1 = list(_All_Matches_.reset_index(drop=True).loc[0,:].to_frame().transpose()['Date'].to_string().split('/')[-1])

            format_lenght_1 = len(date1)

            if format_lenght_1 > 2:
                _All_Matches_['DateEpoch'] = _All_Matches_.apply(lambda X: change_time_epoch2(X['Date']), axis=1)
            else:
                _All_Matches_['DateEpoch'] = _All_Matches_.apply(lambda X: change_time_epoch(X['Date']), axis=1)
    
    
            
            matches_length = len(_All_Matches_['DateEpoch'])
            _All_Matches_['Manager'] = _All_Matches_.apply(lambda X: Get_manager(X['DateEpoch'],Start_date,End_date,name), axis=1)
                
            not_first_time = True
            base_file = r"C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_2\Manager_season\\"
            Manager_season_file = base_file + "Managers_" + "EPL" + "_" + str(int_start_year) + "-" + str(int_start_year + 1) + ".csv"
            
            _All_Matches_.to_csv(Manager_season_file, sep=',', encoding='utf-8')
            Current_year = int_start_year

        not_first_time = False
        
        
    #cnt += 1
    #if cnt == 10: break

#_All_Matches_


def Change_manager_str(Manager):
    temp1 = "";temp2 = ""; temp3 = ""
        
    if '[' in Manager:
        temp1 = Manager.replace('[','')
    
    if ']' in temp1:
        temp2 = temp1.replace(']','')
    
    if '\'' in temp2:
        temp3 = temp2.replace('\'','')
        return temp3
    
    return Manager
    
    
    
Manager_columns = ['Manager', 'Wins','Losses','Goals Conceeded','Goals scored']
all_years_managers = pd.DataFrame(np.nan,index=[0], columns=Manager_columns)
single_year_manager = list(range(5))
cnt1 =0

for Manager_file_ in glob("C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_2\Manager_season\*.csv",):
    _Manager_ALL_ = pd.read_csv(Manager_file_,error_bad_lines=False)
    
    year = Manager_file_.split('\\')[-1].split('.')[0].split('_')[1]
    
    All_Manager_Data = _Manager_ALL_[['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','Manager']]
    
    All_Manager_Data["Manager"] = All_Manager_Data.apply(lambda X: Change_manager_str(X['Manager']), axis=1)
    Managers_Names = All_Manager_Data['Manager'].unique()
    Number_of_mangers = len(Managers_Names)
        
    for count_manager in range(0,Number_of_mangers):
        
        Manager_name = Managers_Names[count_manager]
       
        Manager_Data = All_Manager_Data.loc[(All_Manager_Data["Manager"] == Manager_name)]
        _Home_Matches_ = Manager_Data.loc[(Manager_Data["HomeTeam"] == Team_Name1)]
        _Away_Matches_ = Manager_Data.loc[(Manager_Data["AwayTeam"] == Team_Name1)]

        Home_Wins = _Home_Matches_.loc[(_Home_Matches_["FTR"] == "H")]
        Home_Win_Count = Home_Wins.FTR.count()

        Home_loss = _Home_Matches_.loc[(_Home_Matches_["FTR"] == "A")]
        Home_loss_Count = Home_loss.FTR.count()

        Away_Wins = _Away_Matches_.loc[(_Away_Matches_["FTR"] == "A")]
        Away_Wins_Count = Away_Wins.FTR.count()

        Away_loss = _Away_Matches_.loc[(_Away_Matches_["FTR"] == "H")]
        Away_loss_Count = Away_loss.FTR.count()

        Home_Goals_scored = _Home_Matches_.FTHG.sum()
        Away_Goals_scored = _Away_Matches_.FTAG.sum()
        Home_Goals_conceeded = _Home_Matches_.FTAG.sum()
        Away_Goals_conceeded = _Away_Matches_.FTHG.sum()
        Total_Wins = Home_Win_Count + Away_Wins_Count
        Total_Loss = Home_loss_Count + Away_loss_Count
        Total_Goals_Scored = Home_Goals_scored + Away_Goals_scored
        Total_Goals_Conceeded = Home_Goals_conceeded + Away_Goals_conceeded
        
        single_year_manager[0] = Manager_name
        single_year_manager[1] = Total_Wins
        single_year_manager[2] = Total_Loss
        single_year_manager[3] = Total_Goals_Conceeded
        single_year_manager[4] = Total_Goals_Scored

        single_df = pd.DataFrame([single_year_manager],columns=Manager_columns)
        all_years_managers = all_years_managers.append([single_df],ignore_index=True)
    
    #cnt1 += 1
    #if cnt1 == 2: break

all_years_managers = all_years_managers.drop(all_years_managers.index[0])
#all_years_managers

all_years_managers_file = "C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Output\Analysis_2.csv"
all_years_managers.to_csv(all_years_managers_file, sep=',', encoding='utf-8')


req_cols = ['Wins','Losses','Goals Conceeded', 'Goals scored']
all_df = []

for col in req_cols:
    temp_df = all_years_managers[['Manager',col]]
    temp_df = temp_df.rename(columns={col:'Statistics Values'})
    temp_df['Attributes'] = col
    all_df.append(temp_df)
f_df = pd.concat(all_df)


fig, ax2 = plt.subplots(figsize=(60,20), dpi=150)
sns.set_style('whitegrid')
sns.barplot(x='Manager',y='Statistics Values',hue= 'Attributes',data=f_df,palette="YlGnBu")
#sns.stripplot(x='Manager',y='values_to_plot',hue= 'hue',data=f_df,jitter=True)
#sns.factorplot(x='Manager',y='values_to_plot',hue= 'hue',data=f_df,size=10)

ax2.set_title('Manager Performace over the years',fontsize=80,color='#155084')
labels = ax2.get_xticklabels()
plt.setp(labels, rotation=90, fontsize=50, color='#410200')

labels2 = ax2.get_yticklabels()
plt.setp(labels2, rotation=0, fontsize=40, color='#410200')

plt.xlabel('Different Managers over the year', fontsize=60, color='#ff028d')
plt.ylabel('Value for Different Attributes', fontsize=60, color='#00022e')
plt.ylim([0,90])
plt.tick_params(axis='both',which='major', width=6,length=15,color='r')
plt.legend(loc=1,prop={'size':50})

plt.savefig(r'C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Output\Analysis2.jpeg')
