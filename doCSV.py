from datetime import datetime
import pandas as pd

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

def do_csv(srednia):

    new_line_df = pd.DataFrame({dzis():srednia}, index=[dzis()])
    new_line_df.to_csv(f'C:/Nowy_folder/current.csv', index=True, header=False, quotechar=' ')