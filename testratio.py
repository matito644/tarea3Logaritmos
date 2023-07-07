import csv
import time
import matplotlib.pyplot as plt
import numpy as np
from main import BloomFilterWithoutKandM
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
    csv_movies = csv.reader(open('Film-Names.csv', 'r'), delimiter=',')
    list_of_movies_for_testing = []
    list_for_testing = []
    # insertar los nombres en el filtro
    for row in csv_names:
        if row[0] == "Name":
            continue
        bloomFilter.add(row[0])
        list_for_testing.append(row[0])
    
    for row in csv_movies:
        list_of_movies_for_testing.append(row[0])
    
    return bloomFilter, list_for_testing, list_of_movies_for_testing


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
# fijaremos un k para el test! y de ahí obtendremos m y luego mediremos la cantidad de falsos positivos!
# la idea es ir mostrando varios k's hasta ver que converga hasta el numero esperado de 


def test_and_msr_false_positives(bloomFilter: BloomFilterWithoutKandM, list_of_movies):
    pos = 0
    for movie in list_of_movies:
        if bloomFilter.check(movie):
            pos += 1
    return pos - len(list_of_movies) * 0.7 
    
def test_with_alpha(alpha, n=10000, k = 10, trials=20):
    m = int(k/alpha)
    bloomFilter, list_of_names, list_of_movies = load_test_case(k ,m)
    list_for_testing = generate_names_with_ratio(list_of_names=list_of_names, list_of_movies=list_of_movies, n=n)
    false_pos = 0
    for _ in range(trials):
        false_pos += test_and_msr_false_positives(bloomFilter, list_for_testing)
    false_pos_mean = false_pos / trials
    
    return false_pos_mean
    

def test_a_list_of_alphas(list_of_alphas, k=10):
    res= []    
    for alpha in list_of_alphas:
        res += [test_with_alpha(alpha, k=k)]
    return res


if __name__ == "__main__":
    alphas = np.linspace(0.000001, 0.00001, num=20)
    for k in range(2,23, 2):
        y_vals = test_a_list_of_alphas(alphas, k = k)
        fig = plt.figure()
        plt.scatter(alphas, y_vals, color='blue')
        plt.title(f"#falsos postivos con k = {k} vs α")
        plt.ylabel(r"#falsos positivos")
        plt.xlabel(r"$alpha$")
        plt.savefig(f"figures/Figura_k-{k}.png")
        print(f"Figura {k} listo!")
