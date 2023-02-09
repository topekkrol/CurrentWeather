import requests
import pandas as pd
from doCSV import do_csv
lista_opadow =[]
def pogoda():
    obecna_pogoda = requests.get(f'http://api.weatherapi.com/v1/current.json?key=c475016fbc734b2a99475950230902&q=Rzeszów&aqi=yes')

    pogoda_json = obecna_pogoda.json()

    return  pogoda_json['current']['precip_mm']

# lista_opadow.append(pogoda())
lista_opadow=[0.4,0.5,3,4.9] # testowo

if len(lista_opadow) == 4:
    do_csv(sum(lista_opadow))

