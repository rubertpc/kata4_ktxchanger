from tkinter import *
from tkinter import ttk

import configparser
import json

import requests

config = configparser.ConfigParser()
config.read('config.ini')

inSymbol = input('Qué moneda quieres convertir:')
outSymbol = input('En qué otra moneda:')


url = config['fixer.io']['RATE_LATEST_EP']
api_key = config['fixer.io']['API_KEY']

url = url.format(api_key, inSymbol, outSymbol)
response = requests.get(url)
if response.status_code == 200:
    print(response.text)
    #currencies = json.loads(response.text)
    #print(currencies)
    #print(currencies['symbols']['USD'])
else:
    print("Se ha producido un error en la petición:", response.status_code)




