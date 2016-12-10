from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from datetime import datetime,date

from glob import glob

import seaborn as sns
from matplotlib import pyplot as plt
from datetime import datetime,date,timedelta
#%matplotlib inline

cnt2 = 0
goal_all_list = []

Team_Name_Goals = "Chelsea"

for Goals_file in glob(r"C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_3\Goals\*.csv"):
    Goals_df = pd.read_csv(Goals_file)
    Goals_df = Goals_df.drop(Goals_df.index[0])
    Goals_df['Year'] = Goals_file.split('\\')[-1].split('.')[0].split('_')[-1]
    Goals_df = Goals_df.rename(columns={'Unnamed: 0': 'Teams'})
    Goals_df = Goals_df.rename(columns={'0-10': 'Far in 10 minutes'})
    Goals_df = Goals_df.rename(columns={'0-10.1': 'Aganist in 10 minutes'})
    Goals_df = Goals_df.rename(columns={'20-Nov': 'Far in 20 minutes'})
    Goals_df = Goals_df.rename(columns={'20-Nov.1': 'Aganist in 20 minutes'})
    Goals_df = Goals_df.rename(columns={'21-30': 'Far in 30 minutes'})
    Goals_df = Goals_df.rename(columns={'21-30.1': 'Aganist in 30 minutes'})
    Goals_df = Goals_df.rename(columns={'31-40': 'Far in 40 minutes'})
    Goals_df = Goals_df.rename(columns={'31-40.1': 'Aganist in 40 minutes'})
    Goals_df = Goals_df.rename(columns={'41-50': 'Far in 50 minutes'})
    Goals_df = Goals_df.rename(columns={'41-50.1': 'Aganist in 50 minutes'})
    Goals_df = Goals_df.rename(columns={'51-60': 'Far in 60 minutes'})
    Goals_df = Goals_df.rename(columns={'51-60.1': 'Aganist in 60 minutes'})
    Goals_df = Goals_df.rename(columns={'61-70': 'Far in 70 minutes'})
    Goals_df = Goals_df.rename(columns={'61-70.1': 'Aganist in 70 minutes'})
    Goals_df = Goals_df.rename(columns={'71-80': 'Far in 80 minutes'})
    Goals_df = Goals_df.rename(columns={'71-80.1': 'Aganist in 80 minutes'})
    Goals_df = Goals_df.rename(columns={'81-90': 'Far in 90 minutes'})
    Goals_df = Goals_df.rename(columns={'81-90.1': 'Aganist in 90 minutes'})
    
    temp_goals_df = Goals_df[:]
    temp_goals_df = temp_goals_df.ix[temp_goals_df['Teams'].str.contains(Team_Name_Goals)]
    goal_all_list.append(temp_goals_df)

    cnt2 +=1
    if cnt2 == 10: break
        
        
Final_goal_df = pd.concat(goal_all_list)   
Final_goal_df.reset_index()


league_all_list = []
lll = 0
for League_File in glob("C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Input\Analysis_3\League_Table\*.csv"):
    League_df = pd.read_csv(League_File)
    League_df['Year'] = League_File.split('\\')[-1].split('.')[0].split('_')[-1]
    temp_pos_df = League_df[['Year','Pos','Team']]
    temp_pos_df = temp_pos_df.ix[temp_pos_df['Team'].str.contains(Team_Name_Goals)]
    league_all_list.append(temp_pos_df)
    
    lll +=1
    if lll == 10: break
    
Final_league_df = pd.concat(league_all_list)   
Final_league_df = Final_league_df.rename(columns={'Team': 'Teams'})
Final_league_df.reset_index()

Analysi3_df =  pd.merge(Final_league_df,Final_goal_df,left_on='Year',right_on='Year')
Analysi3_df =  Analysi3_df.rename(columns={'Teams_x':'Team'})
Analysi3_df = Analysi3_df.drop('Teams_y',1)

Goals_req_cols = ['Far in 10 minutes','Aganist in 10 minutes','Far in 20 minutes','Aganist in 20 minutes','Far in 30 minutes','Aganist in 30 minutes','Far in 40 minutes','Far in 50 minutes','Aganist in 50 minutes','Far in 60 minutes','Aganist in 60 minutes','Far in 70 minutes','Aganist in 70 minutes','Far in 80 minutes','Aganist in 80 minutes','Far in 90 minutes','Aganist in 90 minutes']
goal_plot_df = []

for col in Goals_req_cols:
    temp_df = Analysi3_df[['Year',col]]
    temp_df = temp_df.rename(columns={col:'values_to_plot'})
    temp_df['hue'] = col
    goal_plot_df.append(temp_df)
    
Analysis3_plot_df = pd.concat(goal_plot_df)

Analysis3_plot_df['values_to_plot'] = Analysis3_plot_df.values_to_plot.apply(lambda Y: int(Y))

#Create Position List 

Postion_list = list(Analysi3_df.Pos)
Postion_list

label = 'League Table Finish ->  '

Postion_text = [label + str(num) for num in Postion_list]
#Postion_text

Analysi3_df['Far in 10 minutes'] = Analysi3_df['Far in 10 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Aganist  in 10 minutes'] = Analysi3_df['Aganist in 10 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Far in 20 minutes'] = Analysi3_df['Far in 20 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Aganist  in 20 minutes'] = Analysi3_df['Aganist in 20 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Far in 30 minutes'] = Analysi3_df['Far in 30 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Aganist  in 30 minutes'] = Analysi3_df['Aganist in 30 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Far in 40 minutes'] = Analysi3_df['Far in 40 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Aganist  in 40 minutes'] = Analysi3_df['Aganist in 40 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Far in 50 minutes'] = Analysi3_df['Far in 50 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Aganist  in 50 minutes'] = Analysi3_df['Aganist in 50 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Far in 60 minutes'] = Analysi3_df['Far in 60 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Aganist  in 60 minutes'] = Analysi3_df['Aganist in 60 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Far in 70 minutes'] = Analysi3_df['Far in 70 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Aganist  in 70 minutes'] = Analysi3_df['Aganist in 70 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Far in 80 minutes'] = Analysi3_df['Far in 80 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Aganist  in 80 minutes'] = Analysi3_df['Aganist in 80 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Far in 90 minutes'] = Analysi3_df['Far in 90 minutes'].apply(lambda Y: int(Y))
Analysi3_df['Aganist  in 90 minutes'] = Analysi3_df['Aganist in 90 minutes'].apply(lambda Y: int(Y))

#Analysi3_df


#create Annote arrow location 

Num_years = len(Analysi3_df)
cnt = 0

Annotate_point = []
for year_idx in range(0,Num_years):
    year_to_cal = Analysi3_df['Year'][year_idx]

    Annotate_df = Analysi3_df.ix[Analysi3_df['Year'].str.contains(year_to_cal)]

    Annotate1_df =Annotate_df[['Far in 10 minutes','Aganist in 10 minutes','Far in 20 minutes','Aganist in 20 minutes','Far in 30 minutes','Aganist in 30 minutes','Far in 40 minutes','Far in 50 minutes','Aganist in 50 minutes','Far in 60 minutes','Aganist in 60 minutes','Far in 70 minutes','Aganist in 70 minutes','Far in 80 minutes','Aganist in 80 minutes','Far in 90 minutes','Aganist in 90 minutes']]

    Annotate1_df['Annote_point'] = Annotate1_df.max(axis=1)
    Annotate_point.append(int(Annotate1_df['Annote_point']))
    
    cnt += 1
    if cnt == 911: break
        
#Annotate_point


from matplotlib.font_manager import FontProperties

figure, ax3 = plt.subplots(figsize=(35,8),dpi=96)
sns.set_style('whitegrid')
axx = sns.swarmplot(x='Year',y='values_to_plot',hue= 'hue',data=Analysis3_plot_df,size=20,color= "#65fe08")

Annotation_len = len(Annotate_point)

ax3.set_title('Team Goal Scoring record over the seasons',fontsize=40,color='#155084')
labels = ax3.get_xticklabels()
plt.setp(labels, rotation=90, fontsize=20, color='#410200')

labels3 = ax3.get_yticklabels()
plt.setp(labels3, rotation=0, fontsize=20, color='#410200')

plt.xlabel('Over the Different seasons ', fontsize=30, color='#e50000')
plt.ylabel('Number of goals socred in specific minutes', fontsize=30, color='#00022e')
#plt.ylim([0,90])
plt.tick_params(axis='both',which='major', width=6,length=15,color='r')



#fontP = FontProperties()
#fontP.set_size('small')
plt.legend(loc=4,prop={'size':10})



for label_idx in range(0,Annotation_len):
    axx.annotate(Postion_text[label_idx], xy=(label_idx, Annotate_point[label_idx]),
        xytext=(label_idx, Annotate_point[label_idx] + 5), 
            arrowprops=dict(facecolor='blue'), 
            horizontalalignment='left', verticalalignment='top',fontsize=15)


plt.savefig(r'C:\Data Analysis\Sujay_DataAnalysis\Final_Exam\Output\Analysis3.jpeg')

