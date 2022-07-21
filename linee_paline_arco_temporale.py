# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:43:07 2020

@author: M. Tilocca
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import datetime 
import calendar
import random

# per importare il file csv mettere al posto di "r'C:\Users\M. Tilocca\Desktop\edX\prova\combfile.csv'" la directory del nuovo file
# la quale sara diversa per ogni computer. eg("r'C:\Users\Utente\Desktop\cartella1\dati\combfile.csv'"). 
df = pd.read_csv (r'C:\Users\M. Tilocca\Desktop\edX\prova\combineddatafile.csv', index_col=0, error_bad_lines=False)  # import the csv file
matr = pd.read_csv (r'C:\Users\M. Tilocca\Desktop\edX\prova\matrix.csv', index_col=0, error_bad_lines=False)  # import the csv file

# inserire al posto di ('C:\Users\M. Tilocca\Desktop\edX\prova\combineddatafile.csv')  nella linea 10 la directory di dove si trova il file csv contentente i dati da analizzare, lasciare il resto della linea uguale
# inserire al posto di ('C:\Users\M. Tilocca\Desktop\edX\prova\matrix.csv')  nella linea 11 la directory di dove si trova il file csv contentente la matrice di calibrazione matrix.csv, lasciare il resto della linea uguale

arr = matr.to_numpy()
coeff = np.delete(arr, 0, 0)
#df = df.loc[ : , ['properties__codicePalina','properties__codiceLinea','properties__codiceUtente','day','time_slot_from']]# column selector
#df = df.drop_duplicates()  # remove duplicates 

# scommentare linea  24 e 25 in caso nel file sia presente una colonna contenente i codice utente, cosi`da rimuovere eventuali duplicati  

a = df['day'].unique() # finding what are the days present in the dataframe
tmp = 'a'

m = input("Linea, Palina o Utente ? [l,p,u] \n")

###############################################
if m == 'l':
    h = input("Quale Linea ? \n")
elif m == 'p':
    h = input("Quale Palina ? \n")
elif m == 'u': 
    h = input("Quale Utente? \n")
##############################################
j = input("Quale giorno settimanale nell' arco temporale ? [lu/ma/me/gi/ve/sa/do]\n")


if j == 'lu':
    dy = 'Monday'
elif j == 'ma':
    dy = 'Tuesday'
elif j == 'me': 
    dy = 'Wednesday'
elif j == 'gi': 
    dy = 'Thursday'
elif j == 've': 
    dy = 'Friday'
elif j == 'sa': 
    dy = 'Saturday'
elif j == 'do': 
    dy = 'Sunday'

##############
if m == 'l':
    tmp = 'properties__codiceLinea'
elif m == 'p':
    tmp = 'properties__codicePalina'
elif m == 'u': 
    tmp = 'properties__codiceUtente'


# day selecting function
def findDay(date): 
    giorno = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    return (calendar.day_name[giorno]) 
###################################################
# selecting the days and storing them in a list
j = []
for i in a: 
    date = i
    if findDay(date) == dy :
        j.append(date)
####### selecting the data columns and rows we are interested in

columnsData = df.loc[: , [tmp, 'day', 'time_slot_from']   ]# column selector  
columnsData[tmp] = columnsData[tmp].astype(str)
rowsData = columnsData.loc[columnsData[tmp] == str(h)] # row selector 
#######################################################
counter = np.zeros((96, len(j)), dtype=float) # create empy 2D numpy array where later storing the data points to plot 
############################################################################################################################################################### 
# data points counting function 
def function(utentex):
    s1 = utentex.loc[utentex['time_slot_from'] == '00:00:00']; s2 = utentex.loc[utentex['time_slot_from'] == '00:15:00']; s3 = utentex.loc[utentex['time_slot_from'] == '00:30:00']; s4 = utentex.loc[utentex['time_slot_from'] == '00:45:00']
    s5 = utentex.loc[utentex['time_slot_from'] == '01:00:00']; s6 = utentex.loc[utentex['time_slot_from'] == '01:15:00']; s7 = utentex.loc[utentex['time_slot_from'] == '01:30:00']; s8 = utentex.loc[utentex['time_slot_from'] == '01:45:00']
    s9 = utentex.loc[utentex['time_slot_from'] == '02:00:00']; s10 = utentex.loc[utentex['time_slot_from'] == '02:15:00']; s11 = utentex.loc[utentex['time_slot_from'] == '02:30:00']; s12 = utentex.loc[utentex['time_slot_from'] == '02:45:00']
    s13 = utentex.loc[utentex['time_slot_from'] == '03:00:00']; s14 = utentex.loc[utentex['time_slot_from'] == '03:15:00']; s15 = utentex.loc[utentex['time_slot_from'] == '03:30:00']; s16 = utentex.loc[utentex['time_slot_from'] == '03:45:00']
    s17 = utentex.loc[utentex['time_slot_from'] == '04:00:00']; s18 = utentex.loc[utentex['time_slot_from'] == '04:15:00']; s19 = utentex.loc[utentex['time_slot_from'] == '04:30:00']; s20 = utentex.loc[utentex['time_slot_from'] == '04:45:00']
    s21 = utentex.loc[utentex['time_slot_from'] == '05:00:00']; s22 = utentex.loc[utentex['time_slot_from'] == '05:15:00']; s23 = utentex.loc[utentex['time_slot_from'] == '05:30:00']; s24 = utentex.loc[utentex['time_slot_from'] == '05:45:00']
    s25 = utentex.loc[utentex['time_slot_from'] == '06:00:00']; s26 = utentex.loc[utentex['time_slot_from'] == '06:15:00']; s27 = utentex.loc[utentex['time_slot_from'] == '06:30:00']; s28 = utentex.loc[utentex['time_slot_from'] == '06:45:00']
    s29 = utentex.loc[utentex['time_slot_from'] == '07:00:00']; s30 = utentex.loc[utentex['time_slot_from'] == '07:15:00']; s31 = utentex.loc[utentex['time_slot_from'] == '07:30:00']; s32 = utentex.loc[utentex['time_slot_from'] == '07:45:00']
    s33 = utentex.loc[utentex['time_slot_from'] == '08:00:00']; s34 = utentex.loc[utentex['time_slot_from'] == '08:15:00']; s35 = utentex.loc[utentex['time_slot_from'] == '08:30:00']; s36 = utentex.loc[utentex['time_slot_from'] == '08:45:00']
    s37 = utentex.loc[utentex['time_slot_from'] == '09:00:00']; s38 = utentex.loc[utentex['time_slot_from'] == '09:15:00']; s39 = utentex.loc[utentex['time_slot_from'] == '09:30:00']; s40 = utentex.loc[utentex['time_slot_from'] == '09:45:00']
    s41 = utentex.loc[utentex['time_slot_from'] == '10:00:00']; s42 = utentex.loc[utentex['time_slot_from'] == '10:15:00']; s43 = utentex.loc[utentex['time_slot_from'] == '10:30:00']; s44 = utentex.loc[utentex['time_slot_from'] == '10:45:00']
    s45 = utentex.loc[utentex['time_slot_from'] == '11:00:00']; s46 = utentex.loc[utentex['time_slot_from'] == '11:15:00']; s47 = utentex.loc[utentex['time_slot_from'] == '11:30:00']; s48 = utentex.loc[utentex['time_slot_from'] == '11:45:00']
    s49 = utentex.loc[utentex['time_slot_from'] == '12:00:00']; s50 = utentex.loc[utentex['time_slot_from'] == '12:15:00']; s51 = utentex.loc[utentex['time_slot_from'] == '12:30:00']; s52 = utentex.loc[utentex['time_slot_from'] == '12:45:00']
    s53 = utentex.loc[utentex['time_slot_from'] == '13:00:00']; s54 = utentex.loc[utentex['time_slot_from'] == '13:15:00']; s55 = utentex.loc[utentex['time_slot_from'] == '13:30:00']; s56 = utentex.loc[utentex['time_slot_from'] == '13:45:00']
    s57 = utentex.loc[utentex['time_slot_from'] == '14:00:00']; s58 = utentex.loc[utentex['time_slot_from'] == '14:15:00']; s59 = utentex.loc[utentex['time_slot_from'] == '14:30:00']; s60 = utentex.loc[utentex['time_slot_from'] == '14:45:00']
    s61 = utentex.loc[utentex['time_slot_from'] == '15:00:00']; s62 = utentex.loc[utentex['time_slot_from'] == '15:15:00']; s63 = utentex.loc[utentex['time_slot_from'] == '15:30:00']; s64 = utentex.loc[utentex['time_slot_from'] == '15:45:00']
    s65 = utentex.loc[utentex['time_slot_from'] == '16:00:00']; s66 = utentex.loc[utentex['time_slot_from'] == '16:15:00']; s67 = utentex.loc[utentex['time_slot_from'] == '16:30:00']; s68 = utentex.loc[utentex['time_slot_from'] == '16:45:00']
    s69 = utentex.loc[utentex['time_slot_from'] == '17:00:00']; s70 = utentex.loc[utentex['time_slot_from'] == '17:15:00']; s71 = utentex.loc[utentex['time_slot_from'] == '17:30:00']; s72 = utentex.loc[utentex['time_slot_from'] == '17:45:00']
    s73 = utentex.loc[utentex['time_slot_from'] == '18:00:00']; s74 = utentex.loc[utentex['time_slot_from'] == '18:15:00']; s75 = utentex.loc[utentex['time_slot_from'] == '18:30:00']; s76 = utentex.loc[utentex['time_slot_from'] == '18:45:00']
    s77 = utentex.loc[utentex['time_slot_from'] == '19:00:00']; s78 = utentex.loc[utentex['time_slot_from'] == '19:15:00']; s79 = utentex.loc[utentex['time_slot_from'] == '19:30:00']; s80 = utentex.loc[utentex['time_slot_from'] == '19:45:00'] 
    s81 = utentex.loc[utentex['time_slot_from'] == '20:00:00']; s82 = utentex.loc[utentex['time_slot_from'] == '20:15:00']; s83 = utentex.loc[utentex['time_slot_from'] == '20:30:00']; s84 = utentex.loc[utentex['time_slot_from'] == '20:45:00']
    s85 = utentex.loc[utentex['time_slot_from'] == '21:00:00']; s86 = utentex.loc[utentex['time_slot_from'] == '21:15:00']; s87 = utentex.loc[utentex['time_slot_from'] == '21:30:00']; s88 = utentex.loc[utentex['time_slot_from'] == '21:45:00']
    s89 = utentex.loc[utentex['time_slot_from'] == '22:00:00']; s90 = utentex.loc[utentex['time_slot_from'] == '22:15:00']; s91 = utentex.loc[utentex['time_slot_from'] == '22:30:00']; s92 = utentex.loc[utentex['time_slot_from'] == '22:45:00']
    s93 = utentex.loc[utentex['time_slot_from'] == '23:00:00']; s94 = utentex.loc[utentex['time_slot_from'] == '23:15:00']; s95 = utentex.loc[utentex['time_slot_from'] == '23:30:00']; s96 = utentex.loc[utentex['time_slot_from'] == '23:45:00']


    z1 = len(s1); z2 = len(s2); z3 = len(s3); z4 = len(s4); z5 = len(s5); z6 = len(s6); z7 = len(s7); z8 = len(s8); z9 = len(s9)
    z10 = len(s10); z11 = len(s11); z12 = len(s12); z13 = len(s13); z14 = len(s14); z15 = len(s15); z16 = len(s16); z17 = len(s17); z18 = len(s18); z19 = len(s19)
    z20 = len(s20); z21 = len(s21); z22 = len(s22); z23 = len(s23); z24 = len(s24); z25 = len(s25); z26 = len(s26); z27 = len(s27); z28 = len(s28); z29 = len(s29)
    z30 = len(s30); z31 = len(s31); z32 = len(s32); z33 = len(s33); z34 = len(s34); z35 = len(s35); z36 = len(s36); z37 = len(s37); z38 = len(s38); z39 = len(s39)
    z40 = len(s40); z41 = len(s41); z42 = len(s42); z43 = len(s43); z44 = len(s44); z45 = len(s45); z46 = len(s46); z47 = len(s47); z48 = len(s48); z49 = len(s49)
    z50 = len(s50); z51 = len(s51); z52 = len(s52); z53 = len(s53); z54 = len(s54); z55 = len(s55); z56 = len(s56); z57 = len(s57); z58 = len(s58); z59 = len(s59)
    z60 = len(s60); z61 = len(s61); z62 = len(s62); z63 = len(s63); z64 = len(s64); z65 = len(s65); z66 = len(s66); z67 = len(s67); z68 = len(s68); z69 = len(s69)
    z70 = len(s70); z71 = len(s71); z72 = len(s72); z73 = len(s73); z74 = len(s74); z75 = len(s75); z76 = len(s76); z77 = len(s77); z78 = len(s78); z79 = len(s79) 
    z80 = len(s80); z81 = len(s81); z82 = len(s82); z83 = len(s83); z84 = len(s84); z85 = len(s85); z86 = len(s86); z87 = len(s87); z88 = len(s88); z89 = len(s89)
    z90 = len(s90); z91 = len(s91); z92 = len(s92); z93 = len(s93); z94 = len(s94) ; z95 = len(s95); z96 = len(s96)
    k = [z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, z16, z17, z18, z19, z20, z21, z22, z23, z24, z25, z26, z27, z28, z29, z30, z31, z32, z33, z34, z35, z36, z37, z38, z39, z40, z41, z42, z43, z44, z45, z46, z47, z48, z49, z50, z51, z52, z53, z54, z55, z56, z57, z58, z59, z60, z61, z62, z63, z64, z65, z66, z67, z68, z69, z70, z71, z72, z73, z74, z75, z76, z77, z78, z79, z80, z81, z82, z83, z84, z85, z86, z87, z88, z89, z90, z91, z92, z93, z94, z95, z96]


    return k

############################################################################
# calling the function to make the data sets to plot 
for b in range(len(j)): 
    counter[:,b] = function(rowsData[rowsData.day == j[b]])

##################################################### defining and calling the  passengers function 
counter_2 =  np.copy(counter)
counter_4 = np.copy(counter)

for i in range(16): 
    counter_2 = np.delete(counter_2, i, 0)
###
more = np.array([3.,	2.917,	5.,	6.063,	8.128,	9.581,	18.263,	16.143,	6.732,	8.293,	7.361,	4.139,	5.781,	7.766,	7.174,	6.476,	5.702,	2.971,	1.261,	2.579,	6.745])

coeff = np.vstack((coeff, more))
lo = 0
up = 1
if h == '1':
    lo =-1
elif h == '3':
    lo=0; up =1;
elif h == '5':
    lo =1;up=2;
elif h == '6':
    lo =2;up=3;
elif h == '7':
    lo =3;up=4;
elif h == '8A':
    lo =4;up=5;
elif h == '9':
    lo =5;up=6;
elif h == '10':
    lo =6;up=7;
elif h == '13':
    lo =7;up=8;
elif h == '15':
    lo =8;up=9;
elif h == '17':
    lo =9;up=10;
elif h == '18':
    lo =10;up=11;
elif h == '20':
    lo =11;up=12;
elif h == '41':
    lo =12;up=13;
elif h == '30R':
    lo =13;up=14;
elif h == '31R':
    lo =14;up=15;
elif h == 'M':
    lo =15;up=16;
elif h == 'PF':
    lo =16;up=17;
elif h == 'PQ':
    lo =17;up=18;
elif h == 'QS':
    lo =18;up=19;
elif h == '1Q':
    lo =19;up=20;


def to_passengern(passen) :
    if h == '1':
        new = np.zeros((80, len(j)-1), dtype= float)
        new = passen[0:4, :] * coeff[lo, 0:1]; new = np.vstack((new, passen[4:8, :] * coeff[lo, 1:2]))
        new = np.vstack((new, passen[8:12, :] * coeff[lo, 2:3])); new = np.vstack((new, passen[12:16, :] * coeff[lo, 3:4]))  
        new = np.vstack((new, passen[16:20, :] * coeff[lo, 4:5])); new = np.vstack((new, passen[20:24, :] * coeff[lo, 5:6]))  
        new = np.vstack((new, passen[24:28, :] * coeff[lo, 6:7])); new = np.vstack((new, passen[28:32, :] * coeff[lo, 7:8])) 
        new = np.vstack((new, passen[32:36, :] * coeff[lo, 8:9])); new = np.vstack((new, passen[36:40, :] * coeff[lo, 9:10]))  
        new = np.vstack((new, passen[40:44, :] * coeff[lo, 10:11])); new = np.vstack((new, passen[44:48, :] * coeff[lo, 11:12]))  
        new = np.vstack((new, passen[48:52, :] * coeff[lo, 12:13])); new = np.vstack((new, passen[52:56, :] * coeff[lo, 13:14]))  
        new = np.vstack((new, passen[56:60, :] * coeff[lo, 14:15])); new = np.vstack((new, passen[60:64, :] * coeff[lo, 15:16])) 
        new = np.vstack((new, passen[64:68, :] * coeff[lo, 16:17])); new = np.vstack((new, passen[68:72, :] * coeff[lo, 17:18]))  
        new = np.vstack((new, passen[72:76, :] * coeff[lo, 18:19])); new = np.vstack((new, passen[76:80, :] * coeff[lo, 19:20]))   
        return new
    else:
        new = np.zeros((80, len(j)-1), dtype= float)
        new = passen[0:4, :] * coeff[lo:up, 0:1]; new = np.vstack((new, passen[4:8, :] * coeff[lo:up, 1:2]))
        new = np.vstack((new, passen[8:12, :] * coeff[lo:up, 2:3])); new = np.vstack((new, passen[12:16, :] * coeff[lo:up, 3:4]))  
        new = np.vstack((new, passen[16:20, :] * coeff[lo:up, 4:5])); new = np.vstack((new, passen[20:24, :] * coeff[lo:up, 5:6]))  
        new = np.vstack((new, passen[24:28, :] * coeff[lo:up, 6:7])); new = np.vstack((new, passen[28:32, :] * coeff[lo:up, 7:8])) 
        new = np.vstack((new, passen[32:36, :] * coeff[lo:up, 8:9])); new = np.vstack((new, passen[36:40, :] * coeff[lo:up, 9:10]))  
        new = np.vstack((new, passen[40:44, :] * coeff[lo:up, 10:11])); new = np.vstack((new, passen[44:48, :] * coeff[lo:up, 11:12]))  
        new = np.vstack((new, passen[48:52, :] * coeff[lo:up, 12:13])); new = np.vstack((new, passen[52:56, :] * coeff[lo:up, 13:14]))  
        new = np.vstack((new, passen[56:60, :] * coeff[lo:up, 14:15])); new = np.vstack((new, passen[60:64, :] * coeff[lo:up, 15:16])) 
        new = np.vstack((new, passen[64:68, :] * coeff[lo:up, 16:17])); new = np.vstack((new, passen[68:72, :] * coeff[lo:up, 17:18]))  
        new = np.vstack((new, passen[72:76, :] * coeff[lo:up, 18:19])); new = np.vstack((new, passen[76:80, :] * coeff[lo:up, 19:20]))   
        return new 

######### calling the calibration function ####### calculating average , maxima, minima and storing them in a numpy array
if m == 'l':
    counter_3 = to_passengern(counter_2)


    counter_1 = np.copy(counter_2)
    avg = counter_3.mean(axis=1)
    maxInRows = np.amax(counter_3, axis=1)
    minInRows = np.amin(counter_3, axis=1) 

    avg1 = counter.mean(axis=1)
    maxInRows1 = np.amax(counter, axis=1)
    minInRows1 = np.amin(counter, axis=1)

else: 
    avg1 = counter.mean(axis=1)
    maxInRows1 = np.amax(counter, axis=1)
    minInRows1 = np.amin(counter, axis=1)


############################ plotting 
##creating the arrays with the data to plot 
time = ['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45', '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45']
#making the plots 
time1 = ['04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45', '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45']
#making the plots 
r = 0 
b = 0 
g = 0  

def quarter_hour(x):
     return x*4
#
def quarter (x):
    return x/4
#
if m == 'l':
    fig, axs = plt.subplots(2, sharex= True, sharey= True)  # creating 2 figures in one plot 
    for p in range(len(j)): # plotting the single days in axs[0] (first figure)
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        axs[0].plot(time1, counter_3[:,p], label = j[p], marker='o', c = color)
    axs[0].grid(True)
    axs[0].legend(loc="upper right")
    ##############################################################
    # plotting the average, maxima and minima in axs[1] (second figure)
    axs[1].plot(time1, avg, label = "media")
    axs[1].scatter(time1, avg)
    axs[1].plot(time1, maxInRows, label = "maximum", color = 'red')
    axs[1].scatter(time1, maxInRows, color = 'red')
    axs[1].plot(time1, minInRows, label = "minimum", color = 'black')
    axs[1].scatter(time1, minInRows, color = 'black')
    axs[1].legend(loc="upper right")
    axs[1].grid(True)
    
    
    
    fig.suptitle('Passeggeri a bordo della linea ' + str(h) + ' '+ dy)
    secax = axs[0].secondary_yaxis('right', functions=(quarter_hour, quarter) )
    secax.set_ylabel('passeggeri ora')
    secax = axs[1].secondary_yaxis('right', functions=(quarter_hour, quarter) )
    secax.set_ylabel('passeggeri ora')
    axs[1].set_xlabel('ore')
    axs[0].set_ylabel('passeggeri per quarto di ora')
    axs[1].set_ylabel('passeggeri per quarto di ora')
    plt.setp(axs, xticks =['04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00' ], yticks=(np.arange(min(maxInRows), max(maxInRows)+2, 15.0)))
    ############
    # showing the plots 
    plt.show()
    plt.clf()  
    color_index=0
    r = 0 
    b = 0 
    g = 0 
    fig1, axs1 = plt.subplots(2, sharex= True, sharey= True)  # creating 2 figures in one plot 
    for p in range(len(j)): # plotting the single days in axs[0] (first figure)
        r = random.random()
        b = random.random()
        g = random.random()
        color1 = (r, g, b)
        axs1[0].plot(time, counter_4[:,p], label = j[p], marker='o', c=color1)
    axs1[0].grid(True)
    axs1[0].legend(loc="upper right")
    ##############################################################
    # plotting the average, maxima and minima in axs[1] (second figure)
    axs1[1].plot(time, avg1, label = "media")
    axs1[1].scatter(time, avg1)
    axs1[1].plot(time, maxInRows1, label = "maximum", color = 'red')
    axs1[1].scatter(time, maxInRows1, color = 'red')
    axs1[1].plot(time, minInRows1, label = "minimum", color = 'black')
    axs1[1].scatter(time, minInRows1, color = 'black')
    axs1[1].legend(loc="upper right")
    axs1[1].grid(True)
    
    # adaptive selection of the title 
    if m == 'l':
        fig1.suptitle('Interrogazioni su BusFinder per la linea ' + str(h) + ' '+ dy)
    ########################################################
    # setting the x and y axis scales accordingly 
    axs1[1].set_xlabel('ore')
    axs1[0].set_ylabel('numero chiamate')
    plt.setp(axs1, xticks =['00:00', '01:00', '02:00', '03:00','04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00' ],  yticks=(np.arange(min(maxInRows1), max(maxInRows1)+2, 2.0)))
    ############ 
    #showing the plots 
    plt.show()
    plt.clf()   




else:
    fig1, axs1 = plt.subplots(2, sharex= True, sharey= True)  # creating 2 figures in one plot 
    for p in range(len(j)): # plotting the single days in axs[0] (first figure)
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        axs1[0].plot(time, counter[:,p], label = j[p], marker='o', c = color)
    axs1[0].grid(True)
    axs1[0].legend(loc="upper right")
    ##############################################################
    # plotting the average, maxima and minima in axs[1] (second figure)
    axs1[1].plot(time, avg1, label = "media")
    axs1[1].scatter(time, avg1)
    axs1[1].plot(time, maxInRows1, label = "maximum", color = 'red')
    axs1[1].scatter(time, maxInRows1, color = 'red')
    axs1[1].plot(time, minInRows1, label = "minimum", color = 'black')
    axs1[1].scatter(time, minInRows1, color = 'black')
    axs1[1].legend(loc="upper right")
    axs1[1].grid(True)
    # adaptive selection of the title 
    if m == 'p':
        fig1.suptitle('Numero chiamate palina ' + h + ' ' + dy)
    elif m == 'u': 
        fig1.suptitle('Numero chiamate utente ' + h + ' ' + dy)
    ########################################################
    # setting the x and y axis scales accordingly 
    axs1[1].set_xlabel('ore')
    axs1[0].set_ylabel('numero chiamate')
    plt.setp(axs1, xticks =['00:00', '01:00', '02:00', '03:00','04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00' ],
      yticks=(np.arange(min(maxInRows1), max(maxInRows1)+2, 2.0)))
    # showing the plots 
    plt.show()
    plt.clf()   