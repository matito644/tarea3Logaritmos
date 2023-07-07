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
# si nuestro filtro de bloom es bueno, la idea es que estos falsos tengan una probabilidad de fp
# por lo tanto el numero esperado de falsos positivos es (# numero de peliculas) * fp
# Entonces hay que alcanzar este ese valor aproximado! ie 
# Para alcanzar el optimo solo basta con chequear que el numero de falsos positivos sea el dicho anteriromente
# dicho esto podemos asumir para encontrar ese k y M optimos podemos asumir como hipotesis lo siguiente
#
#       H1: k es lineal con respecto a M ie: k = α M, es optimo para algun α en un rango 
#           y esperamos que α = ln(2)/n donde n es el numero esperado de valores que tenemos para un filtro de bloom
#
# Ahora, por teoria esperamos que α = ln(2)/n; donde n = (# valores esperados en el filtro de bloom)
# y como n = 93889 y fp = 0.1, esperamos que α ~ 7.382e-06 = 0.000007382
# fijaremos un k para el test! y de ahí obtendremos m y luego mediremos la cantidad de falsos positivos!
# la idea es ir mostrando varios k's hasta ver que converga hasta el numero esperado de 
KOPT = 3
MOPT = 449965

def test_m_and_k_for_optimum(n, trials=3):
    ks = list(range(1,6))
    ms = list(range(440000, 460001, 500))
    for k in ks:
        false_pos_list = []
        for m in ms:
            bloom_filter, list_names, list_movies = load_test_case(k,m)
            list_for_testing = generate_names_with_ratio(list_names, list_movies, n = n)
            #Queremos encontrar el que da mas cercano al minimo, ie el que da 
            # una cantidad de falsos positivos cercano a 
            # fp*(# peliculas)
            false_pos = 0
            for _ in range(trials):
                false_pos += test_and_msr_false_positives(bloom_filter, list_for_testing)
            false_pos_mean = false_pos / trials
            false_pos_list.append(false_pos_mean)
        fig = plt.figure()
        plt.plot(ms, false_pos_list, color='blue', marker='.')
        ax = plt.gca()
        ax.set_ylim([150,700])
        plt.title(f"#falsos postivos con k = {k} vs M")
        plt.ylabel(r"#falsos positivos")
        plt.xlabel(r"Numero de bits (M)")
        plt.savefig(f"figures/Figura_k-{k}.png")
        print(f"Figura {k} listo!")





def test_and_msr_false_positives(bloomFilter: BloomFilterWithoutKandM, list_of_movies):
    pos = 0
    for movie in list_of_movies:
        if bloomFilter.check(movie):
            pos += 1
    return pos - len(list_of_movies) * 0.7 
    
# def test_with_alpha(alpha, n=10000, k = 10, trials=20):
#     m = int(k/alpha)
#     bloomFilter, list_of_names, list_of_movies = load_test_case(k ,m)
#     list_for_testing = generate_names_with_ratio(list_of_names=list_of_names, list_of_movies=list_of_movies, n=n)
#     false_pos = 0
#     for _ in range(trials):
#         false_pos += test_and_msr_false_positives(bloomFilter, list_for_testing)
#     false_pos_mean = false_pos / trials
    
#     return false_pos_mean
    

# def test_a_list_of_alphas(list_of_alphas, k=10):
#     res= []    
#     for alpha in list_of_alphas:
#         res += [test_with_alpha(alpha, k=k)]
#     return res


if __name__ == "__main__":
    test_m_and_k_for_optimum(n=10000, trials=50)
