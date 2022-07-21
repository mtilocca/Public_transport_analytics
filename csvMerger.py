# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:23:31 2020

@author: M. Tilocca
"""
import os
import glob
import pandas as pd

os.getcwd()
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combineddatafile.csv", index=False, encoding='utf-8-sig') 
#                     mettere nome al posto di combinedfile.csv eg.(documento.csv), mantenere sempre dopo il nome che viene scelto il '.csv' 
# il programma legge la directory in cui si trova e concatena tutti i file csv presenti in quella directory. I files csv vengono concatenati 
# seguendo l'ordine alfabetico dei nomi dei file eg.( A1.csv, A2.csv, A3.csv) per primo verra' messo A1, poi A2 e A3 nel nuovo file csv. 
# successivamente caricare il nuovo file csv creato nel programma linee_palinee_arco_temporale per svolgere ulteriori operazioni di data processing