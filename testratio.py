import csv
import time
import matplotlib.pyplot as plt
from main import BloomFilter, BloomFilterWithoutKandM
import random
N = 93889
FP = 0.1
# crear el filtro de Bloom
def load_test_case(k,m):
    bloomFilter = BloomFilterWithoutKandM(k, m)
    bloomFilter.k = k
    bloomFilter.m = m
    # leer los csv
    csv_names = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
    list_for_testing = []
    # insertar los nombres en el filtro
    for row in csv_names:
        if row[0] == "Name":
            continue
        bloomFilter.add(row[0])
        list_for_testing.append(row[0])
    return bloomFilter, row[0]
#ahora lo que queremos hacer es
#1. generar nombres con una razon r, esto se hace con la siguiente funcion
# vamos a escoger una razon de 0.7
#Notar que el orden no importa! ya que nos importa el resultado de las queries!
def generate_names_with_ratio(list_of_names, list_of_movies, n, r=0.7):
    return random.sample(list_of_names, int(n*r)) + random.sample(list_of_movies, int(n*(1-r)))
#2. luego de generar los nombres, vamos a asumir lo siguiente
# Notemos que con el test a realizar, podemos esperar que el valor 
# de nombres que son positivos seran: (# valores que estan) + (# falsos positivos)
# si nuestro filtro de bloom es bueno, la idea es que estos falsos tengan una probabilidad de 0.1
# por lo tanto el numero esperado de falsos positivos es (# numero de peliculas) * 0.1
# Entonces hay que alcanzar este ese valor aproximado! ie 
# Para alcanzar el optimo solo basta con chequear que el numero de falsos positivos sea el dicho anteriromente
# dicho esto podemos asumir para encontrar ese k y M optimos podemos asumir como hipotesis lo siguiente
#
#       H1: k es lineal con respecto a M ie: k = α M para algun α en un rango
#
# Ahora, por teoria esperamos que α = ln(2)/n; donde n = (# valores esperados en el filtro de bloom)
# y como n = 93889 y fp = 0.1, esperamos que α ~ 7.382e-06 = 0.000007382

def test_a_list_of_alphas(list_of_alphas):
    ...
