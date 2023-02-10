import csv
import requests
import os
from doPSQL import do_Sql
from doCSV import do_csv

import random

lista_opadow=[]

def pogoda():
    # obecna_pogoda = requests.get(f'http://api.weatherapi.com/v1/current.json?key=c475016fbc734b2a99475950230902&q=Rzeszów&aqi=yes')
    #
    # pogoda_json = obecna_pogoda.json()
    #
    # return  pogoda_json['current']['precip_mm']

    return random.uniform(10.5, 75.5)

x = pogoda()

try:
    plik = open('wewnetrze.csv','r')
    tekst = list(csv.reader(plik))
except:
    plik = open('wewnetrze.csv','w')
    tekst=[[]]

tekst[0].append(float(pogoda()))

plik = open('wewnetrze.csv','w')
write = csv.writer(plik)
write.writerow(tekst[0])
plik.close()

if len(tekst[0]) == 4:
    suma = 0
    for wartosci in tekst[0]:
        suma += float(wartosci)
    print(suma)
    print(tekst[0])
    plyk = 'current'
    print(suma)
    do_csv(suma,plyk)
    do_Sql(plyk)
    os.remove('wewnetrze.csv')
    os.remove(f'C:/Nowy_folder/{plyk}.csv')

