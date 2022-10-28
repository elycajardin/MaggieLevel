#importación  de modulos, algunos comandos especificos para Mac (requests)

from pip._vendor import requests
import csv
import json
import time

#definición bucle principal para realizar los GET a la API y obtener las quotes cada 30 segundos de acuerdo con los criterios de separar en General, Homer y Lisa  
while True:
  URL: str = "https://thesimpsonsquoteapi.glitch.me/quotes"
  respuesta = requests.get(url = URL)
  datos= respuesta.json()
  frase_simpson: str= datos[0]['quote']
  autor: str= datos[0]['character']
  #list=[]
  #list.extend(datos.values())
  if autor == 'Lisa Simpson':
    my_dict = {'quote': frase_simpson, 'character':autor}
    with open('/Users/elyca.jardin/Documents/GitHub/MaggieLevel/Lisa/Lisa.csv', 'a') as csvfile:
      w = csv.DictWriter(csvfile, my_dict.keys())

      w.writerow(my_dict)
    
  elif autor == 'Homer Simpson':
    my_dict = {'quote': frase_simpson, 'character':autor}
    with open('/Users/elyca.jardin/Documents/GitHub/MaggieLevel/Homer/Homer.csv', 'a') as csvfile:
      w = csv.DictWriter(csvfile, my_dict.keys())

      w.writerow(my_dict)

  else:
      
    my_dict = {'quote': frase_simpson, 'character':autor}
    with open('/Users/elyca.jardin/Documents/GitHub/MaggieLevel/General/General.csv', 'a') as csvfile:
      w = csv.DictWriter(csvfile, my_dict.keys())

      w.writerow(my_dict)
  time.sleep(30) 