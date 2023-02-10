from datetime import datetime
import pandas as pd
import csv

paczucha ={}

def dzis():
    now = datetime.now()
    if now.day >= 10:
        dzis = '-'+str(now.day)+'T'
    else:
        dzis =  '-0'+str(now.day)+'T'

    miesiac = datetime.now().month
    data = str(miesiac)+dzis
    return  data

def do_csv(suma,plyk):

    new_line_df = pd.DataFrame({dzis():suma}, index=[dzis()])
    new_line_df.to_csv(f'C:/Nowy_folder/{plyk}.csv', index=True, header=False, quotechar=' ')



