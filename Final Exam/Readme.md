## Table of Contents
==============
* [Introduction](.#introduction)
    * [Data Set 1](.#data-set---1)
    * [Data Set 2](.#data-set---2)
    * [Data Set 3](.#data-set---3)
    * [Data Set 4](.#data-set---4)

[Motivation](.#motivation)

* [Analysis 1](.#analysis-1)
     * [Information](.#information)        
     * [Input](.#input)      
     * [Output](.#output)
* [Analysis 2](.#analysis-2)
     * [Information](.#information-1)        
     * [Input](.#input-1)      
     * [Output](.#output-1)
* [Analysis 3](.#analysis-3)
     * [Information](.#information-2)        
     * [Input](.#input-2)      
     * [Output](.#output-2)
* [Analysis 4](.#analysis-3)
     * [Information](.#information-3)        
     * [Input](.#input-3)      
     * [Output](.#output-3)
* [Analysis 5](.#analysis-4)
     * [Information](.#information-4)        
     * [Input](.#input-4)      
     * [Output](.#output-4)
     
     
## Introduction
==============
This Project Performs extensive analysis on the English Premier League Football/Soccer Data Set. This is open source data set provided and maintained by [Football.data.co.uk] (http://www.football-data.co.uk/englandm.php). 

## Data Set - 1
================
I have used data from 2000/2001 - 2016/2017 english premier league data, which is located at the repository [League Data] (https://github.com/Sujaydas/DataAnalysisusingPython/tree/master/Final%20Exam/Input/Analysis_1/Data). Small snippet of the [EPL_2000-2001] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_1/Data/EPL_2000-2001.csv) is shown below. Each of the .csv file is the information about the entire season, it has information about the date of each game, teams names, goals from each time, full time details, half time details, how many fouls, yellow cards, red cards count. Acronym details can be found in repository [Acronym] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_1/Notes.txt)



Div  |  Date      |  HomeTeam  |  AwayTeam       |  FTHG  |  FTAG  |  FTR  |  HTHG  |  HTAG  |  HTR  |  Attendance  |  Referee        |  HS  |  AS  |  HST  |  AST  |  HHW  |  AHW  |  HC  |  AC  |  HF  |  AF  |  HO  |  AO  |  HY  |  AY  |  HR  |  AR
-----|------------|------------|-----------------|--------|--------|-------|--------|--------|-------|--------------|-----------------|------|------|-------|-------|-------|-------|------|------|------|------|------|------|------|------|------|----
E0   |  19/08/00  |  Charlton  |  Man City       |  4     |  0     |  H    |  2     |  0     |  H    |  20043       |  Rob Harris     |  17  |  8   |  14   |  4    |  2    |  1    |  6   |  6   |  13  |  12  |  8   |  6   |  1   |  2   |  0   |  0
E0   |  19/08/00  |  Chelsea   |  West Ham       |  4     |  2     |  H    |  1     |  0     |  H    |  34914       |  Graham Barber  |  17  |  12  |  10   |  5    |  1    |  0    |  7   |  7   |  19  |  14  |  2   |  3   |  1   |  2   |  0   |  0
E0   |  19/08/00  |  Coventry  |  Middlesbrough  |  1     |  3     |  A    |  1     |  1     |  D    |  20624       |  Barry Knight   |  6   |  16  |  3    |  9    |  0    |  1    |  8   |  4   |  15  |  21  |  1   |  3   |  5   |  3   |  1   |  0
E0   |  19/08/00  |  Derby     |  Southampton    |  2     |  2     |  D    |  1     |  2     |  A    |  27223       |  Andy D'Urso    |  6   |  13  |  4    |  6    |  0    |  0    |  5   |  8   |  11  |  13  |  0   |  2   |  1   |  1   |  0   |  0

This data specifies Charlton and Manchester City has played a match on 19/08/2000 , where the full time score is 4-0 (FTHG = 4) favour of home team(charlton), Charlton has won the match indicated by the FTR = 'H'. Charlton has scored 2 goals in the first half (HTHG = 2).
Again, the acroynm and explanation about the each column and there meaning can be found at [Match Abbrevations] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_1/Notes.txt)


## Data Set - 2
================
This data is the collection of data about the managers for all clubs in english premier league from 1990 - Current. This data can be found in repository at [Managers Data] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_2/Manager/EPL_Managers.csv). Snippet of the Managers data set is shown below. Information in Mangers data set are name of the manager, Team the manager has managed, from which year to which year, number of days he handled the team.

Name             |  Nat.  |  Club     |  From       |  Until      |  Duration (days)  |  Years in Premier League
-----------------|--------|-----------|-------------|-------------|-------------------|-------------------------
George Graham    |        |  Arsenal  |  14-May-86  |  21-Feb-95  |  3205             |  1992▒??1995
Stewart Houston  |        |  Arsenal  |  22-Feb-95  |  8-Jun-95   |  106              |  1995
Bruce Rioch      |        |  Arsenal  |  8-Jun-95   |  12-Aug-96  |  431              |  1995▒??1996
Stewart Houston  |        |  Arsenal  |  12-Aug-96  |  13-Sep-96  |  32               |  1996



## Data Set - 3
================
This data set is collection of total Number of goals scored by each team/club in offset of 10 minutes for a season. I have collected the Data from 2005-2006 to 2013-2014. The data set can be found [Goal Data Set] (https://github.com/Sujaydas/DataAnalysisusingPython/tree/master/Final%20Exam/Input/Analysis_3/Goals). Each csv has information about the Name of the team played in that season and how many goals they scored in 10 minutes range. The goal data set csv can be found at [Goal Season CSV] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_3/Goals/Goal_time_2005-2006.csv). Snippet of the Data set is shown below.

             |  0-10  |  0-10  |  20-Nov  |  20-Nov  |  21-30  |  21-30  |  31-40  |  31-40  |  41-50  |  41-50  |  51-60  |  51-60  |  61-70  |  61-70  |  71-80  |  71-80  |  81-90  |  81-90
-------------|--------|--------|----------|----------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|-------
             |  F     |  A     |  F       |  A       |  F      |  A      |  F      |  A      |  F      |  A      |  F      |  A      |  F      |  A      |  F      |  A      |  F      |  A
Arsenal      |  4     |  1     |  10      |  5       |  7      |  3      |  9      |  7      |  8      |  1      |  5      |  2      |  2      |  2      |  8      |  8      |  15     |  2
Aston Villa  |  4     |  6     |  5       |  4       |  3      |  8      |  2      |  4      |  5      |  8      |  5      |  5      |  6      |  5      |  6      |  5      |  6      |  10
Birmingham   |  4     |  5     |  3       |  9       |  2      |  2      |  5      |  2      |  1      |  8      |  1      |  3      |  2      |  10     |  5      |  7      |  5      |  4
Blackburn    |  3     |  5     |  7       |  3       |  1      |  2      |  8      |  4      |  7      |  8      |  6      |  2      |  6      |  11     |  7      |  4      |  6      |  3


Top Column is the range of minutes. 0 - 10 columns is the column where the teams have scored the goals in 0 - 10 minutes. Sub column 'A' and 'F' contains the number of goals a team have conceeded ('A' = Aganist a team in that 0 - 10 minute range) and Scored ('F' = Far a team in that 0 - 10 minute range) 

## Data Set - 4
================
This Data set is Premier League Season Table for entire season. I have collected the from Season 2005/2006 to 2013/2014. This Data Set can be found at [League Table Data Set] (https://github.com/Sujaydas/DataAnalysisusingPython/tree/master/Final%20Exam/Input/Analysis_3/League_Table). Each csvn file contains the information about the position the each team/club ended up with. It has information about Number of matches each team has won, lost, drew. Goals scored, Goals defended and Total Points at the end of the league. League csv file can be found at [League csv File] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_3/League_Table/League_2006-2007.csv). Small snippet can be found below.

Pos  |  Team               |  Pld  |  W   |  D   |  L   |  GF  |  GA  |  GD  |  Pts  |  Qualification or relegation
-----|---------------------|-------|------|------|------|------|------|------|-------|--------------------------------------------------------
1    |  Chelsea?▒(C)       |  38   |  29  |  4   |  5   |  72  |  22  |  50  |  91   |  2006▒??07 UEFA Champions League Group stage
2    |  Manchester United  |  38   |  25  |  8   |  5   |  72  |  34  |  38  |  83   |
3    |  Liverpool          |  38   |  25  |  7   |  6   |  57  |  25  |  32  |  82   |  2006▒??07 UEFA Champions League Third qualifying round
4    |  Arsenal            |  38   |  20  |  7   |  11  |  68  |  31  |  37  |  67   |
5    |  Tottenham Hotspur  |  38   |  18  |  11  |  9   |  53  |  38  |  15  |  65   |  2006▒??07 UEFA Cup First round


## Motivation
==============

Motivation behind Data analysis using python because of the ease of process for obtaining raw data and converting it into information useful for decision-making by users. Data is collected and analyzed to answer questions, test hypotheses or disprove theories using python in very limited number of code.

Also because of the way the human brain processes information, using charts or graphs to visualize large amounts of complex data is easier than poring over spreadsheets or reports. Data visualization is a quick, easy way to convey concepts in a universal manner – and you can experiment with different scenarios by making slight adjustments.

## Analysis 1
==============

Question Asked: How is the Team performing over the last 10 years, are they doing good in terms of points/at home , how they doing away?
--------------

Information:
--------------
This Analysis uses the [League Data] (https://github.com/Sujaydas/DataAnalysisusingPython/tree/master/Final%20Exam/Input/Analysis_1/Data), to get the information about the team/club selected and process the data set to get Number of Home matches won, Away matches won, Home goals scored, Away goals conceeded, Total points in a season and Percentage change in the points from previous season. 

Input:
--------------

Pre Processing
--------------
Data collected from the open source has some errors in Date Column in terms of Date format , some entries have 26/08/00  format, some entries have   5/9/2000  format. Process entire data set and reformatted all date columns to 26/08/2000 format.

Div  |  Date      |  HomeTeam     |  AwayTeam    |  FTHG  |  FTAG  |  FTR  |  HTHG  |  HTAG  |  HTR  |  Attendance  |  Referee           |  HS  |  AS  |  HST  |  AST  |  HHW  |  AHW
-----|------------|---------------|--------------|--------|--------|-------|--------|--------|-------|--------------|--------------------|------|------|-------|-------|-------|-----
E0   |  26/08/00  |  West Ham     |  Man United  |  2     |  2     |  D    |  0     |  1     |  A    |  25998       |  Dermot Gallagher  |  17  |  8   |  8    |  5    |  0    |  2
E0   |  27/08/00  |  Aston Villa  |  Chelsea     |  1     |  1     |  D    |  1     |  1     |  D    |  27056       |  Paul Durkin       |  12  |  11  |  9    |  7    |  0    |  0
E0   |  5/9/2000  |  Leeds        |  Man City    |  1     |  2     |  A    |  0     |  2     |  A    |  40055       |  Graham Poll       |  6   |  8   |  1    |  3    |  1    |  1
E0   |  5/9/2000  |  Man United   |  Bradford    |  6     |  0     |  H    |  2     |  0     |  H    |  67447       |  Ian Harris        |  21  |  6   |  12   |  4    |  1    |  1


How to run the program:
--------------

  * Provide team name to be analysed in the python arguments as
  
      python Analysis_1.py "Man United"

Output:
--------------
It shows different attributes such as, Percentage change in the Number of points, Number of Home Wins, Away Wins, Home Goals Scored for a particular team over the years.

Output csv for the Analysis 1 can be found at [Analysis_1.csv] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Output/Analysis_1.csv)
Output Plot can be found in repository at [Analysis_1 Plot] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Output/Analysis1.jpeg)

Plot - Analysis 1
--------------

![analysis_1](https://cloud.githubusercontent.com/assets/8064761/21077862/9b5a04aa-bf27-11e6-92e6-1d33e6931d71.png)

Plot depicts the how the team is scoring at home, at away, and getting hit at home and away.

## Analysis 2
==============

Question Asked: Does Different Manager have effect on the Team Performance!!!!
--------------

Information:
--------------
This Analysis uses the data [Managers Data] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_2/Manager/EPL_Managers.csv), which is the collection of data about the managers for all clubs in english premier league from 1990 - Current.  

It also uses Data set League Data set, [EPL_2000-2001] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_1/Data/EPL_2000-2001.csv) is shown below. Each of the .csv file is the information about the entire season, it has information about the date of each game, teams names, goals from each time, full time details, half time details, how many fouls, yellow cards, red cards count.

This Analysis gives information about how the team is performing under different managers, on the selected team using the above Data sets. 

Input:
--------------

To Map which Manager was in Club From what time to End Time, I have used the Manager set and got the preprocessed data as below

![analysis_2_1](https://cloud.githubusercontent.com/assets/8064761/21077920/564d672e-bf29-11e6-9d0c-1f16869ac996.png)

![analysis_2_2](https://cloud.githubusercontent.com/assets/8064761/21077924/a33263aa-bf29-11e6-9666-8c0c770fd4d2.png)

And Using the [EPL_2000-2001] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_1/Data/EPL_2000-2001.csv) data set, I match Manager time with the club matches to get the corresponding winning and loss, points information, 

Another Intermediate Output will have Manager data mapped to League matches data as 

![analysis_2_3](https://cloud.githubusercontent.com/assets/8064761/21077943/121330ec-bf2a-11e6-9ad5-200d81d997a0.png)



Output:
--------------


It shows different attributes such as, Number of points, Number of Home Wins, Away Wins, Home Goals Scored for a particular team over the years under particular Manager

Output csv for the Analysis 2 can be found at [Analysis_2.csv] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Output/Analysis_2.csv)

Output Plot can be found in repository at [Analysis_2 Plot] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Output/Analysis2.jpeg)



Created a Map matching the managers performance for a particular season, where each season csv content is shown below,

![1](https://cloud.githubusercontent.com/assets/8064761/21072159/01397112-be87-11e6-8ea2-2c59aa73eeee.jpeg)

AS Shown below, the Analysis is done to check the manager does have impact on the Team winning and losing.

![2](https://cloud.githubusercontent.com/assets/8064761/21072166/2bd0e9b4-be87-11e6-8d3e-6c7c81d0b4df.png)



## Analysis 3
==============

Question Asked: How the scoring trend for a team has been, Does being in top position or lower position in table matters!!!
--------------

Information:
--------------

Input:
--------------
Data set snippet shown below shows the Goals scored by a team in the Year 2005-2006 , with the range 10 minutes gap

![1](https://cloud.githubusercontent.com/assets/8064761/21072198/3808d7a4-be88-11e6-96dd-4954d1dc37f8.png)

Below data snippet the data from the 2005-2006 Table with team rankings, 

![2](https://cloud.githubusercontent.com/assets/8064761/21072201/3ca7c996-be88-11e6-8a05-ced72d257932.jpeg)



Output:
--------------
AS Shown below, position of team is mapped to the scoring of goals in different minutes.

![3](https://cloud.githubusercontent.com/assets/8064761/21072202/3f68660e-be88-11e6-8816-b8e2c87f4e13.png)


## Analysis 4
==============

Question Asked: How Composed the team are, when they are in top of the league and when they are losing matches, does fouls related to positions??!!!
--------------

Information:
--------------

Input:
--------------
Data set snippet shown below shows the Shots Hit on Target, Yellow cards conceeded, Red cards conceeded ate Home/Away, Fouls Committed

![1](https://cloud.githubusercontent.com/assets/8064761/21072234/7174a968-be89-11e6-814e-72b45c372678.jpeg)

Below data snippet shows the expansion of the acronym, 

![2](https://cloud.githubusercontent.com/assets/8064761/21072235/7357742c-be89-11e6-804a-a84fe694174d.jpeg)


Output:
--------------
AS Shown below, When the position of the team is higher, Shot accuracy, is very good, and team is very well composed(not making much fouls),

![3](https://cloud.githubusercontent.com/assets/8064761/21072238/761ed4f2-be89-11e6-9123-2d33fca1c286.png)



## Analysis 5
==============

Question Asked: Can we make the Prediction of the upcoming Matches, based on the past meetings, current form. 
--------------

Information:
--------------

Input:
--------------
Data set snippet shown below shows detailed data of 2006-2007 , with full time score, half time score, Result of match

![1](https://cloud.githubusercontent.com/assets/8064761/21072271/a8dfa73a-be8a-11e6-9657-767f5a22705a.jpeg)

Output:
--------------
AS Shown below, it shows graph for the Form aganist the different Top teams and the prediction of winning aganist the team at Home, 

![2](https://cloud.githubusercontent.com/assets/8064761/21072272/aa25c6ec-be8a-11e6-9567-19e86139094b.png)





>>>>>>> 1df62ddcb8182e574c5223f7e6fa0f883615cf27
