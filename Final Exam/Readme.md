## Table of Contents
==============
[Introduction](.#introduction)

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
I have used data from 2000/2001 - 2016/2017 english premier league data, which is located at the repository [League Data] (https://github.com/Sujaydas/DataAnalysisusingPython/tree/master/Final%20Exam/Input/Analysis_1/Data). Small snippet of the [EPL_2000-2001] (https://github.com/Sujaydas/DataAnalysisusingPython/blob/master/Final%20Exam/Input/Analysis_1/Data/EPL_2000-2001.csv) is shown below. Each of the .csv file is the information about the entire season, it has information about the date of each game, teams names, goals from each time, full time details, half time details, how many fouls, yellow cards, red cards count.


Div  |  Date      |  HomeTeam  |  AwayTeam       |  FTHG  |  FTAG  |  FTR  |  HTHG  |  HTAG  |  HTR  |  Attendance  |  Referee        |  HS  |  AS  |  HST  |  AST  |  HHW  |  AHW  |  HC  |  AC  |  HF  |  AF  |  HO  |  AO  |  HY  |  AY  |  HR  |  AR
-----|------------|------------|-----------------|--------|--------|-------|--------|--------|-------|--------------|-----------------|------|------|-------|-------|-------|-------|------|------|------|------|------|------|------|------|------|----
E0   |  19/08/00  |  Charlton  |  Man City       |  4     |  0     |  H    |  2     |  0     |  H    |  20043       |  Rob Harris     |  17  |  8   |  14   |  4    |  2    |  1    |  6   |  6   |  13  |  12  |  8   |  6   |  1   |  2   |  0   |  0
E0   |  19/08/00  |  Chelsea   |  West Ham       |  4     |  2     |  H    |  1     |  0     |  H    |  34914       |  Graham Barber  |  17  |  12  |  10   |  5    |  1    |  0    |  7   |  7   |  19  |  14  |  2   |  3   |  1   |  2   |  0   |  0
E0   |  19/08/00  |  Coventry  |  Middlesbrough  |  1     |  3     |  A    |  1     |  1     |  D    |  20624       |  Barry Knight   |  6   |  16  |  3    |  9    |  0    |  1    |  8   |  4   |  15  |  21  |  1   |  3   |  5   |  3   |  1   |  0
E0   |  19/08/00  |  Derby     |  Southampton    |  2     |  2     |  D    |  1     |  2     |  A    |  27223       |  Andy D'Urso    |  6   |  13  |  4    |  6    |  0    |  0    |  5   |  8   |  11  |  13  |  0   |  2   |  1   |  1   |  0   |  0

## Motivation
==============

Because of the way the human brain processes information, using charts or graphs to visualize large amounts of complex data is easier than poring over spreadsheets or reports. Data visualization is a quick, easy way to convey concepts in a universal manner – and you can experiment with different scenarios by making slight adjustments.

## Analysis 1
==============

Question Asked: How is the Team performing over the last 10 years, are they doing good in terms of points/at home , how they doing away?
--------------

Information:
--------------

Input:
--------------

<<<<<<< HEAD
Data set snippet shown below shows the Football league data over the last 10 years, where each season csv content is shown below,
 
Acronyms details are as:
Date = Match Date (dd/mm/yy)
HomeTeam = Home Team
AwayTeam = Away Teamm Goals
FTAG = Full Time Away Team Goals
FTHG = Full Time Home Tea
FTR = Full Time Result (H=Home Win, D=Draw, A=Away Win)
HTHG = Half Time Home Team Goals
HTAG = Half Time Away Team Goals
HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)



Div	Date	HomeTeam	AwayTeam	FTHG	FTAG	FTR	HTHG	HTAG	HTR	Referee	HS	AS	HST	AST	HF	AF
E0	19/08/06	Arsenal	Aston Villa	1	1	D	0	0	D	G Poll	19	5	11	3	10	19
E0	19/08/06	Bolton	Tottenham	2	0	H	2	0	H	P Dowd	8	9	6	6	19	22
E0	19/08/06	Everton	Watford	2	1	H	1	0	H	P Walton	6	12	2	8	12	13
E0	19/08/06	Newcastle	Wigan	2	1	H	1	0	H	M Atkinson	9	14	8	9	17	20
E0	19/08/06	Portsmouth	Blackburn	3	0	H	1	0	H	A Wiley	21	9	16	7	20	17
E0	19/08/06	Reading	Middlesbrough	3	2	H	2	2	D	M Halsey	14	7	9	5	8	15
=======
Data set snippet shown below shows the Football league data over the last 10 years, where each season csv content is shown below, 

![1](https://cloud.githubusercontent.com/assets/8064761/21072106/683d3382-be85-11e6-8718-792bc8ad7535.jpeg)

Acronyms details are as:

![2](https://cloud.githubusercontent.com/assets/8064761/21072107/7ac1d9c2-be85-11e6-96d3-b5d3a0dc4a4d.jpeg)

Output:
--------------
It shows different attributes such as, Percentage change in the Number of points, Number of Home Wins, Away Wins, Home Goals Scored for a particular team over the years.

![analysis1](https://cloud.githubusercontent.com/assets/8064761/21072053/c21777de-be83-11e6-96a1-19e8fb311bb7.jpeg)



## Analysis 2
==============

Question Asked: Does Different Manager have effect on the Team Performance!!!!
--------------

Information:
--------------

Input:
--------------

To Map which Manager was in Club From what time to End Time, I have used this data set

![3](https://cloud.githubusercontent.com/assets/8064761/21072165/24de39a4-be87-11e6-8d85-60af809f20c9.jpeg)

Output:
--------------

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
