from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from datetime import datetime,date

from glob import glob

import seaborn as sns
from matplotlib import pyplot as plt
from datetime import datetime,date,timedelta
#%matplotlib inline


Team_Name4 = "Chelsea"
cnt = 0 

Composure_columns = ['Year','Total Shots', 'Home Shooting Accuracy','Away Shooting Accuracy','Fouls Commited','Being Stupid - Yellow carded','Dirty Fouls - Red Carded','Number of Set Pieces']
all_comp_years = pd.DataFrame(np.nan,index=[0], columns=Composure_columns)
single_comp_year = list(range(8))


for composure_file_ in glob("C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_4\Composure\*.csv",):
    _Composure_df_ = pd.read_csv(composure_file_,error_bad_lines=False)
    
    year = composure_file_.split('\\')[-1].split('.')[0].split('_')[1]

    #Analysis #4 Get only set of Data Needed
    Analysis_4_Data = _Composure_df_[['HomeTeam','AwayTeam','FTHG','FTAG','HS','AS','HST','AST','HC','AC','HF','AF','HY','AY','HR','AR']]

    _All_composure_Matches_ = Analysis_4_Data.loc[(Analysis_4_Data["HomeTeam"] == Team_Name4) | (Analysis_4_Data["AwayTeam"] == Team_Name4)]

    _Home_Comp_Matches_ = _All_composure_Matches_.loc[(_All_composure_Matches_["HomeTeam"] == Team_Name4)]
    _Away_Comp_Matches_ = _All_composure_Matches_.loc[(_All_composure_Matches_["AwayTeam"] == Team_Name4)]

    Home_Total_shots = _Home_Comp_Matches_.reset_index().HS.sum()
    Home_Total_shots_on_Target = _Home_Comp_Matches_.reset_index().HST.sum()
    Home_Goals_scored = _Home_Comp_Matches_.reset_index().FTHG.sum()
    Home_Shooting_accuracy = (Home_Goals_scored/Home_Total_shots_on_Target)*100
    Home_Fouls_commited = _Home_Comp_Matches_.reset_index().HF.sum()
    Home_Yellow_cards = _Home_Comp_Matches_.reset_index().HY.sum()
    Home_Red_cards = _Home_Comp_Matches_.reset_index().HR.sum()
    Home_Corners = _Home_Comp_Matches_.reset_index().HC.sum()
    
       
    Away_Total_shots = _Away_Comp_Matches_.reset_index().AS.sum()
    Away_Total_shots_on_Target = _Away_Comp_Matches_.reset_index().AST.sum()
    Away_Goals_scored = _Away_Comp_Matches_.reset_index().FTAG.sum()
    Away_Shooting_accuracy = (Away_Goals_scored/Away_Total_shots_on_Target)*100
    Away_Fouls_commited = _Away_Comp_Matches_.reset_index().AF.sum()
    Away_Yellow_cards = _Away_Comp_Matches_.reset_index().AY.sum()
    Away_Red_cards = _Away_Comp_Matches_.reset_index().AR.sum()
    Away_Corners = _Away_Comp_Matches_.reset_index().AC.sum()
     
        
    Total_Shots = Home_Total_shots + Away_Total_shots
    Total_Fouls = Home_Fouls_commited + Away_Fouls_commited
    Total_Yellow_cards = Home_Yellow_cards + Away_Yellow_cards
    Total_Red_cards = Home_Red_cards + Away_Red_cards
    Total_NUmber_Set_pieces = Home_Corners + Away_Corners
    
    single_comp_year[0] = year
    single_comp_year[1] = Total_Shots
    single_comp_year[2] = Home_Shooting_accuracy
    single_comp_year[3] = Away_Shooting_accuracy
    single_comp_year[4] = Total_Fouls
    single_comp_year[5] = Total_Yellow_cards
    single_comp_year[6] = Total_Red_cards
    single_comp_year[7] = Total_NUmber_Set_pieces
   
    
    single_comp_df = pd.DataFrame([single_comp_year],columns=Composure_columns)

    all_comp_years = all_comp_years.append([single_comp_df],ignore_index=True)
    
    
    cnt += 1
    if cnt == 111: break

all_comp_years = all_comp_years.drop(all_comp_years.index[0])

all_comp_years


league_all_comp_list = []
lll = 0
for League_comp_File in glob("C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_4\Composure_league_Table\*.csv"):
    League_comp_df = pd.read_csv(League_comp_File)
    League_comp_df['Year'] = League_comp_File.split('\\')[-1].split('.')[0].split('_')[-1]
    temp_comp_pos_df = League_comp_df[['Year','Pos','Team']]
    temp_comp_pos_df = temp_comp_pos_df.ix[temp_comp_pos_df['Team'].str.contains(Team_Name4)]
    league_all_comp_list.append(temp_comp_pos_df)
    
    lll +=1
    if lll == 17: break
    
Final_comp_league_df = pd.concat(league_all_comp_list)   
Final_comp_league_df.reset_index()


Analysi4_df =  pd.merge(Final_comp_league_df,all_comp_years,left_on='Year',right_on='Year')
Analysi4_df

Composure_req_cols = ['Total Shots','Home Shooting Accuracy','Away Shooting Accuracy','Fouls Commited','Being Stupid - Yellow carded','Dirty Fouls - Red Carded','Number of Set Pieces']
composure_plot_df = []

for col in Composure_req_cols:
    temp_df = Analysi4_df[['Year',col]]
    temp_df = temp_df.rename(columns={col:'Compsure_Attribute_Values'})
    temp_df['Composure Attributes'] = col
    composure_plot_df.append(temp_df)
    
Analysis4_plot_df = pd.concat(composure_plot_df)

Analysis4_plot_df['Compsure_Attribute_Values'] = Analysis4_plot_df.Compsure_Attribute_Values.apply(lambda Y: int(Y))

#Create Position List 

Postion_comp_list = list(Analysi4_df.Pos)
Postion_comp_list

label = 'League Table Finish ->  '

Postion_comp_text = [label + str(num) for num in Postion_comp_list]
Postion_comp_text

#create Annote arrow location 
Num_years = len(Analysi4_df)
cnt = 0

Annotate_comp_point = []
for year_idx in range(0,Num_years):
    year_to_cal = Analysi4_df['Year'][year_idx]

    Annotate_comp_df = Analysi4_df.ix[Analysi4_df['Year'].str.contains(year_to_cal)]

    Annotate1_comp_df =Annotate_comp_df[['Total Shots','Home Shooting Accuracy','Away Shooting Accuracy','Fouls Commited','Being Stupid - Yellow carded','Dirty Fouls - Red Carded','Number of Set Pieces']]


    #Annotate1_df['HighScore'] = Annotate1_df.apply(lambda X: cal_1(X), axis=1)

    Annotate1_comp_df['Annote_point'] = Annotate1_comp_df.max(axis=1)
    Annotate_comp_point.append(int(Annotate1_comp_df['Annote_point']))
    
    cnt += 1
    if cnt == 911: break
        
Annotate_comp_point


fig, ax4 = plt.subplots(figsize=(30,20), dpi=150)
sns.set_style('whitegrid')

axx = sns.barplot(x='Year',y='Compsure_Attribute_Values',hue= 'Composure Attributes', data = Analysis4_plot_df, palette="autumn")
#axx = sns.stripplot(x='Year',y='values_to_plot',hue= 'hue',data=Analysis4_plot_df,jitter=True)

ax4.set_title('How Composed is the Team Over the years',fontsize=40,color='#155084',loc = 'left')
labels = ax4.get_xticklabels()
plt.setp(labels, rotation=90, fontsize=30, color='#410200')

labels2 = ax4.get_yticklabels()
plt.setp(labels2, rotation=0, fontsize=30, color='#410200')

plt.xlabel('Over many Seasons', fontsize=40, color='#650021')
plt.ylabel('Composure Attributes Values', fontsize=40, color='#00022e')
#plt.ylim([0,90])
plt.tick_params(axis='both',which='major', width=3,length=6,color='r')
plt.legend(loc=1,prop={'size':15})

##plt.savefig(r'C:\Data Analysis\Sujay_DataAnalysis\Final\Output\Analysis2.jpeg')

Annotation_comp_len = len(Annotate_comp_point)

for label_idx in range(0,Annotation_comp_len):
    
    #label = 'League Table Finish ->  '
    axx.annotate(Postion_comp_text[label_idx], xy=(label_idx, Annotate_comp_point[label_idx] + 5),
        xytext=(label_idx, Annotate_comp_point[label_idx] + 30), 
            arrowprops=dict(facecolor='red'), 
            horizontalalignment='left', verticalalignment='top',fontsize=20)		
			
			
plt.savefig(r'C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Output\Analysis4.jpeg')		

Analysis4_plot_df_file = r"C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Output\Analysis_4.csv"
Analysis4_plot_df.to_csv(Analysis4_plot_df_file, sep=',', encoding='utf-8') 	